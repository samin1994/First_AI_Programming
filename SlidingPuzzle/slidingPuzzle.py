from AI_Search.WaterJugs.Utils import find


class SlidingPuzzle:

    def __init__(self, initial_state):

        self.initial = initial_state
        self.pathCost = [0]
        self.bestPath = []
        self.visitedNodes = []
        self.expandedNodes = []
        self.maxMemoryUsed = []
        self.finalState = [][3]

    def actions(self, state):

        actions = ['Right', 'Left', 'Up', 'Down']

        if find(state, 0)['x'] == 0:
            actions.remove('Up')
            if find(state, 0)['y'] == 0:
                actions.remove('Left')
            if find(state, 0)['y'] == 2:
                actions.remove('Right')

        elif find(state, 0)['x'] == 2:
            actions.remove('Down')
            if find(state, 0)['y'] == 0:
                actions.remove('Left')
            if find(state, 0)['y'] == 2:
                actions.remove('Right')

        elif find(state, 0)['x'] == 1:
            if find(state, 0)['y'] == 0:
                actions.remove('Left')

            if find(state, 0)['y'] == 2:
                actions.remove('Right')

        return actions

    def result(self, state, action):

        x = find(state, 0)['x']
        y = find(state, 0)['y']

        if action == 'Right':
            state[x][y] = state[x][y+1]
            state[x][y+1] = 0

        if action == 'Left':
            state[x][y] = state[x][y-1]
            state[x][y-1] = 0

        if action == 'Up':
            state[x][y] = state[x-1][y]
            state[x-1][y] = 0

        if action == 'Down':
            state[x][y] = state[x+1][y]
            state[x+1][y] = 0

    def goal_test(self, state):

        count = 0
        goal_state = [[0, 1, 2], [3, 4, 5], [6, 7, 8]]

        for i in [0, 3]:
            for j in [0, 3]:
                if state[i][j] == goal_state:
                    count += 1

        if count == 9:
            return 1
        else:
            return 0

    def pathcost(self, currentcost):
        pass


    def final_result(self):

        return [self.visitedNodes] + [self.expandedNodes] + [self.bestPath] + [self.pathCost] + [self.maxMemoryUsed] + [self.finalState]