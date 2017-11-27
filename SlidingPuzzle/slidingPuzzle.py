
class SlidingPuzzle:

    def __init__(self, initial_state):

        self.initial = initial_state
        self.pathCost = [0]
        self.bestPath = []
        self.visitedNodes = []
        self.expandedNodes = []
        self.maxMemoryUsed = []
        self.finalState = []
        self.finalState = {}

    def actions(self, state):

        actions = ['Right', 'Left', 'Up', 'Down']
