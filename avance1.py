import networkx as nx
import matplotlib.pylab as plt
import numpy as np
import pickle


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
    



def heuristic(start, goal , g):
    
    vertical=0 
    hoizontal=0
    regla3=0
    conexionesreales=0
    auxiliar=abs(goal[0] -start [0])
    auxiliar2=abs (goal[1]- start [1])
    auxiliar3=auxiliar + auxiliar2
    print auxiliar3
    for node in enumerate(g):
        if node[1]==node [1]:
            conexionesreales=conexionesreales+1
    
    hoizontal=20*19
    vertical=20 *19
    caminostotal=hoizontal+vertical
    regla3=abs((conexionesreales*auxiliar3)/caminostotal) * 3
    return regla3
    
        
#     h = "your heuristic estimate"
#     return h


def getNeighbors(start,visited,g):
    listnei =([n for n in g.neighbors((start))])
    listneighbors = neiVisited(visited,listnei)
    for node in listneighbors:
        if node[1] > start[1]:
            listneighbors.remove(node)
    print ('los vecinos de ')
    print start
    print ('son')
    print listneighbors
    return listneighbors
    
    #     return "list of neighors"
def neiVisited(visited, neighbors):
    for node in visited:
        if node in neighbors:
            neighbors.remove(node)
    return neighbors

def searchPath(start ,goal , visited, g):
    h= heuristic(start,goal,g)
    s=start
    for r in range (1,h):
        nei=getNeighbors(s,visited,g)
        if s == goal:
            break
        elif s[0] == goal[0]:
            found = False
            for node in nei:
                if node[1] < s[1]:
                    visited.append(s)
                    s = node
                    found = True
                    print('me estoy moviendo a')
                    print(s)
            if len(nei) >= 1:
                if node in  nei:
                    visited.append(s)
                    s = node
                    found = True
                    print('me estoy moviendo a')
                    print(s)
            if found == False:
                aux_node = visited.pop()
                visited.append(s)
                s = aux_node
                print('me estoy moviendo a')
                print(s)
        elif len(nei) >= 2:
            if (nei[0][0]-s[0])>(nei[1][0]-s[0]):
                visited.append(s)
                s=nei[0]
                print ('me estoy moviendo a')
                print nei[0]
            elif (nei[0][0]-s[0])<(nei[1][0]-s[0]):
                visited.append(s)
                s=nei[1]
                print ('me estoy moviendo a')
                print nei[1]
            '''else:
                visited.append(s)
                s=nei[2]
                print ('me estoy moviendo a')
                print nei[2]'''
        elif len(nei) == 1:
            visited.append(s)
            s=nei.pop()
            print('me estoy moviendo a')
            print(s)
            
                
                
    return h
    

    #     return path


# def plotPath(G, path):
#     nx.draw("show the path within the graph")
#     print path


def main():
    G, pos = loadData()

    
    start_node = (2,19)
    goal_node = (17,0)
    visited = []
    initialize(G, pos, start_node, goal_node)

    #getNeighbors(start_node,G)
    searchPath(start_node,goal_node,visited,G)

    
    #searchPath(start_node,goal_node,G)
    ''' you have to develop the rest of the functions '''
    # searchPath()

    # plotPath()



# when you call the script, it will start here
if __name__ == "__main__":
    main()
