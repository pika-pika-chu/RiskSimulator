class Agent():

    def __init__(self, id):
        self.id = id

# dummy luquidator


class Liquidator(Agent):

    def __init__(self, id):
        super().__init__(id)

# dummy borrower


class Borrower(Agent):

    def __init__(self, id, borrowedAmoutMap):
        super().__init__(id)
        self.borrowedAmoutMap = borrowedAmoutMap

# dummy lender


class Lender(Agent):

    def __init__(self, id, LentAmountMap):
        super().__init__(id)
        self.LentAmountMap = LentAmountMap
