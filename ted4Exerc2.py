""" Problema: As maçãs custam R$ 1,30 cada, se forem compradas menos de uma dúzia, e R$ 1,00 se
forem compradas pelo menos 12. Escreva um programa que leia o número de maçãs compradas,
calcule e escreva o custo total da compra. """

quant = int(input("Quantas maças deseja levar?:"))


if (quant >= 12):
    total = quant * 1
  
    print("Quantidade de maças: {:3.2f} \nTotal: R${:10.2f}".format(quant, total))
else:
    total = quant * 1.30    
    print("Quantidade de maças: {:3.2f} \nTotal: R${:10.2f}".format(quant, total))