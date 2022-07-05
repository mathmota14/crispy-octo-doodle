número = input("Digite um número inteiro: ")
soma = 0

i = len(número)
while i > 0 :
    resto = int(número) % 10
    soma = soma + resto
    inteiro = int(número) // 10
    resto = inteiro
    número = resto
    i = i - 1
print(soma)