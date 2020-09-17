from graphene import ObjectType, String, Field, JSONString, ResolveInfo, Int, NonNull, List
from ..types.element import GrapheneVertexType, GrapheneEdgeType
from .client import GenericClientInfoSchema

default_pagination_size = 10


class GremlinVertexQuerySchema:
    get_vertex_by_id = Field(GrapheneVertexType, id=String(required=True))
    filter_vertex = Field(List(GrapheneVertexType), label=String(), query=JSONString(),
                          limit=Int(default_value=default_pagination_size), skip=Int())
    get_in_edges_and_vertices = Field(List(GrapheneVertexType), id=String(required=True), label=String(), query=JSONString(),
                                 limit=Int(default_value=default_pagination_size), skip=Int())
    get_out_edges_and_vertices = Field(List(GrapheneVertexType), id=String(required=True), label=String(),
                                  query=JSONString(),
                                  limit=Int(default_value=default_pagination_size), skip=Int())

    remove_vertices = String(label=String(), query=JSONString())

    def resolve_get_vertex_by_id(self, info: ResolveInfo, id: str):
        data = info.context['request'].app.state.gremlin_client.vertex.read_one(id)
        return data.__dict__() if data else None

    def resolve_filter_vertex(self, info: ResolveInfo, label: str = None, query: str = None,
                              limit: int = default_pagination_size, skip: int = 0):
        data = info.context['request'].app.state.gremlin_client.vertex.read_many(
            label=label, query=query, limit=limit, skip=skip
        )
        return [datum.__dict__() for datum in data]

    def resolve_get_in_edges_and_vertices(self, info: ResolveInfo,
                                     id: str = None, label: str = None, query: str = None,
                                     limit: int = default_pagination_size, skip: int = 0):
        data = info.context['request'].app.state.gremlin_client.vertex.read_in_edges_and_vertices(
            id, label=label, query=query, limit=limit, skip=skip
        )
        return [datum.__dict__() for datum in data]

    def resolve_get_out_edges_and_vertices(self, info: ResolveInfo,
                                      id: str = None, label: str = None, query: str = None,
                                      limit: int = default_pagination_size, skip: int = 0):
        data = info.context['request'].app.state.gremlin_client.vertex.read_out_edges_and_vertices(
            id, label=label, query=query, limit=limit, skip=skip
        )
        return [datum.__dict__() for datum in data]


class GremlinEdgeQuerySchema:
    get_edge_by_id = Field(GrapheneEdgeType, id=String(required=True))
    filter_edge = Field(List(GrapheneEdgeType), label=String(), query=JSONString(),
                        limit=Int(default_value=default_pagination_size), skip=Int())

    def resolve_get_edge_by_id(self, info: ResolveInfo, id: str):
        data = info.context['request'].app.state.gremlin_client.edge.read_one(id)
        return data.__dict__() if data else None

    def resolve_filter_edge(self, info: ResolveInfo, label: str = None, query: str = None,
                            limit: int = default_pagination_size, skip: int = 0):
        data = info.context['request'].app.state.gremlin_client.edge.read_many(
            label=label, query=query, limit=limit, skip=skip
        )
        return [datum.__dict__() for datum in data]


class GremlinRawQuerySchema:
    raw_query = Field(List(GrapheneEdgeType), gremlin=String())

    def resolve_raw_query(self, info: ResolveInfo, gremlin: str) -> any:
        data = info.context['request'].app.state.gremlin_client.execute_query(gremlin)
        return data


class GremlinQuery(ObjectType, GremlinRawQuerySchema, GremlinEdgeQuerySchema, GremlinVertexQuerySchema,
                   GenericClientInfoSchema):
    pass