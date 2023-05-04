import math

print("Calculadora Científica\n")

while True:
    print("Escolha uma operação:")
    print("1 - Soma")
    print("2 - Subtração")
    print("3 - Multiplicação")
    print("4 - Divisão")
    print("5 - Potência")
    print("6 - Raiz Quadrada")
    print("0 - Sair")
    op = int(input("Opção: "))
    
    if op == 0:
        break
        
    if op >= 1 and op <= 4:
        num1 = float(input("Digite o primeiro número: "))
        num2 = float(input("Digite o segundo número: "))
    elif op == 5:
        num1 = float(input("Digite o número base: "))
        num2 = float(input("Digite o expoente: "))
    elif op == 6:
        num1 = float(input("Digite o número: "))
    
    if op == 1:
        resultado = num1 + num2
        print("Resultado:", resultado)
    elif op == 2:
        resultado = num1 - num2
        print("Resultado:", resultado)
    elif op == 3:
        resultado = num1 * num2
        print("Resultado:", resultado)
    elif op == 4:
        if num2 != 0:
            resultado = num1 / num2
            print("Resultado:", resultado)
        else:
            print("Não é possível dividir por zero!")
    elif op == 5:
        resultado = math.pow(num1, num2)
        print("Resultado:", resultado)
    elif op == 6:
        resultado = math.sqrt(num1)
        print("Resultado:", resultado)
    else:
        print("Opção inválida!")
    
    input("\nPressione Enter para continuar...")
    print("\n")
