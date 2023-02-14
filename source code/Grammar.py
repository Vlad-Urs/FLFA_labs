import random

from finiteAutomata import FiniteAutomata

class RegularGrammar:
    def __init__(self,Vn,Vt,P,a):
        self.Vn = Vn
        self.Vt = Vt
        self.P = P
        self.alphabet = a
        self.word_list = []
        self.word = ''

    def GenerateWord(self):
        self.word_list = []
        self.word='S'
        self.word_list.append(self.word)
        while self.word[-1].isupper():
            aux = []
            aux.append(self.word[-1])
            self.word = self.word[:-1]+random.choice(self.P[self.word[-1]])
            if self.word[-1].isupper():
                aux.append(self.word[-2])
                aux.append(self.word[-1])
            else:
                aux.append(self.word[-1])
            self.word_list.append(aux)
        self.word_list=self.word_list[1:]
        print(f'generated word: {self.word}')
        print(f'used transitions for created word: {self.word_list}')
        return self.word


    def ConvertFA(self):
        initial_states =[]
        for state in self.P['S']:
            initial_states.append(state[0])

        transition_functions = []
        for key in self.P:
            for state in self.P[key]:
                aux = []
                aux.append(key)
                aux = aux + list(state)
                transition_functions.append(aux)

        print(f'valid transitions: {transition_functions}')


        automaton = FiniteAutomata(initial_states,
                                   self.Vt,
                                   self.alphabet,
                                   transition_functions,
                                   self.Vn)
        return automaton

    def chumsky_type(self):

        def upper_number(state):
            uppers = 0
            for letter in state:
                if letter.isupper():
                    uppers += 1
            return uppers

        def upper_pos(state):
            pos = 0
            for i in range(0, len(state)):
                if state[i].isupper():
                    pos=i
            if pos == len(state)-1:
                return -1
            return pos


        chum_type = 3
        for key in self.P:
            if len(key)>=2:
                chum_type = 1
            for state in self.P[key]:
                if state == '' and chum_type == 1:
                    return 0

        if chum_type==1:
            return 1

        for key in self.P:
            for state in self.P[key]:
                if upper_number(state)>1:
                    return 2
                elif upper_number(state)==1:
                    location = upper_pos(state)

        for key in self.P:
            if upper_number(self.P[key][0])>1:
                return 2
            if upper_pos(self.P[key][0]) not in [0,-1]:
                return 2
            for i in range(1,len(self.P[key])):
                if not self.P[key][i].islower() and self.P[key][i] != '':
                    if upper_number(self.P[key][i])>1:
                        return 2
                    if upper_pos(self.P[key][i]) != upper_pos(self.P[key][i-1]):
                        return 2
        return chum_type




