from lark import Lark

grammar = """
     programa : PROGRAMA ID COLN vars bloque
               |PROGRAMA ID COLN bloque
     vars : VAR ID PTO COLN tipo
               | VAR ID COLN tipo
     tipo : NUMBER 
     bloque : LKEY estatuto RKEY
     estatuto : asignacion | condicion | escritura
     asignacion : ID EQ expresion PTOCOM
     escritura : PRINT LPARENS expresion | STRING RPARENS PTOCOM
               | PRINT LPARENS expresion | STRING COMM LBR expresion | STRING RBR RPARENS PTOCOM
     expresion : exp MOTHN exp | exp LETHN exp | exp NEQ exp 
     condicion : IF LPARENS  expresion RPARENS bloque ELSE bloque PTOCOM
               | IF LPARENS  expresion RPARENS bloque PTOCOM
     exp : termino | SUM | SUB | exp
     termino : factor | MUL | DIV | termino
     factor : LPARENS expresion RPARENS | SUM | SUB | constante | SUM constante | SUB constante
     constante : ID | NUMBER
     
     PROGRAMA :"program"
     ID : "id"
     IF : "if"
     ELSE : "else"
     VAR : "var"
     PRINT : "print"
     LPARENS : "("
     RPARENS : ")"
     LKEY : "{"
     RKEY : "}"
     LBR : "["
     RBR : "]"
     SUM : "+"
     SUB : "-"
     MUL : "*"
     DIV : "/"
     EQ : "="
     COLN:":"
     COMM: ","
     PTO: "."
     PTOCOM: ";"
     MOTHN : ">"
     LETHN : "<"
     NEQ : "<>"


     %import common.ESCAPED_STRING   -> STRING
     %import common.SIGNED_NUMBER    -> NUMBER
     %import common.CNAME -> NAME
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
     test_lilduck1 ="""
     if(3 > 4)
          return true   
     """

     test_lilduck2 = """
     if(3 > 4){
          return true; 
     };
     """
     parsen = Lark(gramatica,parser='earley',start ="programa", ambiguity='explicit')
     parser = Lark(gramatica,start = "programa")
     try:
          print(parsen.parse("program id : var"))
     except Exception as ex:
          print("parsing failed")
          print (ex)
     # print(parser.parse(test_lilduck1).pretty())
     # print(parser.parse(test_lilduck2).pretty())

if __name__ == '_main_':
     main()