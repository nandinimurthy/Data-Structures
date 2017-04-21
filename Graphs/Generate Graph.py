#! /usr/bin/python

#Use dictonaries to represent graph
graph = { "a" : ["c"],
          "b" : ["c", "e"],
          "c" : ["a", "b", "d", "e"],
          "d" : ["c"],
          "e" : ["c", "b"],
          "f" :[]
          }


# Generate list of all edges in form of 2-tuple
def generate_edges(graph):
    edges = []
    for node in graph:
        for neighbour in graph[node]:
            edges.append((node, neighbour))
    return edges

print(generate_edges(graph))

        


