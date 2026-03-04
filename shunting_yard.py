operateur = ("+","-","/","*","^","(",")")
num = ("0","1","2","3","4","5","6","7","8","9", ".")
def tokenize(expression: str) -> list[str]:
    compteur = 0
    try:
        expression = expression.replace("-(", "-1*(")
        expression = expression.replace("()", "")
        token = list(expression.replace(" ", ""))
        if(token == []):
            raise Exception("Expression vide")
        for element in token:
            if(element not in operateur and element not in num):
                raise Exception("Expression invalide: caractère invalide")
            if(element == "("):
                compteur += 1
            if(element == ")"):
                compteur -= 1
            if(compteur < 0):
                raise Exception("Expression invalide: parenthèse mal placée")
        if(compteur != 0):
            raise Exception("Expression invalide: parenthèse non fermée")
        token.append("!")
        i = 0
        while(token[i] != "!"):
            if(token[i] == "-"):
                if(i == 0 or token[i-1] in operateur and token[i-1] != ")"):  
                    while(token[i+1] in num):
                        token[i] = token[i] + token.pop(i+1)
                else:
                    pass
            if(token[i] in num):
                if(i+1 <= len(token)-1):
                    while(token[i+1] in num):
                        token[i] = token[i] + token.pop(i+1)
            i += 1
        for i in range(len(token)):
            if(token[i].count(".") > 1):
                raise Exception("Invalide: trop de points")
            if(token[i].startswith(".")):
                token[i] = "0" + token[i]
            if(token[i].endswith(".")):
                token[i] = token[i] + "0"
            if(token[i] == "."):
                token[i] = "0.0"
            if(token[i] in operateur and token[i] != "(" and token[i] != ")"):
                if(i == 0 or token[i-1] in operateur and token[i-1] != ")"):
                    raise Exception("Expression invalide: opérateur mal placé")
        if(token[-2] in operateur and token[-2] != ")"):
            raise Exception("Expression invalide: opérateur en fin d'expression")
            
        token.remove("!")
        return token
    except Exception as e:
        print(e)
        raise

valeur_op = {
        "+": 1,
        "-": 1,
        "/": 2,
        "*": 2,
        "^": 3,
        "(": 0,
        ")": 0
    }

def infix_to_postfix(infix:list[str]) -> list[str]:
    listnum = []
    listop = []
    for exp in infix:
        if(exp not in operateur):
            listnum.append(exp)
        else:
            if(exp == "("):
                listop.append(exp)
            
            elif(exp == ")"):
                if("(" not in listop):
                    raise Exception("Expression invalide: parenthèse non fermée")
                else:

                    while(listop[-1] != "("):
                        listnum.append(listop.pop())
                listop.pop()

            elif(listop == []):
                listop.append(exp)

            elif(valeur_op.get(listop[-1]) >= valeur_op.get(exp)):
                    listnum.append(listop.pop())
                    listop.append(exp)
                

            else:
                listop.append(exp)

    for i in range(len(listop)):
        listnum.append(listop.pop())
    return listnum

def evaluate_postfix(postfix:list[str]) -> float:
    try:
        while len(postfix) > 1:
            for i in range(len(postfix)):
                if(postfix[i] in operateur):
                    x= float(postfix[i-2])
                    y= float(postfix[i-1])
                    match postfix[i]:
                        case "+":
                            valeur = x+y
                        case "-":
                            valeur = x-y
                        case "/":
                            valeur = x/y
                        case "*":
                            valeur = x*y
                        case "^":
                            valeur = x**y
                    postfix.pop(i)
                    postfix.pop(i-1)
                    postfix.pop(i-2)
                    postfix.insert(i-2,valeur)
                    break
        return float(postfix[0])
    except ZeroDivisionError as e:
        print("Division par zéro")
        raise