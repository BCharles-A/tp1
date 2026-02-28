operateur = ("+","-","/","*","^","(",")")
num = ("0","1","2","3","4","5","6","7","8","9", ".")
def tokenize(expression: str) -> list[str]:
    compteur = 0
    try:
        token = list(expression.replace(" ", ""))
        for element in token:
            if(element not in operateur and element not in num):
                raise Exception("Expression invalide")
            if(element == "("):
                compteur += 1
            if(element == ")"):
                compteur -= 1
            if(compteur < 0):
                raise Exception("Expression invalide, Parenthèses mal fermées")
        if(compteur != 0):
            raise Exception("Expression invalide, Parenthèses non fermées")
        token.append("!")
        i = 0
        while(token[i] != "!"):
            if(token[i] == "-"):
                if(i == 0 or token[i-1] in operateur and token[i-1] != ")"):   
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
                raise Exception("Expression invalide, Trop de points")
            if(token[i].startswith(".")):
                token[i] = "0" + token[i]
            if(token[i].endswith(".")):
                token[i] = token[i] + "0"
        token.remove("!")
    except Exception as e:
        print(e)
    return token

valeur_op = {
        "+": 1,
        "-": 1,
        "/": 2,
        "*": 2,
        "^": 3,
        "(": 0,
        ")": 0
    }
def infix_to_postfix(tokens) -> list[str]:
    infix = tokenize(tokens)
    listnum = []
    listop = []
    for i in range(len(infix)):
        try:
            float(infix[i])
            num = True
        except ValueError:
            num = False
        if(num):
            listnum.append(infix[i])
        else:
            if(infix[i] == ")"):
                if("(" not in listop):
                    raise Exception("Expression invalide")
                else:

                    while(listop[-1] != "("):
                        listnum.append(listop.pop(-1))
                listop.pop(-1)

            elif(listop == []):
                listop.append(infix[i])

            elif(valeur_op.get(listop[-1]) >= valeur_op.get(infix[i])):
                listnum.append(listop.pop(-1))
                listop.append(infix[i])

            else:
                listop.append(infix[i])

    for i in range(len(listop)):
        listnum.append(listop.pop(-1))
    return listnum

def evaluate_postfix(tokens) -> float:
    postfix = infix_to_postfix(tokens)
    while len(postfix) > 1:
        for i in range(len(postfix)):
            if(postfix[i] in operateur and postfix[i] != "^"):
                x= float(postfix[i-1])
                y= float(postfix[i-2])
                match postfix[i]:
                    case "+":
                        valeur = x+y
                    case "-":
                        valeur = x-y
                    case "/":
                        valeur = x/y
                    case "*":
                        valeur = x*y
                postfix.pop(i)
                postfix.pop(i-1)
                postfix.pop(i-2)
                postfix.insert(i-2,valeur)
                break
    return postfix

operation ="(1+3*-22)*4+2"

print(tokenize(operation))
print(infix_to_postfix(operation))
print(evaluate_postfix(operation))
