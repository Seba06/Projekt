import random

ordlista=["groda", "kanin", "råtta","djärv","björn","gädda"]
insult=["SÅ FACKING DUM"]
hemligt_ord=random.choice(ordlista)
while True: 
    gissning=input("Gissa ordet: ")
    if gissning==hemligt_ord:
        print("SÅ JÄVLA RÄTT")
    else: 
        print("SÅ FACKING DUM")

