import random

ordlista=["groda", "kanin", "råtta","djärv","björn","gädda","iller", "kossa", "torsk", "bäver"]
insults=["SÅ FACKING DUM", "Din hjärna har gått på semester och glömt att komma tillbaka", "Det är imponerande hur du alltid lyckas ha fel", "Du får en guldstjärna för försöket… men tyvärr ingen hjärncell på köpet", "Du är beviset på att inte alla utvecklas", "Om jag vill höra något korkat, ringer jag dig"]
insult_picked=random.choice(insults)
hemligt_ord=random.choice(ordlista)
while True: 
    gissning=input("Gissa ordet: ")
    if gissning==hemligt_ord:
        print("SÅ JÄVLA RÄTT")
        # nytt ord
        hemligt_ord=random.choice(ordlista)
    else: 
        insult_picked=random.choice(insults)
        print(insult_picked)
        # samma ord

