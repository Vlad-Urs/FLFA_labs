class Lexer:
    def __init__(self, file):
        self.f = open(file, 'r')
        self.grammar = {
            'BEGIN': 'keywords',
            'END': 'keywords',
            'INPUT': 'keywords',
            'OUTPUT': 'keywords',
            'RAM': 'keywords',
            'I': 'variables',
            'Q': 'variables',
            'M': 'variables',
            'AND': 'logic gates',
            'OR': 'logic gates',
            'XOR': 'logic gates',
            'NOT': 'logic gates',
            'CN01': 'contacts',
            'CN02': 'contacts',
            'CN03': 'contacts',
            'CN04': 'contacts',
            ':=': 'operators',
            ';': 'separators',
            '.': 'separators'
        }

        self.token_list = []

        self.unorganized_tokens = self.f.read().split()

    def tokenize(self):

        i = -1
        while i < len(self.unorganized_tokens)-1:

            i += 1

            # check if token has a dot somewhere in the middle
            if '.' in self.unorganized_tokens[i] and self.unorganized_tokens[i] != '.':
                pos = self.unorganized_tokens[i].index('.')
                self.unorganized_tokens.insert(i + 1, self.unorganized_tokens[i][:pos])
                self.unorganized_tokens.insert(i + 2, '.')
                if pos != len(self.unorganized_tokens[i])-1:
                    self.unorganized_tokens.insert(i + 3, self.unorganized_tokens[i][pos+1:])
                continue


            # check if there is an endline semicolon
            if ';' in self.unorganized_tokens[i] and self.unorganized_tokens[i] != ';':
                pos = self.unorganized_tokens[i].index(';')
                self.unorganized_tokens.insert(i + 1, self.unorganized_tokens[i][:pos])
                self.unorganized_tokens.insert(i + 2, ';')
                continue


            if self.unorganized_tokens[i] in self.grammar:
                self.token_list.append([self.grammar[self.unorganized_tokens[i]], self.unorganized_tokens[i]])
            elif self.unorganized_tokens[i].isnumeric():
                self.token_list.append(['numeric', self.unorganized_tokens[i]])
            else:
                self.token_list.append(['unknown', self.unorganized_tokens[i]])


        return self.token_list



NewLexer = Lexer('DSLCode\code.txt')
tokens = NewLexer.tokenize()

print(tokens)
