import tkinter as tk
from shunting_yard import infix_to_postfix, evaluate_postfix


def cliquer():
    global montre_postfix, montre_result
    try:
        montre_postfix.destroy()
        montre_result.destroy()
        postfix  = infix_to_postfix(equation.get())
        montre_postfix = tk.Label(fenetre, text=f"Postfix : {postfix}")
        montre_postfix.pack()
        result = evaluate_postfix(equation.get())
        montre_result = tk.Label(fenetre, text=f"Résultat : {result}")
        montre_result.pack()
    except ZeroDivisionError:
        montre_result = tk.Label(fenetre, text="Erreur : Division par zéro")
        montre_result.pack()
    except Exception as e:
        montre_result = tk.Label(fenetre, text=f"{e}")
        montre_result.pack()

fenetre = tk.Tk()
fenetre.geometry("800x400")
equation = tk.StringVar()
montre_result = tk.Label(fenetre, text="")
montre_result.pack()
montre_postfix = tk.Label(fenetre, text="")
montre_postfix.pack()
tk.Label(fenetre, text="Entrez une expression mathématique :").pack()
tk.Entry(fenetre, textvariable=equation).pack()
bouton = tk.Button(fenetre, text="Calculer", command=cliquer)
bouton.pack()

fenetre.mainloop()

print("Fin du programme")