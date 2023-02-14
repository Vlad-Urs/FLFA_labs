from Grammar import RegularGrammar
from finiteAutomata import FiniteAutomata

vn = ['S','A','B','C']
vt = ['a','b']
p = {
    'S':['aA'],
    'A':['bS','aB'],
    'B':['bC','aB'],
    'C':['aA','b'],
}
a= vt
'''

vn = ['S','R','L']
vt = ['a','b','c','d','e','f']
p = {
    'S':['aS','bS','cR','dL'],
    'R':['dL','e'],
    'L':['fL','eL','d']
}
a= vt
'''
new_grammar = RegularGrammar(vn,vt,p,a)
new_automaton = new_grammar.ConvertFA()


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