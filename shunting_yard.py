operateur = ("+","-","/","*","^","(",")")
num = ("0","1","2","3","4","5","6","7","8","9", ".")
def tokenize(expression: str) -> list[str]:
    try:
        token = list(expression.replace(" ", ""))
        for element in token:
            if(element not in operateur and element not in num):
                raise Exception("Expression invalide")
        token.append("!")
        i = 0
        while(token[i] != "!"):
            if(token[i] == "-"):
                if(i == 0 or token[i-1] in operateur and token[i-1] != ")"):   
                      while(token[i+1] in num):
                        token[i] = token[i] + token.pop(i+1)
                else:
                    while(token[i+1] in num):
                        token[i] = token[i] + token.pop(i+1)
            if(token[i] in num):
                if(i+1 <= len(token)-1):
                    while(token[i+1] in num):
                        token[i] = token[i] + token.pop(i+1)
            if(token[i] in operateur):
                pass
            i += 1
        for i in range(len(token)):
            if(token[i].count(".") > 1):
                raise Exception("Expression invalide")
            if(token[i].startswith(".")):
                token[i] = "0" + token[i]
            if(token[i].endswith(".")):
                token[i] = token[i] + "0"
        token.remove("!")
    except Exception as e:
        print(e)
    return token

"""def infix_to_postfix(tokens: list[str]) -> list[str]:
    infix = tokenize(tokens)
    postfix = []
    listop = []
    valeur = []
    print(infix)
    for i in range(len(infix)):
        try:
            if(infix[i] in operateur):
                listop.append(infix[i])
                match infix[i]:
                    case "+", "-":
                        valeur.append(0)
                    case "/", "*":
                        valeur.append(1)
                    case "^":
                        valeur.append(2)
                    case "(" , ")":
                        valeur.append(3)
            elif(infix[i] in num):
                postfix.append(infix[i])
            else:
                print("Expression invalide")
        except Exception as e:
            print(e)
    for i in range(len(listop)):
         postfix.append(listop[i])
    return postfix
"""

operation ="-283.52/222+32*(-22)-3.2"
print(tokenize(operation))
