from Grammar import RegularGrammar
from finiteAutomata import FiniteAutomata
from CNF import CNFConvertor

'''
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
a = vt


'''
# Variant 4
p = {
'S' : ['bA', 'A', 'aB'],
'A' : ['B', 'bBAB', 'b', 'AS'],
'B' : ['bS', 'aD', '', 'b'],
'D' : ['AA'],
'C' : ['Ba']
}
vn = ['S', 'A', 'B', 'C', 'D']
vt = ['a', 'b']
a= vt


new_grammar = RegularGrammar(vn,vt,p,a)
cnf_form = new_grammar.ConvertCNF()
for key in cnf_form.p:
    print(f'{key} : {cnf_form.p[key]}')
