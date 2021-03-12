from lark import Lark, Transformer, v_args

grammar = """
    start : estatuto
    estatuto : asignacion | condicion
    asignacion : ID EQUALS expression SEMICOLON
    condicion : IF OPEN_PARENS expression CLOSE_PARENS
    expression : exp LEFTOP exp | exp RIGHTOP exp | exp
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

@v_args(inline=True)    # Affects the signatures of the methods
class CalculateTree(Transformer):
    from operator import add, sub, mul, truediv as div, neg
    number = float

    def __init__(self):
        self.vars = {}

    def assign_var(self, name, value):
        self.vars[name] = value
        return value

    def var(self, name):
        try:
            return self.vars[name]
        except KeyError:
            raise Exception("Variable not found: %s" % name)
def main():
     test()

def test():
     input = 'a = (3 * 8);'
     calc_parser = Lark(grammar, parser='lalr', transformer=CalculateTree())
     calc = calc_parser.parse
    #  parser = Lark(gramatica,start = "programa")
     try:
          print(calc(input))
     except Exception as ex:
          print("parsing failed")
          print (ex)
     # print(parser.parse(test_lilduck1).pretty())
     # print(parser.parse(test_lilduck2).pretty())


if __name__=='__main__':
     main()# Stack example