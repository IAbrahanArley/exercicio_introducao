""" Solicite ao usuário um valor numérico, inteiro ou real, e escrever se é 
positivo ou negativo (considere o valor zero como positivo). """

num = int(input("digite um numero:"))

if (num >= 0):
    print(f"{num} é Positivo")
else:
    print(f"{num} é Negativo")