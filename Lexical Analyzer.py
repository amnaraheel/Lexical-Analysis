import re
def tokenize(expression):
    token_regex = r"""
        (?P<Integer>\d+) |  
        (?P<Addition>\+) |      
        (?P<Subtraction>-) |     
        (?P<Multiplication>\*) | 
        (?P<Division>/) | 
        (?P<Left_Parenthesis>\() |
        (?P<Right_Parenthesis>\)) 
    """
    token_pattern = re.compile(token_regex, re.VERBOSE)
    tokens = []
    for match in token_pattern.finditer(expression):
        token_type = match.lastgroup
        token_value = match.group()
        tokens.append((token_type, token_value))
    return tokens
    
if __name__=="__main__":
    expression=input("Enter a regular Expression (e.g. (3 + 4) * 10): \n")
    n=len(expression)
    for i in range(0,n):
        print(f'{tokenize(expression[i])}')