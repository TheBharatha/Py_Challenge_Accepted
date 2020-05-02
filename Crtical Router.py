def isConnected(graph):
    trav = set()
    start = None
    for k in graph:
        start = k 
        break
    
    def DFS(node):
        trav.add(node)
        
        for child in graph[node]:
            if child not in trav:
                DFS(child)
        return
    
    DFS(start)
    if len(trav)==len(graph):
        return True
    return False
    
                
def getGraph(nodeNum, edges):
    g = {}
    for n in range(nodeNum):
        g[n] = []
    
    for edg in edges:
        g[edg[0]].append(edg[1])
        g[edg[1]].append(edg[0])
    
    return g

    
    
    
def findCriticalNodes(nodeNum, edges):

    ans = []
    for n in range(nodeNum):
        g = getGraph(nodeNum, edges)
        del g[n]
        for node in g:
            if n in g[node]:
                g[node].remove(n)
     
        if(not isConnected(g)):
            ans.append(n)
        
 
    return ans

print(findCriticalNodes(7, [[0,1], [0, 2], [1, 3], [2, 3], [2, 5], [5, 6], [3,4]]))