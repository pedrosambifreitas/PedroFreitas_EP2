#Pedro Sambi Freitas
# -*- coding: utf-8 -*-

from random import choice
import turtle

#abrindo a janela
janela = turtle.Screen()
janela.bgcolor("green")
janela.title("Jogo da Forca")
tartaruga = turtle.Turtle()


#desenhando a forca em funcao 
tartaruga = turtle.Turtle()
tartaruga.speed(20)
tartaruga.hideturtle()
tartaruga.penup()
tartaruga.setpos(-280,-10)
tartaruga.pendown()
tartaruga.color("black")
tartaruga.left(90)
tartaruga.forward(240)
tartaruga.right(90)
tartaruga.forward(100)
tartaruga.right(90)
tartaruga.forward(50)
tartaruga.penup()



#desenhando a cabeca
def cabeca():
	tartaruga.left(90)
	tartaruga.left(180)
	tartaruga.penup()
	tartaruga.setpos(-180,180)
	tartaruga.pendown()
	tartaruga.right(90)
	tartaruga.circle(19)
	tartaruga.left(90)
#desenha do o corpo
def corpo():
	tartaruga.penup()
	tartaruga.setpos(-180,140)
	tartaruga.pendown()
	tartaruga.forward(100)
	tartaruga.penup()
	
	
#desenha braco direito
def bracodireito():
	tartaruga.penup()
	tartaruga.setpos(-180,100)
	tartaruga.right(90)
	tartaruga.pendown()
	tartaruga.forward(50)
	tartaruga.penup()
	tartaruga.left(90)
	
	
#desenha braco esquerdo	
def bracoesquerdo():
	tartaruga.penup()
	tartaruga.setpos(-180,100)
	tartaruga.left(90)
	tartaruga.pendown()
	tartaruga.forward(50)
	tartaruga.penup()
	tartaruga.right(90)
	
#desenha perna esquerda
def pernaesquerda():
	tartaruga.penup()
	tartaruga.setpos(-180,40)
	tartaruga.left(30)
	tartaruga.pendown()
	tartaruga.forward(50)
	tartaruga.penup()
	tartaruga.right(30)
	
#desenha	
def pernadireita():
	tartaruga.penup()
	tartaruga.setpos(-180,40)
	tartaruga.right(30)
	tartaruga.pendown()
	tartaruga.forward(50)
	tartaruga.penup()
	tartaruga.left(30)
	
	
def desenho_geral():
	global erro
	if erro == 1:
		cabeca()
	if erro == 2:
		corpo()
	if erro == 3:
		bracodireito()
	if erro == 4:
		bracoesquerdo()
	if erro == 5:
		pernaesquerda()
	if erro == 6:
		pernadireita()
		



#abrindo entrada de texto salvo como entrada.txt, 
#criando lista vazia e adicionando as palavras limpas na lista
lista = list()
entrada = open("entrada.txt",encoding ='utf-8')
conteudo = entrada.readlines()

for i in conteudo:
	palavras=i.strip()
	if palavras != "":
		lista.append(palavras)
#codigo de normalizacao retirado do site :http://wiki.python.org.br/RemovedorDeAcentos
from unicodedata import normalize
def remover_acentos(txt):
	return normalize('NFKD', txt).encode('ASCII','ignore').decode('ASCII')
if __name__ == '__main__':
	from doctest import testmod
	testmod()		
#computador escolhendo e limpando a palavra, cria lista com as letars separadas
computador = choice(lista)
lopes = computador
escolha_computador = computador.lower()
escolha_computador = remover_acentos(escolha_computador)
tamanho = len(escolha_computador)
letras = list(escolha_computador)

# tracinhos
tartaruga.setheading(0)
tartaruga.penup()
tartaruga.speed(20)
tartaruga.setpos(-160,-10)
tartaruga.hideturtle()
tartaruga.setheading(0)
for i in range(tamanho):
	if letras[i] != " ":
		tartaruga.pendown()
		tartaruga.color("black")
		tartaruga.forward(25)
		tartaruga.penup()
		tartaruga.forward(15)
	elif letras[i] == " ":
		tartaruga.penup()
		tartaruga.forward(25)
		
			
erro = 0
acerto = 0
acerto2 = 0

while erro < 6 and acerto <len(escolha_computador): # e os espaços?
	tentativa = turtle.textinput("escolha da palavra","Escolha uma letra")
	tentativa = tentativa.lower()
	acerto2=0
	
		
	# logica do jogo
	for i in range(0,len(escolha_computador)):

		if tentativa == escolha_computador[i]:
			tartaruga.penup()
			tartaruga.setpos(-160+i*40,-10)
			tartaruga.pendown()
			tartaruga.write(computador[i])
			acerto+=1
			acerto2+=1
					
	if acerto2 == 0:
		erro+=1
		desenho_geral()
		
			

janela.exitonclick()

