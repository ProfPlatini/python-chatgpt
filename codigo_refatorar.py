# ==========================================
# VINLAND GAMES LTDA
# Projeto: Jogo de Adivinhação (Versão 0.1 - Legado)
# Autor: Estagiário Anterior (Demitido) 
#By: Platini
# ==========================================

import random

print("!!! BEM VINDO AO JOGO DA PIXEL FORGE !!!")
print("Tente adivinhar o numero secreto de 1 a 100")

# Variaveis com nomes ruins
n = random.randint(1, 100)
t = 0
acertou = 0

while acertou == 0:
    c = input("Digite seu chute: ")
    
    
    chute = int(c) 
    t = t + 1
    
    if chute == n:
        print("Parabéns, você ganhou!")
        print("Tentativas: ", t)
        acertou = 1
        
    
    if chute > n:
        print("Errou. O numero secreto é MAIOR que seu chute.") 
        
    if chute < n:
        print("Errou. O numero secreto é MENOR que seu chute.")

print("Obrigado por jogar nosso App!")