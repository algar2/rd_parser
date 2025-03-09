# CSCI 2320: RD Parser
# Alfonso Garcia
# Grammar Productions for CLite:
# Program —> type main () {Declarations Statements}
# Declarations —> { Declaration }

# Assume string of tokens and lexems are formatted correctly
# Only reading the tokens not the lexemes ...
# if the next token matches what is expected, if not what is expected
# read through whole input then create a list of tokens 
# then advance token pointers!
# Program —> type main ( ) { Declarations Statements }
"""
if current token is type, advance pointer, if current token is main, advance
pointer, if ( ) { do the same, now in DEclarations, call declarations()
"""

# For example: Program 
import sys
token_pointer = 0
tokens = []


def error(msg):
    print(msg)
    exit()


def program_function():

    global token_pointer
    print("In Program")

    if tokens[token_pointer] != 'type':
        error(f"Expected type but got {tokens[token_pointer]} \
              Cannot continue parsing:")
    token_pointer += 1

    if tokens[token_pointer] != 'main':
        error(f"Expected main but got {tokens[token_pointer]}")
    token_pointer += 1

    if tokens[token_pointer] != '(':
        error(f"Expected ( but got {tokens[token_pointer]}")
    token_pointer += 1

    if tokens[token_pointer] != ')':
        error(f"Expected ( but got {tokens[token_pointer]}")
    token_pointer += 1

    if tokens[token_pointer] != '{':
        error(f"Expected ( but got {tokens[token_pointer]}")
    token_pointer += 1

    declarations()
    statements()

    if tokens[token_pointer] != '}':
        print("Cannot continue parsing:")
        error(f"Expected ending brace to finish parsing, but got '{tokens[token_pointer]}'")
    token_pointer += 1
    print("Successfully parsed!")
    return 

    
def declarations():
    global token_pointer
    finished_declaration = False
    while (finished_declaration == False): 
        finished_declaration = declaration()


def declaration():
    global token_pointer
    print("In Declaration")

    if token_pointer >= len(tokens) or tokens[token_pointer] != 'type':
        print("Cannot continue parsing:")
        error(f"Missing 'type'. Expected 'type' but got '{tokens[token_pointer]}'")
    token_pointer += 1

    if token_pointer >= len(tokens) or tokens[token_pointer] != 'id':
        print("Cannot continue parsing:")
        error(f"Expected 'id' but got '{tokens[token_pointer]}'")
    token_pointer += 1

    while (token_pointer < len(tokens) and tokens[token_pointer] == ','):
        token_pointer += 1
        print(tokens[token_pointer])
        if token_pointer >= len(tokens) or tokens[token_pointer] != 'id':
            print("Cannot continue parsing:")
            error(f"Expected 'id' but got '{tokens[token_pointer]}'")
        token_pointer += 1
      
    if tokens[token_pointer] == ';':
        token_pointer += 1
        return True
    else:
        print("Cannot continue parsing:")
        error(f"Expected ; but got '{tokens[token_pointer]}'")
    

def statements():
    global token_pointer
    print("In Statements")
    while (token_pointer < len(tokens)) and tokens[token_pointer] != '}':
        statement()


def statement():
    print("in Statement")
    current_token = tokens[token_pointer]
    if current_token == "{":
        print("In block")
        block()
    elif current_token == "id":
        assignment()
    elif current_token == "print":
        printStmt()
    elif current_token == "if":
        ifStmt()
    elif current_token == "while":
        whileStmt()
    elif current_token == "return":
        returnStmt()
    else:
        print("Cannot continue parsing:")
        error(f"Expected to get a statement but got '{tokens[token_pointer]}'")


def block():
    global token_pointer
    print("In Block")
    if tokens[token_pointer] == '{':
        token_pointer += 1
    statements()
    if tokens[token_pointer] == "}":
        token_pointer += 1
    else:
        print("Cannot continue parsing:")
        error(f"Expected to end with {'}'} but got '{tokens[token_pointer]}'")
    

def printStmt():
    print("In Print")
    global token_pointer
    if token_pointer >= len(tokens) or tokens[token_pointer] != 'print':
         print("Cannot continue parsing:")
         error(f"Expected print but got '{tokens[token_pointer]}'")
    token_pointer += 1
    expression()
    if token_pointer >= len(tokens) or tokens[token_pointer] != ';':
         print("Cannot continue parsing:")
         error(f"Expected ; but got '{tokens[token_pointer]}'")
    token_pointer += 1
    

def ifStmt():
    print("In If statement")
    global token_pointer
    if token_pointer >= len(tokens) or tokens[token_pointer] != 'if':
        print("Cannot continue parsing:")
        error(f"Expected if but got '{tokens[token_pointer]}'")
    token_pointer += 1
    if token_pointer >= len(tokens) or tokens[token_pointer] != '(':
        print("Cannot continue parsing:")
        error(f"Expected ( but got '{tokens[token_pointer]}'")
    token_pointer += 1
    expression()
    if token_pointer >= len(tokens) or tokens[token_pointer] != ')':
        print("Cannot continue parsing:")
        error(f"Expected ) but got '{tokens[token_pointer]}'")
    token_pointer += 1
    statement()
    if tokens[token_pointer] == 'else':
        token_pointer += 1
        statement()
    

def whileStmt():
    print("In While")
    global token_pointer
    if token_pointer >= len(tokens) or tokens[token_pointer] != 'while':
        print("Cannot continue parsing:")
        error(f"Expected if but got '{tokens[token_pointer]}'")
    token_pointer += 1
    if token_pointer >= len(tokens) or tokens[token_pointer] != '(':
        print("Cannot continue parsing:")
        error(f"Expected ( but got '{tokens[token_pointer]}'")
    token_pointer += 1
    expression()
    if token_pointer >= len(tokens) or tokens[token_pointer] != ')':
        print("Cannot continue parsing:")
        error(f"Expected ) but got '{tokens[token_pointer]}'")
    token_pointer += 1
    statement()


def returnStmt():
    print("In Return")
    global token_pointer
    if token_pointer >= len(tokens) or tokens[token_pointer] != 'return':
        print("Cannot continue parsing:")
        error(f"Expected if but got '{tokens[token_pointer]}'")
    token_pointer += 1
    expression()
    if token_pointer >= len(tokens) or tokens[token_pointer] != ';':
        print("Cannot continue parsing:")
        error(f"Expected ) but got '{tokens[token_pointer]}'")
    token_pointer += 1


def assignment():
    global token_pointer
    print("Assignment")
    if token_pointer >= len(tokens) or tokens[token_pointer] != 'id':
        print("Cannot continue parsing:")
        error(f"Expected id but got '{tokens[token_pointer]}'")
    token_pointer += 1

    if token_pointer >= len(tokens) or tokens[token_pointer] != 'assignOp':
        print("Cannot continue parsing:")
        error(f"Expected assignOp but got '{tokens[token_pointer]}'")
    token_pointer += 1
   
    expression()

    if token_pointer >= len(tokens) or tokens[token_pointer] != ';':
        print("Cannot continue parsing:")
        error(f"Expected ; but got '{tokens[token_pointer]}'")
    token_pointer += 1


def conjunction():
    global token_pointer
    print("In Conjunction")
    equality()

    while (token_pointer < len(tokens) and tokens[token_pointer] == "&&"):
        token_pointer += 1
        equality()


def expression():
    global token_pointer
    print("In Expression!")
    conjunction()
    while (token_pointer < len(tokens) and tokens[token_pointer] == "||"):
        token_pointer += 1
        conjunction()


def equality():
    global token_pointer
    print("In Equality")
    relation()
    if tokens[token_pointer] == 'equOp':
        token_pointer += 1
        relation()


def relation():
    global token_pointer
    print("In Relation")
    addition()
    if tokens[token_pointer] == 'relOp':
        token_pointer += 1
        addition()


def addition():
    global token_pointer
    print("In Addition")
    term()
    while (token_pointer < len(tokens) and tokens[token_pointer] == 'addOp'):
        token_pointer += 1
        term()


def term():
    global token_pointer
    print("In Term")
    factor()
    while (token_pointer < len(tokens) and tokens[token_pointer] == 'multOp'):
        token_pointer += 1
        factor()


def factor():
    global token_pointer
    print("In Factor")
    if token_pointer < len(tokens) and (tokens[token_pointer] == "addOp" or \
    tokens[token_pointer] == '!'):
        token_pointer += 1
    else:
        primary()


def primary():
    global token_pointer
    print("In Primary")
    primaries = ['id', 'intLiteral', 'boolLiteral', 'floatLiteral', \
                 'charLiteral']
    if tokens[token_pointer] in primaries:
        token_pointer += 1
        
    else:
        if token_pointer >= len(tokens) or tokens[token_pointer] != '(':
            print("Cannot continue parsing:")
            error(f"Expected ( but got '{tokens[token_pointer]}'")
        token_pointer += 1 

        expression()

        if token_pointer >= len(tokens) or tokens[token_pointer] != ')':
            print("Cannot continue parsing:")
            error(f"Expected ) but got '{tokens[token_pointer]}'")
        token_pointer += 1 
    


def main(input_file_name):
    with open(input_file_name, 'r') as input_file:
        for line in input_file:
            token_and_lex = line.strip().split('\t')
            tokens.append(token_and_lex[0])
        program_function()


if __name__ == "__main__":
    main(sys.argv[1])

