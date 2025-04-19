import re

class ParserLL1:
    def __init__(self, expression):
        self.tokens = re.findall(r'\d+|[()+\-*/]', expression)
        self.pos = 0
    
    def consume(self):
        """Avança para o próximo token."""
        self.pos += 1
    
    def lookahead(self):
        """Retorna o token atual ou None se chegar ao fim."""
        return self.tokens[self.pos] if self.pos < len(self.tokens) else None

    def parse(self):
        """Inicia a análise sintática e calcula o valor da expressão."""
        result = self.expr()
        if self.lookahead() is not None:
            raise SyntaxError("Erro de sintaxe inesperado.")
        return result

    def expr(self):
        """Expr → Term (('+' | '-') Term)*"""
        value = self.term()
        while self.lookahead() in ('+', '-'):
            op = self.lookahead()
            self.consume()
            if op == '+':
                value += self.term()
            elif op == '-':
                value -= self.term()
        return value

    def term(self):
        """Term → Factor (('*' | '/') Factor)*"""
        value = self.factor()
        while self.lookahead() in ('*', '/'):
            op = self.lookahead()
            self.consume()
            if op == '*':
                value *= self.factor()
            elif op == '/':
                value /= self.factor()  # Nota: resultado em float se houver divisão
        return value

    def factor(self):
        """Factor → NUM | '(' Expr ')'"""
        token = self.lookahead()
        if token is None:
            raise SyntaxError("Fator esperado, mas nada foi encontrado.")

        if token.isdigit():  # Se for um número
            self.consume()
            return int(token)
        elif token == '(':
            self.consume()
            value = self.expr()
            if self.lookahead() == ')':
                self.consume()
                return value
            else:
                raise SyntaxError("Parêntese fechado esperado.")
        else:
            raise SyntaxError(f"Token inesperado: {token}")

# Testes
expressoes = [
    "2+3",
    "67-(2+3*4)",
    "(9-2)*(13-4)",
    "10/(2+3)",
    "5+3*2-8/4"
]

for expr in expressoes:
    parser = ParserLL1(expr)
    resultado = parser.parse()
    print(f"{expr} = {resultado}")
