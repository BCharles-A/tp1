operateur = ("+","-","/","*","^","(",")")
num = ("0","1","2","3","4","5","6","7","8","9", ".")
def tokenize(expression: str) -> list[str]:
    try:
        token = list(expression)
        for i in range(len(token)-1):
            while (token[i] in num and token[i+1] in num):
                token[i] = token[i] + token[i+1]
                token.pop(i+1)
    except Exception as e:
        print(e)
    return token

#def infix_to_postfix(tokens: list[str]) -> list[str]:
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
print(tokenize("28/2+3"))
