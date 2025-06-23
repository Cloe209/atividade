#1° como colocar cores no terminal sem usar bibliotecas?
print("\33[34m*\33[0m"*25)
print("\33[32mmeu programa em pyhton\33[0m")
print("\33[34m*\33[0m"*25)
#2° passo: colocar as cores
#colocamos as cores sem instalar bibliotecas usando a tabela ANSI ou ASCII
#o que é? é uma tabela de codificação de caracteres
#o codigo ANSI é usado para modificar cores no terminal
print("\33[31mEsse texto está vermelho\33[0m")
#31m é referente a cor vermelha
#0 32 é a verde
#o 34 é azul
#codificações da tabela ANSI
#30: preto, 31:vermelho, 32:verde, 33:amarelo, 34:azul, 35: roxo, 36: ciano, 37: branco
#outra forma de fazer: biblioteca colorama
#pip install colorama
print("\33[41;37mEsse texto tem fundo vermelho e letras brancas\33[0m")
print("\33[44;33m*\33[0m"*25)
print("\33[44;33mMeu programa de Python\33[0m")
print("\33[44;33m*\33[0m"*25)
print("\33[31mBem-vindo(a)\33[0m")
#3° passo: cor de fundo e cor do texto