import networkx as nx
import matplotlib.pyplot as mp

from networkx import Graph

def MyMinimumSpannigTree(graph) -> Graph:

    # Show algorithm steps
    show_steps = True

    if show_steps:
        print("I am following Prim's Algorithm")

    # Prim is a greedy algorithm: each step is important so a step by step in neccessary
    
    MST = nx.Graph()
    MST.add_nodes_from(graph.nodes())

    # Choose a start node
    start = list(graph.nodes())[0]

    # Need to keep track of nodes already visited in the MST
    visited = set()
    visited.add(start)

    if show_steps:
        print("Start node:", start)
        print("Step-by-step MST creation (Prim):")

    step = 1
    while len(visited) < graph.number_of_nodes():

        # Looking for the lowest weight edge that goes from visited to unvisited
        best_edge = None
        best_key = (float("inf"), "", "")

        # tie-break key in case 2 edges are the same weight
        for u in sorted(visited):
            for v in sorted(graph.neighbors(u)):
                if v not in visited:
                    w = int(graph.get_edge_data(u, v)["weight"])

                    # always take the smallest next edge without looking forward
                    # if there is a tie, always break the same way so is consistent
                    candidate_key = (w, str(u), str(v))
                    if candidate_key < best_key:
                        best_key = candidate_key
                        best_edge = (u, v)

        if best_edge is None:
            break

        u, v = best_edge
        best_weight = best_key[0]

        # Add the chosen edge to the MST and mark node as visited
        MST.add_edge(u, v, weight=best_weight)
        visited.add(v)

        if show_steps:
            print(f"\nStep {step}: choose edge ({u}, {v}) with weight {best_weight}")
            print("Visited nodes:", sorted(list(visited)))
            print("Current MST edges:", list(MST.edges()))

        step += 1

    if show_steps:
        print("\nFinal MST edges (with weights):")
        for (u, v, data) in MST.edges(data=True):
            print(f"({u}, {v}) weight={data['weight']}")

    return MST




# Steps necessary to take so I can reuse the same process for 3 graphs

def DrawGraphWithWeights(graph, pos, title):
    nx.draw_networkx_nodes(graph, pos)
    nx.draw_networkx_edges(graph, pos)
    nx.draw_networkx_labels(graph, pos)

    edge_labels = nx.get_edge_attributes(graph, "weight")
    nx.draw_networkx_edge_labels(graph, pos, edge_labels)

    mp.title(title)
    mp.show()


def RunTest(graph, graph_title):

    # This keeps the layout the same for each run
    pos = nx.circular_layout(graph)

    # Print title ans lines so output is easy to read/seperate 
    print("\n" + "=" * 60)
    print(graph_title)
    print("=" * 60)

    # 1. Create and depict the original connected graph using matplotlib.
    DrawGraphWithWeights(graph, pos, graph_title + " (Original)")

    # 2. Call the MyMinimumSpannigTree function.
    # 2.a/b already addressed previously in the code.
    T = MyMinimumSpannigTree(graph)

    # 3. Depict the final MST using matplotlib.
    DrawGraphWithWeights(T, pos, graph_title + " (MST - Prim)")

    return T


# GRAPH 1 

G1 = nx.Graph()
# G1 = (V,E)
# V = {"1","2","3","4","5","6"}
# E = {{"1","2"},{"1","3"},{"1","4"},{"2","3"},{"2","5"},{"3","4"},{"3","6"},{"4","5"},{"4","6"},{"5","6"}}

nodes1 = ["1", "2", "3", "4", "5", "6"]
G1.add_nodes_from(nodes1)

edges1 = [
    ("1", "2", {"weight": 3}),
    ("1", "3", {"weight": 5}),
    ("1", "4", {"weight": 2}),
    ("2", "3", {"weight": 8}),
    ("2", "5", {"weight": 2}),
    ("3", "4", {"weight": 6}),
    ("3", "6", {"weight": 9}),
    ("4", "5", {"weight": 5}),
    ("4", "6", {"weight": 3}),
    ("5", "6", {"weight": 4})
]
G1.add_edges_from(edges1)

T1 = RunTest(G1, "Graph 1")


# GRAPH 2

G2 = nx.Graph()
# G2 = (V, E)
# V = {"A","B","C","D","E"}
# E = {{"A","B"},{"A","C"},{"A","D"},{"B","C"},{"B","E"},{"C","D"},{"C","E"},{"D","E"}}

nodes2 = ["A", "B", "C", "D", "E"]
G2.add_nodes_from(nodes2)

edges2 = [
    ("A", "B", {"weight": 4}),
    ("A", "C", {"weight": 2}),
    ("A", "D", {"weight": 7}),
    ("B", "C", {"weight": 1}),
    ("B", "E", {"weight": 5}),
    ("C", "D", {"weight": 3}),
    ("C", "E", {"weight": 8}),
    ("D", "E", {"weight": 6})
]
G2.add_edges_from(edges2)

T2 = RunTest(G2, "Graph 2")


# GRAPH 3

G3 = nx.Graph()
# G3 = (V, E)
# V = {"1","2","3","4","5","6"}
# E = {{"1","2"},{"1","3"},{"1","4"},{"2","3"},{"2","5"},{"3","4"},{"3","6"},{"4","5"},{"4","6"},{"5","6"}}

nodes3 = ["1", "2", "3", "4", "5", "6"]
G3.add_nodes_from(nodes3)

edges3 = [
    ("1", "2", {"weight": 6}),
    ("1", "3", {"weight": 2}),
    ("1", "4", {"weight": 8}),
    ("2", "3", {"weight": 5}),
    ("2", "5", {"weight": 3}),
    ("3", "4", {"weight": 4}),
    ("3", "6", {"weight": 1}),
    ("4", "5", {"weight": 7}),
    ("4", "6", {"weight": 9}),
    ("5", "6", {"weight": 2})
]
G3.add_edges_from(edges3)

T3 = RunTest(G3, "Graph 3")
