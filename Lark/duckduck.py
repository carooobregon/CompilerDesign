from lark import Lark, Transformer, v_args

grammar = """
    start : programa 
    programa : PROGRAM ID SEMICOLON progaux bloque
    progaux : vars | estatuto
    vars : VAR ID COLON tipo SEMICOLON
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

def main():
     test()
     
def test():
    #  input = '{print("hola"); ab = 3*2; if(2 > 2){ ab = 2*2; }else{print(2);}; print("hola");}'
     correct_input = """
          program ab;
          var ab : int;
          {
               print("hola");
               ab = 3 * 2 + 1 * (2 + 2);
               if(2 > 2){
                    ab = 2*2;
               } else {
                    print(2);
               };
               print("hola", ab, 2 * 2, 1);
          }
     """
     incorrect_input = """
          program ab;
          var ab : int;
          
               print("hola");
               ab = 3 * 2 + 1 * (2 + 2);
               if(2 > 2){
                    ab = 2*2;
               } else {
                    print(2);
               };
               print("hola", ab, 2 * 2, 1);
          }
     """
     calc_parser = Lark(grammar, parser='lalr')
     calc = calc_parser.parse
    #  parser = Lark(gramatica,start = "programa")
     try:
          if(calc(correct_input)):
               print("Programa Valido")
     except Exception as ex:
          print("parsing failed")
     # print(parser.parse(test_lilduck1).pretty())
     # print(parser.parse(test_lilduck2).pretty())


if __name__=='__main__':
     main()# Stack example