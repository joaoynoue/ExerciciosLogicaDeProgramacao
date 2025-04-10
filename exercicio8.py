#O usuário digitará 3 notas e você deve exibir uma mensagem nas seguintes condições:
#I) Se média < 6, usuário reprovado
##II) Se 6<=média e média < 8, usuário em recuperação
###III) Se média >= 8, usuário aprovado

a = float(input("Digite um número: "))
b = float(input("Digite outro número: "))
c = float(input("Digite outro número: "))

media = (a + b + c)/3 

if media < 6:
    print('usuario reprovado')
elif 6 <= media and media < 8:
    print("usuario em recuperação")
elif media >=8 :
    print("usuário aprovado")