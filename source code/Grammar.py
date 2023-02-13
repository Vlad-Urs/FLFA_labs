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
        print(f'used transitions: {self.word_list}')


    def ConvertFA(self):
        initial_states =[]
        for state in self.P['S']:
            initial_states.append(state[0])

        final_states = []
        for key in self.P:
            for state in self.P[key]:
                if state.islower():
                    final_states.append(state)

        transition_functions = []
        for key in self.P:
            for state in self.P[key]:
                aux = []
                aux.append(key)
                aux = aux + list(state)
                transition_functions.append(aux)

        print(f'valid transitions: {transition_functions}')


        automaton = FiniteAutomata(initial_states,
                                   final_states,
                                   self.alphabet,
                                   transition_functions,
                                   self.word_list)
        print('Verdict: ',end='')
        if automaton.checkWord(self.word):
            print('Valid word')
        else:
            print('Invalid word')
