from rply import LexerGenerator
import re

lg = LexerGenerator()

lg.add("PRINT", r'print')
lg.add('INT', r'int')
lg.add('FLOAT', r'float')
lg.add('PLUS', r'\+')
lg.add('MINUS', r'-')
lg.add('MUL', r'\*')
lg.add('DIV', r'/')
lg.add('OPEN_PARENS', r'\(')
lg.add('CLOSE_PARENS', r'\)')
lg.add('VAR', r'var')
lg.add('IF', r'if')
lg.add('ELSE', r'else')
lg.add('PROGRAM', r'program')
lg.add("ID", r'[a-zA-Z_$][a-zA-Z_0-9]*')
lg.add('COLON', r'\:')
lg.add('LEFTOP', r'\>')
lg.add('RIGHTOP', r'\<')
lg.add('EQUALS', r'\=')
lg.add('SEMICOLON', r'\;')
lg.add("STRING", r"\"([^\"\\]|\\.)*\"")
lg.add('OPEN_CURLY', r'\{')
lg.add('CLOSE_CURLY', r'\}')
lg.add('COMMA', r',')
lg.add("CTE_FLOAT", r'(((0|[1-9][0-9]*)(\.[0-9]*)+)|(\.[0-9]+))([eE][\+\-]?[0-9]*)?')
lg.add('CTE_INT', r'\d+')
lg.ignore('\s+')

lexer = lg.build()


from rply import ParserGenerator

pg = ParserGenerator(
    # A list of all token names, accepted by the parser.
    ['NUMBER', 'OPEN_PARENS', 'CLOSE_PARENS',
     'PLUS', 'MINUS', 'MUL', 'DIV', 'IF', 'ID', 'PROGRAM', 'COLON', 'LEFTOP', 'RIGHTOP',
     'EQUALS', 'SEMICOLON', 'STRING', 'PRINT', 'OPEN_CURLY', 'CLOSE_CURLY', 'ELSE', 'VAR', 'COMMA', 'INT',
     'FLOAT', 'CTE_INT', 'CTE_FLOAT'
    ],
    # A list of precedence rules with ascending precedence, to
    # disambiguate ambiguous production rules.
    precedence=[
        ('left', ['PLUS', 'MINUS']),
        ('left', ['MUL', 'DIV'])
    ]
)

@pg.production('programa : PROGRAM ID SEMICOLON programAux bloque')
def expression_parens(p):
    return Termino()

@pg.production('programAux : vars')
@pg.production('programAux : estatuto')
def expression_parens(p):
    return Termino()

@pg.production('vars : VAR varsAuxA COLON tipo SEMICOLON')
def expression_parens(p):
    return Termino()

@pg.production('varsAuxA : ID varsAuxB')
def expression_parens(p):
    return Termino()

@pg.production('varsAuxB : COMMA varsAuxA')
@pg.production('varsAuxB : none')
def expression_parens(p):
    return Termino()

@pg.production('bloque : OPEN_CURLY estatuto bloqueAux CLOSE_CURLY')
def expression_parens(p):
    return Termino()

@pg.production('bloqueAux : estatuto bloqueAux')
@pg.production('bloqueAux : none')
def expression_parens(p):
    return Termino()

@pg.production('estatuto : escritura')
@pg.production('estatuto : asignacion')
@pg.production('estatuto : condicion')
def expression_parens(p):
    return Termino()

@pg.production('condicion : IF OPEN_PARENS expresion CLOSE_PARENS bloque SEMICOLON')
@pg.production('condicion : IF OPEN_PARENS expresion CLOSE_PARENS bloque ELSE bloque SEMICOLON')
def expression_parens(p):
    return Termino()

@pg.production('escritura : PRINT OPEN_PARENS escrHelperA CLOSE_PARENS SEMICOLON')
def expression_parens(p):
    return Termino()

@pg.production('escrHelperA : expresion escrHelperB')
@pg.production('escrHelperA : STRING escrHelperB')
def expression_parens(p):
    return Termino()

@pg.production('escrHelperB : COMMA escrHelperA')
@pg.production('escrHelperB : none')
def expression_parens(p):
    return Termino()

@pg.production('asignacion : ID EQUALS expresion SEMICOLON')
def expression_parens(p):
    return Termino()

@pg.production('expresion : exp LEFTOP exp')
@pg.production('expresion : exp RIGHTOP exp')
@pg.production('expresion : exp')
def expression_parens(p):
    return Termino()

@pg.production('exp : termino')
@pg.production('exp : termino expHelper')
def expression_parens(p):
    return Termino()

@pg.production('expHelper : PLUS exp')
@pg.production('expHelper : MINUS exp')
@pg.production('expHelper : none')
def expression_parens(p):
    return Termino()

@pg.production('termino : factor')
@pg.production('termino : factor fAux')
def expression_parens(p):
    return Termino()

@pg.production('fAux : MUL termino')
@pg.production('fAux : DIV termino')
@pg.production('fAux : none')
def expression_parens(p):
    return Termino()

@pg.production('factor : OPEN_PARENS expresion CLOSE_PARENS')
@pg.production('factor : PLUS var_cte')
@pg.production('factor : MINUS var_cte')
@pg.production('factor : var_cte')
def expression_parens(p):
    return Factor()

@pg.production('tipo : INT')
@pg.production('tipo : FLOAT')
def expression_number(p):
    return Id()

@pg.production('var_cte : ID')
@pg.production('var_cte : CTE_FLOAT')
@pg.production('var_cte : CTE_INT')
def expression_number(p):
    return Id()

@pg.production("none : ")
def none(p):
    return None


parser = pg.build()
# Var Cte
print(parser.parse(lexer.lex("""
    program main;
    var myVar: int;
    {
        myVar = 2 * 2;
        print(myVar);
        if(myVar > 3){
            myVar = (3.2 + 1) / 7;
        } else {
            myVar = (3 - 1) * 7;
        };
        print("RESULTADO" , myVar, 200);
    }
    """
    )).eval())

print(parser.parse(lexer.lex('program a; print("HOLA MUNDO"); {a = 2 * 2;}')).eval())