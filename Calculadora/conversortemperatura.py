def celsius_para_fahrenheit(temp_celsius):
    temp_fahrenheit = (temp_celsius * 9/5) + 32
    return temp_fahrenheit

def fahrenheit_para_celsius(temp_fahrenheit):
    temp_celsius = (temp_fahrenheit - 32) * 5/9
    return temp_celsius

print("Bem-vindo ao conversor de temperatura!")

while True:
    print("\nEscolha uma opção:")
    print("1. Celsius para Fahrenheit")
    print("2. Fahrenheit para Celsius")
    print("3. Sair")

    opcao = input("Digite o número da opção desejada: ")

    if opcao == "1":
        temp_celsius = float(input("Digite a temperatura em Celsius: "))
        temp_fahrenheit = celsius_para_fahrenheit(temp_celsius)
        print(f"A temperatura em Fahrenheit é {temp_fahrenheit:.2f}")
    elif opcao == "2":
        temp_fahrenheit = float(input("Digite a temperatura em Fahrenheit: "))
        temp_celsius = fahrenheit_para_celsius(temp_fahrenheit)
        print(f"A temperatura em Celsius é {temp_celsius:.2f}")
    elif opcao == "3":
        print("Obrigado por usar o conversor de temperatura!")
        break
    else:
        print("Opção inválida. Tente novamente.")
