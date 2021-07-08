#  Copyright 2020 Invana
#
#  Licensed under the Apache License, Version 2.0 (the "License");
#  you may not use this file except in compliance with the License.
#  You may obtain a copy of the License at
#
#    http:www.apache.org/licenses/LICENSE-2.0
#
#  Unless required by applicable law or agreed to in writing, software
#  distributed under the License is distributed on an "AS IS" BASIS,
#  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#  See the License for the specific language governing permissions and
#  limitations under the License.
#

from invana_engine.gremlin.client import GremlinClient

gremlin_client = GremlinClient("ws://192.168.0.10:8182/gremlin")

# results = gremlin_client.schema.update_vertex_label("PlanetNew", "PlanetNew2")
# print("results", results)
#
# results = gremlin_client.schema.update_edge_label("has_satellite", "has_satellite2")
# print("results", results)

# results = gremlin_client.schema.get_graph_schema()
# print("results", results)


# results = gremlin_client.schema.get_all_vertices_schema()
# print("results", results)


#
# results2 = gremlin_client.query(
#     """
# mgmt = graph.openManagement();
# label_ = mgmt.getVertexLabel("my_vertex_6");
# label_.getProperties();
# mgmt.commit();
#     """,
#     serialize_elements=False
# )
# print("==results2", results2)

# exit()
results = gremlin_client.schema.create_vertex_label_with_schema(
    "Planet",
    name={"data_type": "String", "cardinality_type": "SINGLE"},
    mass_in_kgs={"data_type": "Double", "cardinality_type": "SINGLE"},
    radius_in_kms={"data_type": "Integer", "cardinality_type": "SINGLE"},
)
print("results", results)
#
# results = gremlin_client.schema.create_edge_label_with_schema(
#     "my_edge_5",
#     name5={"data_type": "String", "cardinality_type": "SINGLE"},
#     age5={"data_type": "Integer", "cardinality_type": "SINGLE"},
# )
# print("results", results)


# results = gremlin_client.schema.get_graph_schema()
# print("results", results)

# results = gremlin_client.schema.get_all_vertices_schema()
# print("results", results)
# #
# results = gremlin_client.schema.get_all_edges_schema()
# print("results", results)
#
# results = gremlin_client.schema.get_vertex_schema("my_vertex_6")
# print("results my_vertex_6", results)

# exit()
#
# results = gremlin_client.schema.get_vertex_label_schema("Teacher")
# print("results", results[0])

# results = gremlin_client.get_graph_features()
# print("results", results)

#
# results = gremlin_client.query("""
# mgmt = graph.openManagement()
#
#
# person = mgmt.makeVertexLabel('person').make()
# name = mgmt.makePropertyKey('name').dataType(String.class).cardinality(Cardinality.SET).make()
# birthDate = mgmt.makePropertyKey('birthDate').dataType(Long.class).cardinality(Cardinality.SINGLE).make()
# mgmt.addProperties(person, name, birthDate)
#
#
# follow = mgmt.makeEdgeLabel('follow').multiplicity(MULTI).make()
# name = mgmt.makePropertyKey('name').dataType(String.class).cardinality(Cardinality.SET).make()
# mgmt.addProperties(follow, name)
# mgmt.commit()
# """)
#
# print("results", results)
