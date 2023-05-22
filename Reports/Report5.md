# Laboratory work no. 5 report.
### Course: Formal Languages & Finite Automata
### Author: Ursu Vlad, st. gr. FAF-212 

---

## Objectives:
1. Get familiar with parsing, what it is and how it can be programmed [1].
2. Get familiar with the concept of AST [2].
3. In addition to what has been done in the 3rd lab work do the following:
   1. In case you didn't have a type that denotes the possible types of tokens you need to:
      1. Have a type __*TokenType*__ (like an enum) that can be used in the lexical analysis to categorize the tokens. 
      2. Please use regular expressions to identify the type of the token.
   2. Implement the necessary data structures for an AST that could be used for the text you have processed in the 3rd lab work.
   3. Implement a simple parser program that could extract the syntactic information from the input text.

---

## Implementation description:
First of all, the categorization of tokens.

Although in the laboratory work 3 this functionality was already included,
it was not however based on regular expressions.
In this laboratory a new method is added to the Lexer class, 'regex_tokenize'
that will use the 're' library in python to categorize the tokens by help of
regular expressions.
```python
 def regex_tokenize(self):
        for token in self.unorganized_tokens:
            category = self.categorize_token(token)
            self.token_list.append([category, token])

        return self.token_list

    def categorize_token(self, token):
        for pattern, category in self.grammar.items():
            if token.isnumeric():
                return 'numeric'

            if re.match(pattern, token):
                return category
```
The result of this new tokenizer is the same as last time:
```python
[['keywords', 'INPUT'], ['variables', 'I'], ['numeric', '011'], ['separators', '.'], ['variables', 'Q'], 
 ['numeric', '011'], ['separators', ';'], ['keywords', 'OUTPUT'], ['variables', 'Q'], ['numeric', '011'], 
 ['separators', '.'], ['variables', 'M'], ['numeric', '011'], ['separators', ';'], ['keywords', 'RAM'], 
 ['contacts', 'CN01'], ['logic gates', 'AND'], ['variables', 'I'], ['numeric', '011'], ['separators', '.'], 
 ['variables', 'Q'], ['numeric', '011'], ['separators', '.'], ['contacts', 'CN04'], ['separators', '.'], 
 ['logic gates', 'NOT'], ['variables', 'Q'], ['numeric', '011'], ['separators', '.'], ['variables', 'I'], 
 ['numeric', '011'], ['separators', ';'], ['keywords', 'BEGIN'], ['variables', 'I'], ['numeric', '011'], 
 ['operators', ':='], ['logic gates', 'NOT'], ['variables', 'I'], ['numeric', '011'], ['keywords', 'END']]
```

Moving to the abstract syntax tree, it was constructed in python using 
graphs and the 'nx' and 'matplotlib' libraries.

The whole method is in the Parser class, and the result looks like this:

![screenshot](images/lab5_1.PNG)

And a bit more zoomed in:

![screenshot](images/lab5_2.PNG)

Finally moving on to the last point, the parser.

The Parser class is a simple parser that processes a list of tokens 
according to a specific grammar. It is responsible for syntactic analysis 
and ensures that the input tokens adhere to the expected structure.

The class has the following methods:

- __init__(self, tokens): Initializes the Parser object with the input 
tokens.
-parse(self): Initiates the parsing process by calling the parse_program() method.

- advance(self): Moves to the next token in the token list.
- match(self, expected_type): Checks if the current token matches the expected type. If it does, advances to the next token; otherwise, raises a SyntaxError.
-parse_program(self): Parses the entire program by calling various section parsing methods and ensuring the presence of the "BEGIN" and "END" keywords.
- parse_input_section(self): Parses the input section of the program, which consists of variable declarations followed by a semicolon.
- parse_output_section(self): Parses the output section of the program, which also consists of variable declarations followed by a semicolon.
- parse_ram_section(self): Parses the RAM section of the program, which consists of contact, logic gate, variable, and numeric tokens.
- parse_assignment(self): Parses an assignment statement, which consists of a variable, numeric value, assignment operator, logic gate, variable, and numeric value.
- The Parser class ensures that the tokens are processed in the correct order and follows the defined grammar rules. If any token is encountered that doesn't match the expected type, a SyntaxError is raised.

Given the program:
```commandline
INPUT
I 011. Q 011;
OUTPUT
Q 011. M 011;
RAM
CN01 AND I 011. Q 011 . CN04.NOT Q 011. I 011;
BEGIN
I 011 := NOT I 011
END
```

The parser works without raising any error.

To test it, something as simple as removing the first semicolon can be 
done:
```commandline
INPUT
I 011. Q 011
```

The parser raises the following error:
```commandline
SyntaxError: Expected token of type 'separators', but found 'keywords'
```