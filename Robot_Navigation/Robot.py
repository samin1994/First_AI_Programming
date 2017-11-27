
class Robot:

    def __init__(self, n, m, matrix):

        self.state = {'x': 0, 'y': 0}
        self.pathCost = 0
        self.bestPath = []
        self.visitedNodes = []
        self.expandedNodes = []
        self.maxMemoryUsed = []
        self.n = n
        self.m = m
        self.matrix = matrix
        self.finalState = [n][m]

    def actions(self, state):
        actions = []
        x = state['x']
        y = state['y']
        right = self.matrix[x][y+1]
        left = self.matrix[x][y-1]
        down = self.matrix[x+1][y]
        up = self.matrix[x-1][y]

        if x <= self.n - 1 and y <= self.m - 1:
            if y != self.m - 1 and right == 1:
                actions.append('Right')
            if y != 0 and left == 1:
                actions.append('Left')
            if x != self.m - 1 and down == 1:
                actions.append('Down')
            if x != 0 and up == 1:
                actions.append('Up')

    def result(self, state, action):

        if action == 'Right':
            state['y'] += 1
        if action == 'Left':
            state['y'] -= 1
        if action == 'Up':
            state['x'] -= 1
        if action == 'Down':
            state['x'] += 1

    def goal_test(self, state):

        if state['x'] == self.m - 1 and state['y'] == self.n - 1:
            return 1
        else:
            return 0

    def path_cost(self, currentcost):
        return currentcost + 1
