

def dfs_tree_search(problem, frontier):
    frontier.append(Node(problem.initial))
    while frontier:

        node = frontier.pop()

        if problem.goaltest(node.state):
            problem.bestPath = node.solution()
            problem.pathCost = node.pathcost
            return node

        problem.expandedNodes += 1
        for child in node.expand(problem):
            problem.visitedNodes += 1

            frontier.extend([child])
            problem.maxMemoryUsed = max(problem.maxMemoryUsed, frontier.size())

    return None

