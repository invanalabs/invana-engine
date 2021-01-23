from graphene import ObjectType, String, Field, JSONString, ResolveInfo, Int, List
from ..types.element import GrapheneVertexType, GrapheneEdgeType, AnyField, GrapheneVertexOrEdgeType
from ..types.gremlin import LabelStats
from .client import GenericClientInfoSchema
from typing import Any

default_pagination_size = 10


class ManagementQuerySchema:
    get_vertices_label_stats = Field(List(LabelStats), namespace=String())
    get_edges_label_stats = Field(List(LabelStats), namespace=String())
    get_vertex_label_stats = Field(LabelStats, label=String())
    get_edge_label_stats = Field(LabelStats, label=String())

    def resolve_get_vertices_label_stats(self, info: ResolveInfo, namespace: str = None):
        data = info.context['request'].app.state.gremlin_client.management.get_vertices_label_stats(namespace=namespace)
        return data

    def resolve_get_edges_label_stats(self, info: ResolveInfo, namespace: str = None):
        data = info.context['request'].app.state.gremlin_client.management.get_edges_label_stats(namespace=namespace)
        return data


    def resolve_get_vertex_label_stats(self, info: ResolveInfo, label: str = None) -> any:
        return info.context['request'].app.state.gremlin_client.management.get_vertex_label_stats(label)

    def resolve_get_edge_label_stats(self, info: ResolveInfo, label: str = None) -> any:
        return info.context['request'].app.state.gremlin_client.management.get_edge_label_stats(label)

class GremlinVertexQuerySchema:
    get_vertex_by_id = Field(GrapheneVertexType, id=String(required=True))
    filter_vertex = Field(List(GrapheneVertexType), label=String(), namespace=String(), query=JSONString(),
                          limit=Int(default_value=default_pagination_size), skip=Int())
    get_in_edges_and_vertices = Field(List(GrapheneVertexOrEdgeType), id=AnyField(required=True),
                                      label=String(), namespace=String(), query=JSONString(),
                                      limit=Int(default_value=default_pagination_size), skip=Int())
    get_out_edges_and_vertices = Field(List(GrapheneVertexOrEdgeType), id=AnyField(required=True),
                                       label=String(), namespace=String(), query=JSONString(),
                                       limit=Int(default_value=default_pagination_size), skip=Int())
    get_neighbor_edges_and_vertices = Field(List(GrapheneVertexOrEdgeType), id=AnyField(),
                                            label=String(), namespace=String(), query=JSONString(),
                                            limit=Int(default_value=default_pagination_size), skip=Int())
    get_or_create_vertex = Field(GrapheneVertexType, label=String(), namespace=String(), properties=JSONString())

    def resolve_get_vertex_by_id(self, info: ResolveInfo, id: str):
        data = info.context['request'].app.state.gremlin_client.vertex.read_one(id)
        return data.__dict__() if data else None

    def resolve_filter_vertex(self, info: ResolveInfo, label: str = None, namespace: str = None, query: str = None,
                              limit: int = default_pagination_size, skip: int = 0):
        data = info.context['request'].app.state.gremlin_client.vertex.read_many(
            label=label, namespace=namespace, query=query, limit=limit, skip=skip
        )
        return [datum.__dict__() for datum in data]

    def resolve_get_in_edges_and_vertices(self, info: ResolveInfo,
                                          id: Any = None, label: str = None, namespace: str = None,
                                          query: str = None,
                                          limit: int = default_pagination_size, skip: int = 0):
        data = info.context['request'].app.state.gremlin_client.vertex.read_in_edges_and_vertices(
            id, label=label, namespace=namespace, query=query, limit=limit, skip=skip
        )
        return [datum.__dict__() for datum in data]

    def resolve_get_out_edges_and_vertices(self, info: ResolveInfo,
                                           id: Any = None, label: str = None, namespace: str = None, query: str = None,
                                           limit: int = default_pagination_size, skip: int = 0):
        data = info.context['request'].app.state.gremlin_client.vertex.read_out_edges_and_vertices(
            id, label=label, namespace=namespace, query=query, limit=limit, skip=skip
        )
        return [datum.__dict__() for datum in data]

    def resolve_get_neighbor_edges_and_vertices(self, info: ResolveInfo,
                                                id: Any = None, label: str = None, namespace: str = None,
                                                query: str = None,
                                                limit: int = default_pagination_size, skip: int = 0):
        data = info.context['request'].app.state.gremlin_client.vertex.get_neighbor_edges_and_vertices(
            vertex_id=id, label=label, namespace=namespace, query=query, limit=limit, skip=skip
        )
        return [datum.__dict__() for datum in data]

    def resolve_get_or_create_vertex(self, info: ResolveInfo, label: str = None, namespace: str = None,
                                     properties: str = None):
        return info.context['request'].app.state.gremlin_client.vertex.get_or_create(label=label,
                                                                                     namespace=namespace,
                                                                                     properties=properties)


class GremlinEdgeQuerySchema:
    get_edge_by_id = Field(GrapheneEdgeType, id=String(required=True))
    filter_edge = Field(List(GrapheneEdgeType), label=String(), query=JSONString(),
                        limit=Int(default_value=default_pagination_size), skip=Int())
    filter_edge_and_get_neighbor_vertices = Field(List(GrapheneEdgeType), label=String(), query=JSONString(),
                                                  limit=Int(default_value=default_pagination_size), skip=Int())
    get_or_create_edge = Field(GrapheneEdgeType, label=String(), namespace=String(), properties=JSONString())

    def resolve_get_edge_by_id(self, info: ResolveInfo, id: str):
        data = info.context['request'].app.state.gremlin_client.edge.read_one(id)
        return data.__dict__() if data else None

    def resolve_filter_edge(self, info: ResolveInfo, label: str = None, namespace: str = None,
                            query: str = None, limit: int = default_pagination_size, skip: int = 0):
        data = info.context['request'].app.state.gremlin_client.edge.read_many(
            label=label, namespace=namespace, query=query, limit=limit, skip=skip
        )
        return [datum.__dict__() for datum in data]

    def resolve_filter_edge_and_get_neighbor_vertices(self, info: ResolveInfo, label: str = None,
                                                      namespace: str = None, query: str = None,
                                                      limit: int = default_pagination_size, skip: int = 0):
        data = info.context['request'].app.state.gremlin_client.edge.filter_edge_and_get_neighbor_vertices(
            label=label, namespace=namespace, query=query, limit=limit, skip=skip
        )

        #
        return [datum.__dict__() for datum in data]

    def resolve_get_or_create_edge(self, info: ResolveInfo, label: str = None, namespace: str = None,
                                   properties: str = None):
        return info.context['request'].app.state.gremlin_client.edge.get_or_create(label=label,
                                                                                   namespace=namespace,
                                                                                   properties=properties)


class GremlinRawQuerySchema:
    raw_query = Field(List(GrapheneEdgeType), gremlin=String())

    def resolve_raw_query(self, info: ResolveInfo, gremlin: str) -> any:
        return info.context['request'].app.state.gremlin_client.execute_query(gremlin)



class GremlinQuery(ObjectType,
                   ManagementQuerySchema,
                   GremlinRawQuerySchema,
                   GremlinEdgeQuerySchema,
                   GremlinVertexQuerySchema,
                   GenericClientInfoSchema,
                   # GremlinManagementQuerySchema
                   ):
    pass
