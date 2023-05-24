print("Digite um número")
número = int(input("> "))
X = False
if número < 0:
    print("Impossível!")
    X = True
if número < 18 and número >=0:
    print("Não precisa se alistar.")
    X = True
if número > 18 and número < 65: 
    print("Não esqueça de votar na próxima eleição.")
    X = True
if número > 65:
    print("Vá descansar.")
    X = True
if X is False:
    print("Eita!")
