from lexer import Lexer
from parser import Parser

def analyzeCode(input):
    lexer = Lexer().get_lexer()
    tokens = lexer.lex(input)

    pg = Parser()
    pg.parse()
    parser = pg.get_parser()
    print(parser.parse(tokens).eval())

def main():
    correct_test = """
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

    ## Missing opening curly brace
    incorrect_test = """
        program main;
        var myVar: int;
        
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
    analyzeCode(correct_test)
    analyzeCode(incorrect_test)


if __name__=='__main__':
     main()# Stack example