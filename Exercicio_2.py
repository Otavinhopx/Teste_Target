def fibonacci(numero):
    a = 1
    b = 1
    sequencia = [0, 1, 1]
    
    if numero == 1 or numero == 2:
        print("1")
    else:
        contagem = 3
        while contagem <= numero:
            termo = a + b
            b = a
            a = termo
            contagem += 1
            sequencia.append(termo)
        print(sequencia)
        if numero in sequencia:
            print("Seu número está na sequência")
        else:
            print("Seu número não está na sequencia")
    
numero_escolhido = int(input("Insira um número: "))
fibonacci(numero_escolhido)