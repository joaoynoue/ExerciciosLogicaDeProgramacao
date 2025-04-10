 #O usuário vai digitar um número inteiro, você deve verificar se ele é divisível por 3. Se o número
##Caso contrário, verifique qual dos dois números consecutivos ao digitado são divisíveis por 3
##obrigatoriamente um deles é divisível por 3).

a = int(input("Digite um número: "))

if a % 3 == 0:
    print("É divisível por 3")
elif (a + 1) % 3 == 0:
    print("O sucessor é divisível por 3")
elif (a - 1) % 3 == 0:
    print("O antecessor é divisível por 3")
else:
    print("Nem ele, nem o sucessor, nem o antecessor são divisíveis por 3")