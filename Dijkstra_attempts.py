
import math

graph = {
    "U": {"V": 6, "W": 7},
    "V": {"U":6, "X":10},
    "W": {"U": 7, "X": 1},
    "X": {"W": 1, "V": 10},
}


def dijkstra(graph):
    unvisited = []
    for i in graph.keys():
        unvisited.append(i)
    visited = []
    distances = {}
    for i in graph.keys():
        distances[i] = math.inf
    for i in graph.keys():
        distances[i] = 0 # notice this loop breaks after visiting the first one
        break
    
    # find shortest distance that has not been visited:
    while unvisited:
        distances = dict(sorted(distances.items(), key=lambda x:x[1]))
        for key, value in distances.items():
            if key not in visited: #if the key is not already visited then
                for b, n in graph.items(): # find the key in the graph that is the same as what we are currently selecting in distances
                    if b == key: #if the key in the graph is the same as the key we are currenctly selecting
                        for o, p in n.items(): # for the sub dictionary in n (n is the sub dictionary of the currently selected )
                            if distances[o] > p + value:
                                distances[o] = p + value #if: distances[o] < p + value. then set: distances[o] =p + value
                             

                            #distances[b] = n + #
                        visited.append(b)
                        unvisited.remove(b)
                        break
                break# if we did not break here, then it wouldnt go back to the start of the while loop to sort the distances again.
                     # which we need in order for it to take the lowest vertex first (that hasnt been selected)
    return distances


print(dijkstra(graph))

