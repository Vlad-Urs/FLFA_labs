from lexer import Lexer
from parserator import Parser

NewLexer = Lexer('DSLCode\code.txt')
tokens = NewLexer.regex_tokenize()
print(tokens)

new_parser = Parser(tokens)
new_parser.parse()