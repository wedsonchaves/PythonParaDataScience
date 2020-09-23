



print ("******************* Calculator Python ******************* \n \n \n ")


operacao = int(input("Digite a operaçao desejada: \n 1 - (Soma) \n 2 - (Subtraçao) \n 3 - (Divisao) \n 4 - (Multiplicaçao) \n ----------------------------->"))
num1 = int(input("Digite o primeiro número: "))
num2 = int(input("Digite o segundo número: "))


if operacao == 1:
    print ("Opçao soma selecionada. \n" , num1 , "+" , num2 , "=" , (num1 + num2))
elif operacao == 2:
    print ("Opçao subtracao selecionada. \n" , num1 , "-" , num2 , "=" , (num1 - num2))
elif operacao == 3:
    print ("Opçao divisao selecionada. \n" , num1 , "/" , num2 , "=" , (num1 / num2))
elif operacao == 4:
    print ("Opçao multiplicacao selecionada. \n" , num1 , "*" , num2 , "=" , (num1 * num2))
else:
    print ("Nenhuma opçao válida.")
