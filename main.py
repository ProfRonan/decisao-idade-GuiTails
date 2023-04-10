print("Digite um número")
número = int(input("> "))

if número < 0:
    print("impossível!")
if número < 18:
    print("não precisa se alistar.")
if número > 18: 
    print("Não esqueça de votar na próxima eleição.")
if número > 65:
    print("Vá descansar.")
else: 
    print("eita!")
