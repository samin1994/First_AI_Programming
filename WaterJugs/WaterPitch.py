

class WaterPitch:

    def __init__(self):

        state = {'Three': 0, 'Four': 0}
        self.state = state

    def actions(self, state):

        x = state['Three']
        y = state['Four']

        # PourThreeToFour_1 : Empty Three  , PourThreeToFour_2 : Fill Four

        if x == 0 and y == 0:

            return ['FillThree', 'FillFour']

        elif x == 3 and y == 0:
            return ['EmptyThree', 'FillFour', 'PourThreeToFour_1']

        elif x == 0 and y == 4:
            return ['EmptyFour', 'FillThree', 'PourFourToThree_1', 'PourFourToThree_2']

        elif x == 3 and y == 4:
            return ['EmptyThree', 'EmptyFour']

        elif x == 0 and y == 3:
            return ['FillThree', 'FillFour' 'PourFourToThree_1']

        elif x == 3 and y == 1:
            return ['FillFour', 'EmptyFour', 'PourThreeToFour_1']

        elif x == 3 and y == 3:
            return ['EmptyThree', 'EmptyFour', 'PourThreeToFour_1', 'PourThreeToFour_2']

        elif x == 2 and y == 4:
            return ['EmptyThree', 'EmptyFour', 'PourFourToThree_1', 'PourFourToThree_2', 'FillThree']

        elif x == 2 and y == 0:
            return ['EmptyThree', 'PourThreeToFour_1', 'FillFour', 'FillThree']

    def goaltest(self, state):

        if state['Four'] == 2:
            return 1
        else:
            return 0

    def result(self, state, action):

        if action == 'FillThree':
            state['Three'] = 3

        if action == 'FillFour':
            state['Four'] = 3

        if action == 'EmptyThree':
            state['Three'] = 0

        if action == 'EmptyFour':
            state['Four'] = 0

        if action == 'PourThreeToFour_1':
            if state['Four'] == 0:
                state['Four'] = state['Three']
            else:
                state['Four'] = 4
            state['Three'] = 0

        if action == 'PourThreeToFour_2':
            state['Four'] = 4
            state['Three'] -= (4-state['Four'])

        if action == 'PourFourToThree_1':
            state['Four'] = 0
            state['Three'] = 3

        if action == 'PourFourToThree_2':
            state['Three'] = 3
            state['Four'] = 0

        return state

    def pathcost(self, current_cost):
        return current_cost + 1
