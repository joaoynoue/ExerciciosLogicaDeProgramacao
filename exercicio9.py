#A pessoa deve inserir o nome e você deve verificar se o nome começa com vogal. (dicas: nome[0]
#fala qual é a primeira letra na string armazenada em nome. Use nome.lower() para colocar todas
#as letras do nome minúsculo (Por que seria importante colocar as letras em minúsculo?).


nome = str(input("Digite seu nome: "))

vogais = ('a', 'e', 'i', 'o', 'u')  

nome = nome.lower()  

if nome[0] in vogais:
    print("Seu nome começa com uma vogal.")
else:
    print("Seu nome não começa com uma vogal.")