from lark import Lark, Transformer, v_args

grammar = """
    programa : PROGRAM ID SEMICOLON progaux bloque
    progaux : vars | estatuto
    vars : VAR varaux COLON tipo SEMICOLON
    varaux : ID COMMA varaux | ID
    bloque : OPEN_CURLY estatuto CLOSE_CURLY
    estatuto : asignacion estatuto
                | escritura estatuto
                | condicion estatuto
                | asignacion | condicion | escritura
    escritura : PRINT OPEN_PARENS help CLOSE_PARENS SEMICOLON
    help : expression COMMA help | STRING COMMA help | expression | STRING
    asignacion : ID EQUALS expression SEMICOLON
    condicion : IF OPEN_PARENS expression CLOSE_PARENS bloque condhelper
    condhelper : SEMICOLON | ELSE bloque SEMICOLON
    expression : exp LEFTOP exp | exp RIGHTOP exp | exp NEQ exp | exp
    exp : termino | termino PLUS exp | termino MINUS exp
    termino : factor | factor MUL termino | factor DIV termino
    factor : PLUS var_cte | MINUS var_cte | var_cte | OPEN_PARENS expression CLOSE_PARENS
    tipo : INT | FLOAT
    var_cte : ID | CTE_FLOAT | CTE_INT | COLON

    MUL : "*"
    PRINT : "print"
    INT : "int"
    FLOAT : "float"
    PLUS : "+"
    MINUS : "-"
    DIV : "/"
    OPEN_PARENS : "("
    CLOSE_PARENS : ")"
    VAR : "var"
    IF : "if"
    ELSE : "else"
    PROGRAM : "program"
    COLON : ":"
    LEFTOP : ">"
    RIGHTOP : "<"
    EQUALS : "="
    SEMICOLON : ";"
    OPEN_CURLY : "{"
    CLOSE_CURLY : "}"
    COMMA : ","
    NEQ : "<>"

    %import common.ESCAPED_STRING   -> STRING
    %import common.SIGNED_INT    -> CTE_INT
    %import common.SIGNED_FLOAT    -> CTE_FLOAT
    %import common.CNAME -> ID
    %import common.LETTER
    %import common.WS_INLINE
    %import common.WS
    %ignore WS
    %ignore WS_INLINE
    %ignore " "
"""
def inputUser():
     archName = input("Enter file name with extension: \n")
     file = open(archName, "r", encoding="utf-8")
     user_input = file.read()
     return user_input

def main():
     code = inputUser()
     calc_parser = Lark(grammar, parser='lalr', start="programa")
     calc = calc_parser.parse
     try:
          if(calc(code)):
               print("Programa Valido")
     except Exception as ex:
          print("Programa Invalido")

if __name__=='__main__':
     main()