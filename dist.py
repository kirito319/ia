import networkx as nx
import matplotlib.pylab as plt
import numpy as np
import pickle
import math


def loadData():
    # load graph information
    pickle_in = open("Midterm1.pickle","rb")
    data = pickle.load(pickle_in)

    return data[0], data[2]


def initialize(G, pos, start, goal):
    # define start and goal nodes
    color_map = []
    node_size = []
    for node in enumerate(G):
        # start node
        
        if node[1] == start:
        
            color_map.append('green')
            node_size.append(200)
        # end node
        elif node[1] == goal:
            color_map.append('blue')
            node_size.append(200)
        # all others
        else:
            color_map.append('red')
            node_size.append(50)

    # plot graph
    nx.draw_networkx(G, pos=pos, with_labels=False, node_color=color_map, node_size=node_size)
    plt.xticks(np.arange(0, 20))
    plt.yticks(np.arange(0, 20))
    plt.show()
    



def heuristic(start, goal):
    return math.sqrt(math.pow(start[0] - goal[0], 2) + math.pow(start[1] - goal[1], 2))


#returns a list of neighbors that haven't visited
def getNeighbors(start, visited, avoid, g):
    listnei =([n for n in g.neighbors((start))])
    listneighbors = neiVisited(visited, avoid, listnei)
    for node in listneighbors:
        if node[1] > start[1]:
            listneighbors.remove(node)
    return listneighbors


#filters the nodes already visited
def neiVisited(visited, avoid, neighbors):
    for node in visited:
        if node in neighbors:
            neighbors.remove(node)
    for node in avoid:
        if node in neighbors:
            neighbors.remove(node)
    return neighbors


def searchPath(start ,goal , visited, avoid, g):
    s=start
    distance_dic = {}
    distance_h = []
    nei=getNeighbors(s,visited,avoid,g)
    if s == goal:
        visited.append(s)
    elif len(nei) == 1:
        visited.append(s)
        s=nei.pop()
        searchPath(s, goal, visited, avoid, g)
    elif len(nei) > 1:
        for node in nei:
            distance_dic[heuristic(node,goal)] = node
            distance_h.append(heuristic(node,goal))
        visited.append(s)
        s = distance_dic[min(distance_h)]
        searchPath(s, goal, visited, avoid, g)
    else:
        aux_node = visited.pop()
        avoid.append(s)
        s = aux_node
        searchPath(s, goal, visited, avoid, g)

def drawPath(visited)
    for node in visited:
        pass

def main():
    G, pos = loadData()

    
    start_node = (2,19)
    goal_node = (17,0)
    visited = []
    avoid = []
    initialize(G, pos, start_node, goal_node)
    searchPath(start_node,goal_node,visited,avoid,G)
    print(visited)


# when you call the script, it will start here
if __name__ == "__main__":
    main()
