from package.Node import Node
from package.excelimporter import get_names
from package.Prims import prims
from package.group import findGroups
import numpy as np
#from package.group import group
#from package.abc import get_names

import networkx as nx
import matplotlib.pyplot as plt

def setAll(everyPerson): #sets the Node connections and removes connections that people don't want.
    for i in range(len(everyPerson)):
        everyPerson[i].setConnections(everyPerson, i)
    for i in range(len(everyPerson)):
        everyPerson[i].initializeEdgeWeights(everyPerson)
    for i in range(len(everyPerson)):
        everyPerson[i].addToEdgeWeights(everyPerson)
    for i in range(len(everyPerson)):
        everyPerson[i].removeDirectionalConnections()

def getGroups(everyPerson):
    return findGroups(everyPerson)
    #return prims(everyPerson)

def createGraph(everyPerson):
    graph = nx.Graph()
    for i in range(len(everyPerson)):  # add all people as nodes to graph
        graph.add_node(everyPerson[i].name)

    for i in range(len(everyPerson)):  # go through all i nodes
        for j in range(len(everyPerson)):  # for each i node, go through all j other nodes to check for connections
            if everyPerson[i].getEdgeWeights().__contains__(
                    everyPerson[j].name):  # if the dictionary of edges has an edge bw everyperson[i] and [j]
                graph.add_edge(everyPerson[i].name, everyPerson[j].name,
                               weight=everyPerson[i].getEdgeWeights()[everyPerson[j].name])

    return graph

def plotGraph(graph, distEdges, name):

    pos = nx.spring_layout(graph, k=distEdges)  # positions for all nodes

    nx.draw_networkx_nodes(graph, pos, node_size=700) # nodes
    nx.draw_networkx_edges(graph, pos, edgelist=graph.edges, width=2) # edges
    nx.draw_networkx_labels(graph, pos, font_color="red", font_size=7, font_family='sans-serif')
    labels = nx.get_edge_attributes(graph, 'weight')
    nx.draw_networkx_edge_labels(graph, pos, edge_labels=labels, font_color=(0, 0.5, 0.2), font_size=10, font_family='sans-serif')

    plt.suptitle(name)
    plt.axis('off')
    plt.show()

def main():
    allNames = get_names('../Test Random.xlsx')
    everyPerson = []
    for i in range(len(allNames)):
        everyPerson.append(Node(allNames[i][1], allNames[i][2], allNames[i][0]))

    tempList = get_names('../Test Random.xlsx')
    everyPerson = []
    onlyConnections = []
    onlyConnectionsCopy = []

    for i in tempList:
        everyPerson.append(Node(i[1], i[2], i[0]))
        if i[1][0] != "None" or i[1][1] != "None" or i[1][2] != "None":
            onlyConnections.append(Node(i[1], i[2], i[0]))
            onlyConnectionsCopy.append(Node(i[1], i[2], i[0]))

    for i in range(len(everyPerson)): #There is a "None None" person in everyperson, remove it.
        if everyPerson[i].name == "None None":
            everyPerson.remove(everyPerson[i])

    setAll(everyPerson)
    setAll(onlyConnections)


    for i in range(len(onlyConnectionsCopy)):
        onlyConnectionsCopy[i].setConnectionsNoZeroes(onlyConnectionsCopy, i)
    for i in range(len(onlyConnectionsCopy)):
        onlyConnectionsCopy[i].addToEdgeWeights(onlyConnectionsCopy)
    for i in range(len(onlyConnectionsCopy)):
        onlyConnectionsCopy[i].removeDirectionalConnections()

    #graphEveryone = createGraph(everyPerson)
    #plotGraph(graphEveryone, 3.5*1/np.sqrt(len(graphEveryone.nodes())), "Graph of everyone")

    groupedPeopleTEST = getGroups(everyPerson)
    graph2Cxns = createGraph(groupedPeopleTEST)
    plotGraph(graph2Cxns, None, "Connections found in graph of everyone")

    groupedPeople = getGroups(onlyConnections)
    graph2 = createGraph(groupedPeople)
    plotGraph(graph2, 3*1/np.sqrt(len(graph2.nodes())), "Connections found in graph of only people with preferences")

    graphOnlyCxnsNoZeroes = createGraph(onlyConnectionsCopy)
    plotGraph(graphOnlyCxnsNoZeroes, 3 * 1 / np.sqrt(len(graphOnlyCxnsNoZeroes.nodes())),
              "Graph of only people with preferences and no zeroes")

if __name__ == "__main__":
    main()
