#Pedro Sambi Freitas
# -*- coding: utf-8 -*-

from random import choice
import turtle

#abrindo a janela
janela = turtle.Screen()
janela.bgcolor("green")
janela.title("Jogo da Forca")

#desenhando a forca em funcao 
tartaruga = turtle.Turtle()
tartaruga.speed(20)
tartaruga.penup()
tartaruga.setpos(-250,-10)
tartaruga.pendown()
tartaruga.color("black")
tartaruga.left(90)
tartaruga.forward(240)
tartaruga.right(90)
tartaruga.forward(100)
tartaruga.right(90)
tartaruga.forward(50)


#abrindo entrada de texto salvo como entrada.txt, 
#criando lista vazia e adicionando as palavras limpas na lista
lista = list()
entrada = open("entrada.txt",encoding ='utf-8')
conteudo = entrada.readlines()

for i in conteudo:
	palavras=i.strip()
	if palavras != "":
		lista.append(palavras)
		
#computador escolhendo e limpando a palavra
computador = choice(lista)
escolha_computador = computador.lower()
acerto = 0
errado = 0
tamanho = len(escolha_computador)

# tracinhos
tartaruga.speed(20)
tartaruga.setpos(-220,-10)
for i in range(tamanho):
	if i != "":
		tartaruga.pendown()
		tartaruga.color("black")
		tartaruga.forward(10)
		tartaruga.penup()
		tartaruga.forward(5)
	
		
	
"""
while erro < 6 and acerto < len(computador): # e os espaços?
	tentativa = janela.textinput("Escolha uma letra")
	tentativa = tentativa.lower()
	# logica do jogo
	if tentativa in escolha_computador
"""



