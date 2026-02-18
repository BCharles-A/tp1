operateur = ("+","-","/","*","^","(",")")
num = ("0","1","2","3","4","5","6","7","8","9", ".")
def tokenize(expression: str) -> list[str]:
    try:
        token = list(expression)
        for i in range(len(token)):
            position = [index for index ,x in enumerate(token) if x in num]
        for i in range(len(position)):
            if(position[i]+1 == position[i+1]):
                token[position[i]] = token[position[i]],token[position[i+1]]
                token[position[i+1]]
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
#        try:
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
#        except Exception as e:
#            print(e)
    for i in range(len(listop)):
         postfix.append(listop[i])
    return postfix
print(tokenize("28/2+3"))
