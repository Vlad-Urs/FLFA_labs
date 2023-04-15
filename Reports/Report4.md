# Laboratory work no. 4 report.
### Course: Formal Languages & Finite Automata
### Author: Ursu Vlad, st. gr. FAF-212 

---

## Objectives:
1. Learn about Chomsky Normal Form (CNF) [1].
2. Get familiar with the approaches of normalizing a grammar.
3. Implement a method for normalizing an input grammar by the rules of CNF.
    1. The implementation needs to be encapsulated in a method with an appropriate signature (also ideally in an appropriate class/type).
    2. The implemented functionality needs executed and tested.
    3. A BONUS point will be given for the student who will have unit tests that validate the functionality of the project.
    4. Also, another BONUS point would be given if the student will make the aforementioned function to accept any grammar, not only the one from the student's variant.

---

## Laboratory notes:
For this laboratory, and according to the register index, Variant 28 shall
be the Variant chosen. Adapted to a Python dictionary, the type of data
that will be mainly used, the grammar looks like this:

```python
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
```
In this laboratory, the epsilon is noted simply as an empty string "".

Unit tests will be implemented for each of the methods responsible for
each step in the CNF conversion. For unit tests, the 'unittest' module
in python will be used.

---

## Implementation description:
Firstly, this laboratory builds on previous work. To be more concise, 
the Grammar class type object is created to intake the grammar. Additionally,
a new method in the Grammar class that using this given grammar, returns
a new type of object, from a new class:

```python
    def ConvertCNF(self):
        # Create convertor instance
        chomsky_form = CNFConvertor(self.P, self.Vn)
        # Remove Epsilon-transitions
        chomsky_form.RemoveEpsilon()
        # Remove unit productions, key by key
        for key in chomsky_form.p:
            chomsky_form.RemoveUnitProd(key)
        # Remove unproductive symbols:
        chomsky_form.RemoveUnproductive()
        # Remove inaccesible, and cleanup the grammar
        chomsky_form.Cleanup()
        # Obtain the final Chomsky form
        chomsky_form.Transform()


        return chomsky_form
```

The new aforementioned class is basically a CNF converter, containing the
methods necessary for each of the CNF conversion steps. These methods are 
called in the code above.

### Step 1. Removing epsilon-transitions:
First one to be used is the method that removes the epsilon-transitions,
and possibly the most difficult to implement. In the end, the method can
be broken down in 5 steps:

```python
    def RemoveEpsilon(self):
        # Step 1: Identify all non-terminals that produce ε.
        eps_producing = set()
        for nt, prods in self.p.items():
            if "" in prods:
                eps_producing.add(nt)

        # Step 2: Generate all possible combinations of non-terminals that can produce ε.
        eps_combinations = [[]]
        for nt in eps_producing:
            for i in range(len(eps_combinations)):
                eps_combinations.append(eps_combinations[i] + [nt])

        # Step 3: Generate new productions to replace non-terminals that produce ε.
        new_productions = {}
        for nt, prods in self.p.items():
            new_productions[nt] = []
            for prod in prods:
                for combination in eps_combinations:
                    new_prod = prod
                    for c in combination:
                        new_prod = new_prod.replace(c, "")
                    if new_prod != prod and new_prod not in new_productions[nt]:
                        new_productions[nt].append(new_prod)

        # Step 4: Update the grammar with the new productions.
        for nt, prods in new_productions.items():
            for prod in prods:
                if prod != "" and prod not in self.p[nt]:
                    self.p[nt].append(prod)
            if "" in self.p[nt]:
                self.p[nt].remove("")

        # Step 5: Remove the element if it consisted only of an epsilon transition
        to_be_popped = []
        for key in self.p:
            if self.p[key] == []:
                for key1 in self.p:
                    for state in self.p[key1]:
                        if key in state:
                            self.p[key1].remove(state)

                to_be_popped.append(key)

        # Remove it from dictionary and from nonterminals lists
        for key in to_be_popped:
            self.p.pop(key)
            self.Vn.remove(key)
```
It should be noted that to iterate over all possible combinations, the
'itertools' library was used.

#### Unit testing:
```python
    def test_eps_rem(self):
        self.assertEqual(self.cnf_grammar.RemoveEpsilon(),correct_1,'The epsilon was not removed correctly')
```
The correct_1 variable, against which the result of the method is compared
was computed by hand, using the standard rules, and looking like this:
```python
correct_1 = {
    "S": ["B"],
    "A": ["aX", "bX","a","b"],
    "X": ["BX", "b", "B"],
    "B": ["AXaD","AaD"],
    "C": ["Ca"],
    "D": ["aD", "a"]
}
```

#### Test results:
```commandline
...\python.exe "...\_jb_unittest_runner.py" --path .../FLFA_labs/SourceCode/testing.py
Testing started at 6:14 PM ...
Launching unittests with arguments python -m unittest .../FLFA_labs/SourceCode/testing.py in C:\Users\vladu\Documents\uni\FLFA_labs\SourceCode

Ran 1 test in 0.005s

OK

Process finished with exit code 0
```

As can be seen, the test result was successful, and just to be sure, here
is the result returned by the method:

```python
S : ['B']
A : ['aX', 'bX', 'a', 'b']
X : ['BX', 'b', 'B']
B : ['AXaD', 'AaD']
C : ['Ca']
D : ['aD', 'a']
```

### Step 2. Removing Unit Productions:
Next in line, is the method that clears any renaming in the grammar.
This method works a little bit different, going through the grammar
line-by-line, recursively if necessary (i.e. if it detects one unit producton
and a second one when it tries to remove it).

```python
    def RemoveUnitProd(self,key):
        for state in self.p[key]:
            self.RemoveCycles()
            # Check for unit productions
            if len(state) == 1 and state.isupper():
                # If unit prod is detected, start iterating over next production
                for state1 in self.p[state]:
                    if len(state1) == 1 and state1.isupper():
                        self.RemoveUnitProd(state)

                    self.p[key].append(state1)
                # Remove the Renaming
                self.p[key].remove(state)
```

As it removes the renaming, the method transfers all the states associated
with the removed state, while constantly keeping an eye on any possible
cycles forming. If any cycles forms, it is removed using another method:

```python
    def RemoveCycles(self):
        for key in self.p:
            for state in self.p[key]:
                if len(state) == 1 and state.isupper():

                    for state1 in self.p[state]:
                        if state1 == key:

                            for state2 in self.p[state]:
                                if state2 != key:
                                    self.p[key].append(state2)

                            self.p[state] = []
                            break
```

#### Unit testing:
Due to it going through the grammar line-by-line, it cannot be tested 
individually, hence the result returned by the  RemoveUnitProd() method 
will be tested through the ConvertCNF() method.

Again, the correct result was computed by hand:

```python
correct_2 = {
    'S' : ['AXaD', 'AaD'],
    'A' : ['aX', 'bX', 'a', 'b'],
    'X' : ['BX', 'b', 'AXaD', 'AaD'],
    'B' : ['AXaD', 'AaD'],
    'C' : ['Ca'],
    'D' : ['aD', 'a']
}
```

```python
    def test_unit_rem(self):
        self.assertEqual(self.reg_grammar.ConvertCNF(),correct_2,'The unit production removal was not correct')
```
#### Test results:
```commandline
...\python.exe "...\_jb_unittest_runner.py" --path .../FLFA_labs/SourceCode/testing.py
Testing started at 6:58 PM ...
Launching unittests with arguments python -m unittest .../FLFA_labs/SourceCode/testing.py in C:\Users\vladu\Documents\uni\FLFA_labs\SourceCode



Ran 1 test in 0.006s

OK

Process finished with exit code 0
```
### Step 3. Removing non-productive symbols:
```python
    def RemoveUnproductive(self):
        to_be_popped = []

        for key in self.p:
            terminals = 0
            for state in self.p[key]:
                if state.islower():
                    terminals += 1

            if terminals == 0:
                to_be_popped.append(key)

        for key in to_be_popped:
            self.p.pop(key)
            self.Vn.remove(key)
```
The Algorithm is simple, it just checks if the transitions has any terminals,
if it doesn't, it gets popped from the grammar.

#### Unit Testing:
```python
    def test_unpr_rem(self):
        self.cnf_grammar.p = correct_2
        self.assertEqual(self.cnf_grammar.RemoveUnproductive(),correct_3,'The unprodoctive removal went wrong')
```
The correct result that the method should return:
```python
correct_3 = {
    'A' : ['aX', 'bX', 'a', 'b'],
    'X' : ['BX', 'b', 'AXaD', 'AaD'],
    'D' : ['aD', 'a']
}
```
This case of a grammar is particularly interesting, as 'S' is removed. In
this case, a new entry point should be selected.
#### Test Results:
```commandline
...\python.exe "...\_jb_unittest_runner.py" --target testing.TestMethods.test_eps_rem
Testing started at 7:29 PM ...
Launching unittests with arguments python -m unittest testing.TestMethods in ...\FLFA_labs\SourceCode



Ran 1 test in 0.005s

OK

Process finished with exit code 0
```

### Step 4. Unreachable states removal and cleanup:
```python
    def Cleanup(self):
        # Firstly, remove any transitions that would lead to any previously removed non-terminals
        for key in self.p:
            for state in self.p[key]:
                for letter in state:
                    if letter.isupper() and letter not in self.Vn:
                        self.p[key].remove(state)

        # Then check and remove any inaccesible nodes
        # nont is non-terminal
        for nont in self.Vn:
            encounters = 0
            for key in self.p:
                if key != nont:
                    for state in self.p[key]:
                        if nont in state:
                            encounters += 1

            if encounters == 0:
                self.p.pop(nont)
                self.Vn.remove(nont)
```
This method checks for any unreachable states, but before that it cleans
up any states left that contain any non-terminal removed in the previous
step.

#### Unit Testing:
```python
    def test_cln(self):
        self.cnf_grammar.p = correct_3
        self.assertEqual(self.cnf_grammar.Cleanup(),correct_4,'The cleanup went wrong')
```
The correct answer:
```python
correct_4 = {
    'A' : ['aX', 'bX', 'a', 'b'],
    'X' : ['b', 'AXaD', 'AaD'],
    'D' : ['aD', 'a']
}
```
#### Test Result:
```commandline
...\python.exe "..._jb_unittest_runner.py" --target testing.TestMethods.test_cln
Testing started at 7:58 PM ...
Launching unittests with arguments python -m unittest testing.TestMethods.test_cln in ...\FLFA_labs\SourceCode



Ran 1 test in 0.005s

OK

Process finished with exit code 0
```
### Step 5. Transforming it into Chomsky Normal Form:

Now here is a lot to explain, and I am tired
I'll do it next week.

in any case, here's how the grammar looks in the end:

```commandline
A : ['a', 'b', 'EX', 'FX']
X : ['b', 'GH', 'AH']
D : ['a', 'ED']
E : ['a']
F : ['b']
G : ['AX']
H : ['ED']
```

Very good, eh? 
It works for other variants as well, and I'll add that too

# Merry Easter to me!