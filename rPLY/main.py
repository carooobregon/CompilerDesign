from lexer import Lexer
from parser import Parser

text_input = """
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

lexer = Lexer().get_lexer()
tokens = lexer.lex(text_input)

pg = Parser()
pg.parse()
parser = pg.get_parser()
print(parser.parse(tokens).eval())