from .Node import Node
"""
def prims(arr):
        rtnarr = arr
        for i in range (arr.len):
            currentNode = arr[i]
            for j in range (currentNode.connections.len):
"""

def prims(arr):
    tmparr = arr.copy() #copy array to be safe cuz idk how python pointers work
    used = [] #array of names that have been visited already
    returnarr = [] #format: [[name, [connectionname, weight], [connectionname, weight]], [name, [ , ], [ , ]]]
    print(tmparr)
    #root = tmparr[0]
    while len(tmparr) > 0:

        print("Popping at start ", tmparr[0].name)
        used.append(tmparr[0])
        tmparr.pop(0) #pop first element and add name to the visited array
        toadd = []
        highestname = ""

        for i in range(len(used)):
            highest = -1 #lower than it should ever be
            highestname = ""
            cur = used[i]
            for j in range(len(cur.connections)):
                #SEARCH ALL NODES NOT JUST CURRENT
                if cur.getEdgeWeights()[cur.connections[j].name] > highest and not(used.__contains__(cur.connections[j])): # only accept the node if it hasn't been visited
                    print("Found new high",cur.name ,cur.connections[j].name)
                    highestname = cur.connections[j].name
                    highestweight = cur.getEdgeWeights()[cur.connections[j].name]
                    if highestname != "" and highest > -1:
                        toadd = [cur.name, [highestname, highestweight]]
                        inverse = [highestname, [cur.name, highestweight]]
                        print(toadd, highest)

        if toadd != []:
            returnarr.append(toadd)
            returnarr.append(inverse)
        #print(returnarr)

    return returnarr

"""
printarr = []
                for k in range(len(tmparr)):
                    printarr.append(tmparr[k].name)
                print(printarr)
        for j in range(len(tmparr)):
            if len(tmparr) > 0:
                #print(len(tmparr), j)
                if tmparr[j - 1].name == highestname:
                        currentNode = tmparr[j - 1]
                        print("Popping ", tmparr[j-1].name)
                        returnarr.append([tmparr[j-1].name])
                        tmparr.pop(j - 1)
                        break
        """
"""
def prims(arr):
    rtnarr = arr
    for i in range(len(rtnarr)): #first pass: find the shortest path out of the node
        currentNode = rtnarr[i]
        lowest = 1000
        for j in range(len(currentNode.connections)): #search current node's connections for the shortest one
            lowest = min(lowest, currentNode.getEdgeWeights()[currentNode.connections[j].name]) #set lowest to the lowest out of the 2
            print(currentNode.getEdgeWeights()[currentNode.connections[j].name])
            print("min = " , lowest)
        print(currentNode.name, lowest)
    for k in range(len(rtnarr)): #second pass: remove the nodes with longer paths out of the node
        print("REMOVE STEP")
        for l in range(len(currentNode.connections)):
                if currentNode.getEdgeWeights()[currentNode.connections[l].name] > lowest:
                    print("REMOVE")
                    currentNode.deleteConnection(currentNode.connections[l])

    for i in range(len(rtnarr)): #printing/debug
        print(rtnarr[i].name)
        for j in range(len(arr[i].connections)):
            print(rtnarr[i].connections[j].name, rtnarr[i].edgeWeights[arr[i].connections[j].name])
        print("-------------------------")

    return rtnarr


from sys import maxsize

INT_MAX = maxsize
V = 5


# Returns true if edge u-v is a valid edge to be
# include in MST. An edge is valid if one end is
# already included in MST and other is not in MST.
def isValidEdge(u, v, inMST):
    if u == v:
        return False
    if inMST[u] == False and inMST[v] == False:
        return False
    elif inMST[u] == True and inMST[v] == True:
        return False
    return True


def primMST(cost):
    inMST = [False] * V

    # Include first vertex in MST
    inMST[0] = True

    # Keep adding edges while number of included
    # edges does not become V-1.
    edge_count = 0
    mincost = 0
    while edge_count < V - 1:

        # Find minimum weight valid edge.
        minn = INT_MAX
        a = -1
        b = -1
        for i in range(V):
            for j in range(V):
                if cost[i][j] < minn:
                    if isValidEdge(i, j, inMST):
                        minn = cost[i][j]
                        a = i
                        b = j

        if a != -1 and b != -1:
            print("Edge %d: (%d, %d) cost: %d" %
                  (edge_count, a, b, minn))
            edge_count += 1
            mincost += minn
            inMST[b] = inMST[a] = True

    print("Minimum cost = %d" % mincost)



def primss(arr):
    remaining = arr
    currentNode = arr[0]
    newGraph = currentNode
    for i in range(remaining.len):
        lowest = 1000
        for i in range(currentNode.connections.len):
            if currentNode.getEdgeWeights()[currentNode.connections[i].name] < lowest and currentNode.connections[i] in remaining:
                lowestnode = currentNode.connections[i]
            currentNode.addNode(lowestnode, currentNode.getEdgeWeights()[lowestnode.name])
            currentNode = lowestnode
            remaining.remove(lowestnode)
            
    return newGraph
"""
"""
def prims(arr):
    v = arr.len
    adj = []
    for i in range(v):
        adj.append([])
        for j in range(v):
            adj[i] = -1
       
    inMST = []
    i = 0
    while(inMST.len != arr.len):
        currentNode = arr[i]
       """



"""
create empty array
find a node
find shortest way out that isnt in the visited array
add way out into array

"""
"""
import sys
from collections import defaultdict
def Prims(everyPerson):
    adj = []  # 2d array
    # selectedCol = 0 #where to start with the adjacency matrix stuff
    # largestEdgeNum = 0
    for i in range(len(everyPerson)):
        row = []
        for j in range(len(everyPerson)):
            row.append(0)
            if everyPerson[i].getEdgeWeights().__contains__(everyPerson[j].name):  # i has connection with j
                row[j] = everyPerson[i].getEdgeWeights()[everyPerson[j].name]
                # if everyPerson[i].getEdgeWeights()[everyPerson[j].name] > largestEdgeNum:
                # largestEdgeNum = everyPerson[i].getEdgeWeights()[everyPerson[j].name]
                # selectedCol = i
            else:
                row[j] = -1
            if j != len(everyPerson) - 1:
                print(row[j], end=" ")
            else:
                print(row[j])

        adj.append(row)
"""