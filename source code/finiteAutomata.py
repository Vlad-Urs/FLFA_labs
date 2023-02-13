class FiniteAutomata:
    def __init__(self,q0,F,sigma,delta,Q):
        self.q0 = q0
        self.F = F
        self.sigma = sigma
        self.delta = delta
        self.Q = Q

    def checkWord(self,word):
        if word[0] not in self.q0:
            return False

        if word[-1] not in self.F:
            return  False

        for letter in word:
            if letter not in self.sigma:
                return False

        for transition in self.Q:
            if transition not in self.delta:
                return False

        return True
