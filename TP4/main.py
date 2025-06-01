import ply.lex as lex

# Lista de tokens
tokens = (
    'SELECT', 'WHERE', 'LIMIT',
    'VAR', 'IDENTIFIER', 'LITERAL', 'NUMBER',
    'LBRACE', 'RBRACE', 'DOT'
)

# Expressões regulares para tokens simples
t_LBRACE = r'\{'
t_RBRACE = r'\}'
t_DOT = r'\.'

def t_SELECT(t):
    r'select'
    return t

def t_WHERE(t):
    r'where'
    return t

def t_LIMIT(t):
    r'LIMIT'
    return t

def t_VAR(t):
    r'\?[a-zA-Z_]\w*'
    return t

def t_IDENTIFIER(t):
    r'[a-zA-Z_][a-zA-Z0-9_:]*'
    return t

def t_LITERAL(t):
    r'".*?"(@[a-zA-Z]+)?'
    return t

def t_NUMBER(t):
    r'\d+'
    t.value = int(t.value)
    return t

# Ignorar espaços e tabs
t_ignore = ' \t'

def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

def t_error(t):
    print(f"Caractere inválido: {t.value[0]}")
    t.lexer.skip(1)


if __name__ == '__main__':
    lexer = lex.lex()
    
    data = """
    select ?nome ?desc where { 
        ?s a dbo:MusicalArtist. 
        ?s foaf:name "Chuck Berry"@en . 
        ?w dbo:artist ?s. 
        ?w foaf:name ?nome. 
        ?w dbo:abstract ?desc 
    } LIMIT 1000
    """
    lexer.input(data)

    for tok in lexer:
        print(tok)