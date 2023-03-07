from Grammar import RegularGrammar
from finiteAutomata import FiniteAutomata


'''
---Lab 1 stuff---
for i in range(5):
    word = new_grammar.GenerateWord()
    if new_automaton.checkWord(word):
        print('Valid word')
    print()

user_word = 'abbbbaaaabbb'
if new_automaton.checkWord(user_word):
    print('user word is valid')
else:
    print('user word not valid')

# Lab2 stuff
vn = ['S','A','B','C']
vt = ['a','b']
p = {
    'S':['aA'],
    'A':['bSs','aB'],
    'B':['bC','aBB'],
    'C':['aA','b'],
}
a= vt

new_grammar = RegularGrammar(vn,vt,p,a)
#new_automaton = new_grammar.ConvertFA()
#new_new_grammar = new_automaton.convertGrammar()

for key in new_grammar.P:
    print(f'{key} -> {new_grammar.P[key]}')
print('grammar type')
print(new_grammar.chumsky_type())
#print(new_new_grammar.P)
#print(new_automaton.automatonType())


Variant 28
Q = {q0,q1,q2,q3},
∑ = {a,b,c},
F = {q3},
δ(q0,a) = q0,
δ(q0,a) = q1,
δ(q1,a) = q1,
δ(q1,c) = q2,
δ(q1,b) = q3,
δ(q0,b) = q2,
δ(q2,b) = q3.

unfortunately I will have to modify a bit this form, to acomodate my madness, but it essentially works as intended,
I swear to God 

q0 ~ S
q1 ~ A
q2 ~ B
q3 ~ C
'''
Q = ['S','A','B','C']
q0 = 'S'
F = 'C'
sigma = ['a','b','c']
delta =[
    ['S','a','S'],
    ['S','a','A'],
    ['A','a','A'],
    ['A','c','B'],
    ['A','b','C'],
    ['S','b','B'],
    ['B','b','C']
]

new_new_automaton = FiniteAutomata(q0,F,sigma,delta,Q)
new_dfa = new_new_automaton.nfa_to_dfa()
print(f'Q = {new_dfa.Q}')
print(f'start state: {new_dfa.q0}')
print(f'final states: {new_dfa.F}')
print(f'sigma: {new_dfa.sigma}')
print('delta:')
for row in new_dfa.delta:
   print(row)

new_new_automaton.display()

#for transition in new_new_automaton.delta:
#    print(transition)
#print(f'automaton type: {new_new_automaton.automatonType()}')

#generated_grammar = new_new_automaton.convertGrammar()

#for key in generated_grammar.P:
#    print(f'{key} -> {generated_grammar.P[key]}')

#new_dfa_automaton = new_new_automaton.nfa_to_dfa()
#dfa_grammar = new_dfa_automaton.convertGrammar()

#print(new_dfa_automaton.delta)
#print(dfa_grammar.P)

