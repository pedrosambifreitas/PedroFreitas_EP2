#Pedro Sambi Freitas
# -*- coding: utf-8 -*-

from random import choice
import turtle

#abrindo a janela
janela = turtle.Screen()
janela.bgcolor("green")
janela.title("Jogo da Forca")

#desenhando a forca
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


#abrindo entrada de texto salvo como entrada.txt
entrada = open("entrada.txt","r",encoding ='utf-8')
palavras = entrada.readlines()

lista = [0]*11
lista = [palavras]


escolha_computador = choice(lista)
print(escolha_computador)