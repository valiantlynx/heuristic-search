#heritic search. Astar searching algorithm 
nodesToSearch = [start] 
searchedNodes = []  

while nodesToSearch:
    currentNode = nodesToSearch.pop(0)
    if currentNode not in searchedNodes:
        searchedNodes.append(currentNode)
        for child in range(len(nodesToSearch)):
            if nodesToSearch[child] < currentNode:
                nodesToSearch.insert(child, currentNode)
                break
            if nodesToSearch[child] > currentNode[-1]:
                nodesToSearch.append(child)
                break