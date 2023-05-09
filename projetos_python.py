'''

#nome = 'gabriel'
#sobrenome = 'costa'
#idade = 30

#print(nome, sobrenome, idade)

#soma
#print(4+5)

#junção string
#print('5''4')

#interação com usuario
#nome1 = input('Qual é seu nome ?')
#idade1 = input('Qual sua idade ?')
#peso = input ('Qual seu peso ?')

#print('Seu nome é '+nome1+', tem '+idade1+' anos de idade e pesa Kg '+peso)

#soma de numeros
#print('Bem vindo a calcuradora do biel :D ')

#n1 = int(input('Digite um numero: '))
#n2 = int(input('Digite outro numero: '))
#r = int(n1)+int(n2)

#print('Resultado da soma entre esses numeros é de: {} '.format(r)) or
#print('Resultado da soma entre esses numeros é de: ') r

#aula6
#tiṕosprimitivos
#funções para trablhamoor com string, numeros, booleano, float e etc..


#n1 = int(input('Digite o um numero : '))
#n2 = int(input('Digite o segundo numero: '))
#res = n1+n2

#print('A soma do numero {} e numero {} vale {}'.format(n1, n2, res))


#.isnumeric é numerico ?
#.isalpha é aphanumerico ?
#.isalnum é numerico e alpha ?
#.isdecimal
#.isupper()
#v= oi
#EXEMPLO
#print(v.isnumeric())
#RESPOSTA SERA SEMPRE TRUE OU FALSE

#v = input('Digite algo : ')

#print('seu tipo primitivo é : ', type(v))
#print('é um numero ? ', v.isnumeric())
#print('tem letras e numeros ?', v.isalnum())
#print('esta em letra maiscula ? ', v.isupper())
#print('esta em letra minuscula ? ', v.islower())
#print('esta espaçada ? ', v.isspace())
#print('esta capitalizada ? ', v.istitle())



#===============================================================================#
#================================================================================#


#aula-7- operadores aritmeticos
#ordem-de-precedencia--> 1°()-2°**-3°*-4°/-5°//-6°%- 7°+ e 8°-

#1-exercicio

#n1 = int(input('Digite um numero :'))
#print('Seu antecessor de {}, é {} e seu sucessor é {}'.format(n1,(n1-1),(n1+1)))

#2exercicio

#n1 = int(input('Digite um numero : '))
#print('seu dobro é : {}'.format(n1*2))
#print('seu triplo é : {}'.format(n1*3))
#print('sua raiz quadrada é :{} '.format(n1**(1/2)))

#3exercicio

#n1 = int(input('Digite a primeira nota : '))
#n2 = int(input('Digite a segunda nota : '))
#res = ((n1 + n2)/2)
#print('A média é : {}' .format(res))

#4exercicio

#n1 = int(input('Digite o metro: '))
#print('convertido em milimetros: {}' .format(n1*1000))
#print('convertido em  centimetro é : {}' .format(n1*100))

#5exercicio - tabuada

#n1 = int(input('Digite um numero: '))
#aux = 0
#print('*'*18)
#print('Tabuada do numero : {}' .format(n1))
#print('*'*18)
#while(aux <= 10):
 #   print('{} x {}={}' .format(aux, n1, (aux*n1)))
  #  aux = aux+1

#exercicio-6- reais para dolares

#cart =float(input('Digite  o valor de sua carteira: '))
#dol = float(5.15)
#print('seu valor  em dolares é de : {}' .format(float(cart//dol)))


#exercicio-7- calcular altura e largura em metros e ter uma base quanto gasta de tinta em 2m²

#alt = int(input('Digite a altura: '))
#lar = int(input('Digite a largura: '))
#res = (alt*lar)/2
#print('Você ira precisar de {} litros de tinta' .format(res))

#exercicio-8- ler um valor e dar um deconto de 5 %

#val = int(input('Digite o valor do produto : '))
#res = (val*5)/100
#print('O valor do produto com desconto é de: {}'.format(val-res))

#exercicio-9- mostre salario de um funcionario atual e com ajuste de 15%

#sal = int(input('Digite o valor de seu salario: '))
#sal1 = (sal*15)/100
#print('Seu novo com salario com ajuste de 15% é de : {}' .format(sal+sal1))

#exercico-10- calculo de diarias e km aser pago por carro de locação
#km = float(input('Digite os km Rodado: '))
#day = int(input('Quantas dias de locação :  '))
#payKm = 0.15
#payDay = 60
#resKm = km*payKm
#resDay = day*payDay
#print('Foi utilizado {} Kms e {} diaria(s), o valor a ser pago é de R${:.2f}' .format(km, day, (resKm+resDay)))

#####################MODULOS#########################
#modulos são bibliotecas que saõ importadas para IDE, onde são guardadas pacotes de funções.

#execicios- 11 - monstrando uma porção inteira de um numero fracionado.

#import math <- importa todas funções da biblioteca math(matematica)
#from math import trunc <- importa somente a função trunc da biblioteca math.
#n = float(input('Digite um numero : '))
#print('Porção inteira desde numero é de : {}'.format(math.trunc(n)))

#sorteio de nomes

#from random import choice
#aluno1 = str(input('Digite o nome do primeiro aluno: '))
#aluno2 = str(input('Digite o nome do segundo aluno: '))
#aluno3 = str(input('Digite o nome do terceiro aluno: '))
#aluno4 = str(input('Digite o nome do quarto aluno: '))

#sort =choice([aluno1, aluno2, aluno3, aluno4])
#print('O aluno que ira apagar o quadro hoje é : {}' .format(sort))



#ex:22
frase = str(input('Digite seu nome: ')).strip()
print(frase.upper())#tudo em maiscula
print(frase.lower())#tudo em minusculo
print('seu nome tem ao todo {} letras'.format(len(frase) - frase.count(' ')))quantos caracteres tirando todos os espaçoes

spl = frase.split()#criando menu na frase
print(len(spl[0]))#caracteres da primeira palavra da frase, criando um menu e pegando os caracteres
import datetime

#ex:23
#criar um programa que leia uma sequecia de 4 numero e o divida em 4.
#ex:24
#criar um programa que fala se o primeiro nome comeca com santo
#ex:25
#criar um programa que mostre se tem silva no nome
name = input('digite seu nome: ')
print(name.find('silva'))

#ex:26
#escreve uma frase e pesquisar quantas vezes aparece a letra a,em que posição ela aparece a primeira vez,e ultima vez
name = input('escreva sua frase : ')
res = name.count('a')
print('quantidade de "A" que sua frase tem é de : {}' .format(res))
print(name.find('a'))
#ex:27
#faça o programa que leia nome completo e mostre o primeiro nome e ultimo.
name = input('insira seu nome: ')
res = name.split()
print('seu primeiro nome é :{} ' .format(res[0]))
print('seu segundo o nome é :{} ' .format(res[2]))

#CONDIÇÕES AULA 10_

nome = str(input('Qual é seu nome: '))
if nome == 'Gabriel':
    print('Você Gabriel é um gostoso')
else:
    print('Você é um frango kkkk')

#exercicio_28_ sorteio_ de_numeros
from random import choice
number = choice([0, 1, 2, 3, 4, 5])
print(number)
number_es = int(input('Digite um numero de 0 a 5 e adivinhe qual numero a maquina escolheu ?'))

if number == number_es:
    print('Parabens Você adivinhou o numero escolhido pelo computador !! S2')
else:
   print(' Você Falhou :(, tente novamente !!')
#testando-git

#teste_segundo_commit_2

#exercicio_29_multa _de_velocidade

velocidade = int(input(" A velocidade permitida é 80Km, Qual Foi a velocidade medida ? "))
valorMulta = 7

if velocidade > 80:
    print("Você foi multado !! . \n  O valor da multa é: R$:{}".format((velocidade-80)*valorMulta))
else:
    print("Boa Viagem")

#exercicio_30_mosntrnado se o numero é impar ou par

number = int(input("Digite um numero : "))

if number/2 == 0:
    print("este numero é par !! ")
else:
    print("este numero é ímpar")

#exercicio_31_ calculando custo de viagem por km rodado
kilos = int(input("Qual a distancia da viagem em Km ?"))

km1 = 0.50
km2 = 0.45
if kilos <= 200:
    
     print("sua viagem custara: R${:.2f} Reais".format(km1*kilos))
else:
    print("sua viagem custara: R${:.2f} Reais".format(km2*kilos))

#exercicio_32_ calculado ano bissexto

data = int(input("Informe a data que deseja saber se o ano é bissexto ou não !!"))


if data % 4 == 0 and data % 100 != 0 or data % 400 == 0:
    print("Este ano é bissexto ")
else:
    print("Este ano não é bissexto ! ")


#exercicio_33_lendo tras numeros e mosntrando qual menor e maior
num1 = int(input("Escolha um numero : "))
num2 = int(input("Escolha outro numero : "))
num3 = int(input("Escolha o terceiro numero : "))
res = sorted([num1,num2,num3])

print("o numero maior é:{}".format(res[2]))
print("o numero menor é: {}".format(res[0]))

#exercicio_34__(ajsute de salario em 10 e 15 %

sal = float(input('Qual é seu salario atual: '))

sal_10 = 10 * sal / 100
sal_15 = 15 * sal / 100

print(sal_10)
print(sal_15)

if sal >= 1250:
    print("Seu Salario novo ajustado é de : R${:.2f}".format(sal + sal_10))
elif sal < 1250:
    print("Seu Salario novo ajustado é de : R${:.2f}".format(sal + sal_15))
else:
    print('nada')

#exercicio_35_colentando_3_medidas_e_verificar_se_as_mesmas_forma_um_triangulo

med1 = float(input('Digite a primeira medida'))
med2 = float(input('Digite a segunda medida'))
med3 = float(input('Digite a terceira medida'))

if med1 < med2+med3 and med2 < med1+med3 and med3 < med1+med2:
    print('Conseguimos fazer o triangulo')
else:
    print('Não Conseguimos criar o triangulo :(')

#AULA_12_CONDIÇÕES_ANINHADAS

#exercicio_36_ arpovando emprestimo em base dos 30% do salario e em quanto tempo

print('=' * 20)
print('Bem Vindo a Crefisa Emprestimos House')
print('=' * 20)

valor = float(input('Digite o Valor do imovel que deseja adquirir : '))
salario = float(input('Digite Seu salario liquido : '))
ano = int(input('Digite em quantos anos desejar pagar: '))
porc_sal = (30 * salario) / 100

if valor / (ano * 12) <=  porc_sal:#3.600

    print('Seu emprestimo esta aprovado !!, sua parcela sera no valor de R$ {:.2f}'.format(valor / (ano * 12)))
else:
    print('Crédito reprovado !!!')

#exercicio_37




number = int(input('Digite o numero que deseja converter : '))
opcao = int(input('Digite 1 para conversão em BINARIO \n''Digite 2 para conversão em OCTAL''\nDigite 3 para conversão em HEXADECIMAL\n''--> :'))

if opcao == 1:
    print('O numero {} em BINARIO é :{} '.format(number, bin(number)[2:]))
elif opcao == 2:
    print('O numero {} em OCTAL é :{} '.format(number, oct(number)[2:]))
elif opcao == 3:
    print('O numero {} em HEXADECIMAL é :{} '.format(number, hex(number)[2:]))
else:
    print('Tente novamente')




#exercicio_38

number1 = int(input('Digite um numero : '))
number2 = int(input('Digite outro numero : '))

if number1 > number2:
    print('O primeiro valor é maior')
elif number2 > number1:
    print('O segundo valor é maior ')
else:
    print('Não existe valor maior, os dois são iguais')

#exercicio_39

import datetime
data = int(input('Informe sua ano de nascimento com 4 digitos  : '))
date_now = datetime.datetime.now().date().year
if date_now - data < 18:
    dataFal = date_now - data
    print('Calma gafanhoto ainda nao é sua hora !!, falta {}'.format(18- dataFal))

elif date_now - data == 18:
    print('Já é a hora de se alistar')

elif date_now - data > 18:
    temp = date_now - data
    temp1 = temp - 18
    print('Já passou seu tempo de se alistar, Já passou : {} ano(s) '.format(temp1))

#exercicio_40


nota1 = float(input('Digite a primeira nota: '))
nota2 = float(input('Digite a segunda nota: '))
res = (nota1+nota2)/2
print(res)

if res >= 7:
    print('Você esta aprovado !!')

elif res <= 4.9:
    print('Você esta reprovado !!')

elif res >=5 or 6.9:
    print('Você esta recuperação !!')

#exercicio_ 41
import datetime
ano = int(input('Digite o ano de nascimento: '))
data_res = datetime.datetime.now().date().year - ano

if data_res >= 9:
 print('Sua categoria será mirim')

elif data_res >= 14:
 print('Sua categoria será infantil')

elif data_res >= 19:
 print('Sua categoria será junior')

elif data_res>= 20:
 print('Sua categoria será senior')

elif data_res > 21:
 print('Sua categoria será master')

#exercicio_42_ listar resultados de possiveis triangulos equilatero ou isosceles ou escaleno

med1 = float(input('Digite a primeira medida'))
med2 = float(input('Digite a segunda medida'))
med3 = float(input('Digite a terceira medida'))

if med1 < med2+med3 and med2 < med1+med3 and med3 < med1+med2:
    print('Conseguimos fazer o triangulo')

    if med1 and med2 and med3 == med1 and med2 and med3:
        print('Todos os lados do trianguo são iguais')
    elif med1 == med2 or med1 == med3 and med2 == med3:
        print('dois lados são iguais')
    elif med1 != med2 and med2 != med3:
        print('todos os lados são diferentes')
else:
    print('Não Conseguimos criar o triangulo :(')

#exercicio_43 _ calculando massa corporal


peso = float(input('Digite seu peso: '))
altura = float(input('Digite sua altura: '))
res = float(format(peso / (altura*altura), '.2f'))

print(res)

if res < 18.4:
    print('Voce esta abaixo do peso ! ')

elif res >= 18.5 and res <= 25:
    print('Peso ideal !')

elif res >= 25 and res <= 30:
    print('Sobre peso !')

elif res >= 30 and res <= 40:
        print('obesidade !')

elif res > 40:
    print('obesidade morbida !')
else:
    print('nada')


#exercicio_43

valor_preco = float(input('Digite o valor do produto R$ :'))
print(' ' * 2)
form_pag = int(input('Pagamento em dinheiro ou cheque a vista " 1 "\n Pagamento cartão de débito "2"\n pagamento no cartão de credito "3"'))

if form_pag == 1:
    desc_10 = (10 * valor_preco) / 100
    print('O valor a vista dinheiro ou cheque ficara R${:.2f} reais '.format(valor_preco - desc_10))
elif form_pag == 2:
    desc_5 = (5 * valor_preco) / 100
    print('O valor a vista no cartão ficara R${:.2f} reais '.format(valor_preco - desc_5))
    

elif form_pag == 3:
    parcelas = int(input('Parcelas ?'))
    if parcelas >=3:
        juros = (20*valor_preco)/ 100
        print('O valor do parcelado em {} ficara por R$ {}'.format(parcelas, valor_preco+juros))
    else:
        print('O valor do produto no cartão ficara {}'.format(valor_preco))
#exercicio_45

from random import randint
from time import sleep
itens = ['pedra','papel','tesoura']
computador = randint(0, 2)
print('Suas ações \npedra[0]\npapel[1]\ntesoura[2]\n')
print(computador)
acao = int(input('Qual sua jogada ?\n'))
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PÔ')
sleep(1)
print('=' * 10)

if computador == 0:
    if acao == 1:
        print('você ganhou')
    elif acao == 2:
        print('você perdeu')
    else:
        print('Empate')

if computador == 1:
    if acao == 2:
        print('você ganhou')
    elif acao == 0:
        print('você perdeu')
    else:
        print('Empate')

if computador == 2:
    if acao == 1:
        print('você ganhou')
    elif acao == 0:
        print('você perdeu')
    else:
        print('Empate')

#aula_13_ estrutura for
for c in range(0, 20, 2) :
    print(c)
'''
'''
i = int(input('Digite o numero de inicio: '))
f = int(input('Digite o numero de fim: '))
p = int(input('Digite o numero de passo(s): '))
for c in range(i, f, p):
    print(c)
print('FIM')


#exercicio_46_ contagem regressiva de 10 a 0.

from time import sleep
i = int(input('Digite o numero de inicio: '))
f = int(input('Digite o numero de fim: '))

for c in range(10, -1, -1):
    print(sleep(1), c)
print('Feliz ano novo !!, Fogos !!')

#exercicio_47_ numeros pares de 1 a 50

for c in range(2, 51, 2):
    print(c)

#exercicio_48

s = 0
for c in range(1, 501, 2):
    if c% 3 == 0:
        s += c
print(s)
'''
#exercicio 49

