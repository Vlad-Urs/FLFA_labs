from Grammar import RegularGrammar
from finiteAutomata import FiniteAutomata
from CNF import CNFConvertor


# Variant 28
vn = ['S','A','B','C','D','X']
vt = ['a','b']
p = {
    "S": ["B"],
    "A": ["aX", "bX"],
    "X": ["", "BX", "b"],
    "B": ["AXaD"],
    "C": ["Ca"],
    "D": ["aD","a"]

}
a= vt


'''
# Variant 1
vn = ['S','A','B','C', 'D', 'E']
vt = ['a','b']
p = {
    "S": ["aB", "AC"],
    "A": ["a", "ASC", "BC","AD"],
    "B": ["b", "bS", "AC"],
    "C": ["", "BA"],
    "E": ["aB"],
    "D": ["abC"]
}
a= vt
'''

new_grammar = RegularGrammar(vn,vt,p,a)
cnf_form = new_grammar.ConvertCNF()
for key in cnf_form.p:
    print(f'{key} : {cnf_form.p[key]}')
