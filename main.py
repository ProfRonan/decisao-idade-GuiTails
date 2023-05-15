print("Digite um número")
número = int(input("> "))

if número < 0:
    print("Impossível!")
if número < 18:
    print("Não precisa se alistar.")
if número > 18: 
    print("Não esqueça de votar na próxima eleição.")
if número > 65:
    print("Vá descansar.")
else: 
    print("Eita!")
