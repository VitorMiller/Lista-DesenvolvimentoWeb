n1 = float(input("Digite o primeiro Número: "))
sinal = input("Digite a operação desejada (+-*/):")
n2 = float(input("Digite o segundo Número: "))

match sinal:
    case "*":
        print(n1*n2)
    case "/":
        print(n1/n2)
    case "+":
        print(n1+n2)
    case "-":
        print(n1-n2)
    
