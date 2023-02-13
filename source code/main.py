from Grammar import RegularGrammar

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


for i in range(5):
    new_grammar.GenerateWord()
    new_grammar.ConvertFA()
    print()