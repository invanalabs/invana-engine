import pytest
from .sample_payloads.vertex import CREATE_VERTICES_SAMPLES
from .sample_payloads.edge import CREATE_EDGES_SAMPLES
from invana_engine.storages.gremlin.core.types import EdgeElement
from invana_engine.storages.gremlin.core.exceptions import InvalidQueryArguments
import os
from ..settings import TEST_GRAPH_HOST


class TestEdgesOperations:

    @pytest.fixture
    def gremlin_client(self):
        from invana_engine.storages import GremlinClient
        return GremlinClient(f"{TEST_GRAPH_HOST}/gremlin")

    @pytest.fixture
    def init_data(self):
        from invana_engine.storages import GremlinClient
        gremlin_client = GremlinClient(f"{TEST_GRAPH_HOST}/gremlin")
        for k, vertex_sample in CREATE_VERTICES_SAMPLES.items():
            gremlin_client.vertex.create(label=vertex_sample["label"], properties=vertex_sample["properties"])

        _ = gremlin_client.vertex.read_many()
        gremlin_client.close_connection()

        return _

    def test_create_edge(self, gremlin_client, init_data):
        for k, edge_sample in CREATE_EDGES_SAMPLES.items():
            result = gremlin_client.edge.create(
                label=edge_sample["label"],
                properties=edge_sample["properties"],
                inv=init_data[0].id,
                outv=init_data[1].id
            )
            print("==========result", result)
            assert isinstance(result, EdgeElement)
        gremlin_client.close_connection()

    def test_read_edge(self, gremlin_client):
        for k, edge_sample in CREATE_EDGES_SAMPLES.items():
            props = edge_sample['properties']
            responses = gremlin_client.edge.read_many(
                label=edge_sample['label'],
                query={list(props.keys())[0]: list(props.values())[0]})
            assert isinstance(responses, list)
            assert isinstance(responses[0], EdgeElement)
        gremlin_client.close_connection()

    def test_update_edge(self, gremlin_client):
        for k, edge_sample in CREATE_EDGES_SAMPLES.items():
            props = edge_sample['properties']
            response = gremlin_client.edge.read_many(
                label=edge_sample['label'],
                query={list(props.keys())[0]: list(props.values())[0]}
            )
            assert isinstance(response, list)
            response2 = gremlin_client.edge.update(response[0].id, properties={"new_field": "yeah!"})
            assert isinstance(response2, EdgeElement)
        gremlin_client.close_connection()

    def test_delete_single_edge(self, gremlin_client):
        for k, edge_sample in CREATE_EDGES_SAMPLES.items():
            props = edge_sample['properties']
            responses = gremlin_client.edge.read_many(
                label=edge_sample['label'],
                query={
                    list(props.keys())[0]: list(props.values())[0]
                }
            )
            assert isinstance(responses, list)
            response2 = gremlin_client.edge.delete_one(responses[0].id)
            responses3 = gremlin_client.edge.read_one(responses[0].id)
            assert responses3 is None
        gremlin_client.close_connection()

    def test_delete_edges(self, gremlin_client, init_data):
        for k, edge_sample in CREATE_EDGES_SAMPLES.items():
            gremlin_client.edge.create(
                label=edge_sample["label"],
                properties=edge_sample["properties"],
                inv=init_data[0].id,
                outv=init_data[1].id
            )
        responses = gremlin_client.edge.delete_many(label="has_satellite")
        responses2 = gremlin_client.edge.read_many(label="has_satellite")
        assert responses2.__len__() == 0
        gremlin_client.close_connection()

    def test_delete_many_noargs_sent_error(self, gremlin_client):
        with pytest.raises(InvalidQueryArguments, match=r"label and query"):
            responses = gremlin_client.edge.delete_many()
        gremlin_client.close_connection()

    def test_delete_one_noargs_sent_error(self, gremlin_client):
        with pytest.raises(TypeError, match=r"missing 1 required positional"):
            responses = gremlin_client.edge.delete_one()
        gremlin_client.close_connection()

    def test_read_one_noargs_sent_error(self, gremlin_client):
        with pytest.raises(TypeError, match=r"missing 1 required positional"):
            responses = gremlin_client.edge.read_one()
        gremlin_client.close_connection()
