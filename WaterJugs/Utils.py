from collections import deque

# ______________________________________________________________________________
# Code to model queue


class Queue:
    def __init__(self):
        raise NotImplementedError

    def extend(self, items):
        for item in items:
            self.append(item)


class FIFOQueue(Queue):

    def __init__(self):
        self.Q = deque()

    def append(self, item):
        self.Q.appendleft(item)

    def extend(self, items):
        self.Q.extendleft(items)

    def pop(self):
        return self.Q.pop()

    def size(self):
        return len(self.Q)

    def __contains__(self, item):
        return item in self.Q

    def __len__(self):
        return len(self.Q)


class LIFOQueue(Queue):

    def __init__(self):
        self.Q = deque()

    def append(self, item):
        self.Q.append(item)

    def extend(self, items):
        self.Q.extend(items)

    def pop(self):
        return self.Q.pop()

    def size(self):
        return len(self.Q)

    def __contains__(self, item):
        return item in self.Q

    def __len__(self):
        return len(self.Q)


class PriorityQueue(Queue):
    def __init__(self, order=min, f=lambda x: x):
        self.A = []
        self.order = order
        self.f = f

    def append(self, item):
        bisect.insort(self.A, (self.f(item), item))

    def __len__(self):
        return len(self.A)

    def pop(self):
        if self.order == min:
            return self.A.pop(0)[1]
        else:
            return self.A.pop()[1]

    def size(self):
        return len(self.A)

    def __contains__(self, item):
        return any(item == pair[1] for pair in self.A)

    def __getitem__(self, key):
        for _, item in self.A:
            if item == key:
                return item

    def __delitem__(self, key):
        for i, (value, item) in enumerate(self.A):
            if item == key:
                self.A.pop(i)


# ______________________________________________________________________________
# Code to model a graph

class Node:

    def __init__(self, state, parent=None, action=None, path_cost=0):
        self.state = state
        self.parent = parent
        self.action = action
        self.path_cost = path_cost
        self.depth = 0
        if parent:
            self.depth = parent.depth + 1

    def __repr__(self):
        return "<Node {}>".format(self.state)

    def __lt__(self, node):
        return self.state < node.state

    def expand(self, problem):
        childs = []
        for action in problem.actions(self.state):
            childs.append(self.child_node(problem, action))

        return childs

    def child_node(self, problem, action):
        next = problem.result(self.state, action)
        node = Node(next, self, action, problem.path_cost(self.path_cost, self.state, action, next))
        return node

    def solution(self):
        solution = []
        for node in self.path()[1:]:
            solution.append(node.action)

        return solution

    def path(self):
        node, path_back = self, []
        while node:
            path_back.append(node)
            node = node.parent
        return list(reversed(path_back))

    def __eq__(self, other):
        return isinstance(other, Node) and self.state == other.state

    def __hash__(self):
        return hash(self.state)

class Graph:

    def __init__(self, dict=None):
        self.dict = dict or {}
        for a in list(self.dict.keys()):
            for (b, distance) in self.dict[a].items():
                self.dict.setdefault(b, {})[a] = distance

    def get(self, a, b=None):
        self.dict.setdefault(a, {})
        links = self.dict[a]
        if b is None:
            return links
        else:
            return links.get(b)

    def nodes(self):
        return list(self.dict.keys())


def DO_SEARCH(problem, searchers):

    result = []
    for searcher in searchers:
        p = problem
        searcher(problem)

        row = [name(searcher)] + problem.final_result()
        result.append(row)

    return result