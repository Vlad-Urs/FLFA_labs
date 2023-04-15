import unittest
from CNF import CNFConvertor
from Grammar import RegularGrammar

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

correct_1 = {
    "S": ["B"],
    "A": ["aX", "bX","a","b"],
    "X": ["BX", "b", "B"],
    "B": ["AXaD","AaD"],
    "C": ["Ca"],
    "D": ["aD", "a"]
}

correct_2 = {
    'S' : ['AXaD', 'AaD'],
    'A' : ['aX', 'bX', 'a', 'b'],
    'X' : ['BX', 'b', 'AXaD', 'AaD'],
    'B' : ['AXaD', 'AaD'],
    'C' : ['Ca'],
    'D' : ['aD', 'a']
}

correct_3 = {
    'A' : ['aX', 'bX', 'a', 'b'],
    'X' : ['BX', 'b', 'AXaD', 'AaD'],
    'D' : ['aD', 'a']
}

correct_4 = {
    'A' : ['aX', 'bX', 'a', 'b'],
    'X' : ['b', 'AXaD', 'AaD'],
    'D' : ['aD', 'a']
}

class TestMethods(unittest.TestCase):
    def setUp(self):
        self.cnf_grammar = CNFConvertor(p,vn)
        self.reg_grammar = RegularGrammar(vn,vt,p,a)

    #def test_eps_rem(self):
       #self.assertEqual(self.cnf_grammar.RemoveEpsilon(),correct_1,'The epsilon was not removed correctly')

    #def test_unit_rem(self):
        #self.assertEqual(self.reg_grammar.ConvertCNF(),correct_2,'The unit production removal was not correct')

    #def test_unpr_rem(self):
        #self.cnf_grammar.p = correct_2
        #self.assertEqual(self.cnf_grammar.RemoveUnproductive(),correct_3,'The unprodoctive removal went wrong')

    def test_cln(self):
        self.cnf_grammar.p = correct_3
        self.assertEqual(self.cnf_grammar.Cleanup(),correct_3,'The cleanup went wrong')


if __name__ == '__main__':
    unittest.main()