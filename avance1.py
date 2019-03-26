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
    regla3=abs((conexionesreales*auxiliar3)/caminostotal) * 2
    return regla3
    
        
#     h = "your heuristic estimate"
#     return h


def getNeighbors(start,goal,g):
    listnei=[]
    a=np.array((start))
    down=np.array((0,-1))
    m0=a+down
    print m0
    left=np.array((-1,0))
    m1=a+left
    print m1
    right=np.array((1,0))
    m2=a+right
    print m2
    
    for node in enumerate (g):
        
        if node[1] == tuple(m0):
            listnei.append(tuple(m0))
        elif node [1]== tuple (m1):
            listnei.append(tuple(m1))
        elif node [1]== tuple(m2):
            listnei.append(tuple(m2))
            
    print listnei        
    return listnei

    
    
    #     return "list of neighors"


#def searchPath(start ,goal ,g):
   
    
    

    #     return path


# def plotPath(G, path):
#     nx.draw("show the path within the graph")
#     print path


def main():
    G, pos = loadData()
    print G
    
    start_node = (2,19)
    goal_node = (17,0)
    initialize(G, pos, start_node, goal_node)
    getNeighbors(start_node,goal_node,G)
    print(G[(3,19)])
    print(G.neighbors(start_node))
    #searchPath(start_node,goal_node,G)
    ''' you have to develop the rest of the functions '''
    # searchPath()

    # plotPath()



# when you call the script, it will start here
if __name__ == "__main__":
    main()
