#Pedro Sambi Freitas
# -*- coding: utf-8 -*-

import random 
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
tartaruga.foward(240)
tartaruga.right(90)
tartaruga.foward(50)
tartaruga.right(90)
tartaruga.foward(50)


