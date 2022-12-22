#Vamos construir uma calculadora usando a biblioteca tkinter em Python

#0: Importando as bibliotecas usadas
import tkinter as tk
import tkinter.ttk as ttk
import time
from math import sqrt

#1: Construindo uma janela 
janela=tk.Tk()
janela.title('Calculadora')
janela.resizable(True, True)


#2: Criando o layout do aplicativo
#2.1: Configurando o grid da tela do aplicativo
for i in range(5):
 for j in range(5):
  janela.columnconfigure(j, weight=1, minsize=50)
  janela.rowconfigure(i, weight=1, minsize=50)


#2.2:Criando o display da tela
display_valor=tk.DoubleVar()
display_frame=tk.Frame(relief=tk.SUNKEN, borderwidth=5)
display_frame.grid(row=0, column=0, columnspan=5)
display=tk.Entry(bg='white', fg='black', master=display_frame)
display.pack()


'''Módulo de teste do display da calculadora, use um # após o teste'''
#display_valor=3.1415
#display.insert(tk.INSERT, display_valor)


#2.3: Criando as funções que são acionadas pelos botões da calculadora
#2.3.1: Encerrar aplicativo

def sair():
 '''Função para encerrar a aplicação'''
 time.sleep(0.3)
 quit()

#2.3.2:Inserindo e limpando conteudo do display
def clean():
 '''Função que limpa o display da calculadora e reseta os operadores da calculadora'''
 global somar
 global subtrair
 global multiplicar
 global dividir
 display.delete(0, tk.END)
 somar=False
 subtrair=False
 multiplicar=False
 dividir=False

def put_0():
 '''Função para inserir contéudo no display'''
 display.insert(tk.INSERT, 0)

def put_1():
 '''Função para inserir contéudo no display'''
 display.insert(tk.INSERT, 1)

def put_2():
 '''Função para inserir contéudo no display'''
 display.insert(tk.INSERT, 2)

def put_3():
 '''Função para inserir contéudo no display'''
 display.insert(tk.INSERT, 3)

def put_4():
 '''Função para inserir contéudo no display'''
 display.insert(tk.INSERT, 4)

def put_5():
 '''Função para inserir contéudo no display'''
 display.insert(tk.INSERT, 5)

def put_6():
 '''Função para inserir contéudo no display'''
 display.insert(tk.INSERT, 6)

def put_7():
 '''Função para inserir contéudo no display'''
 display.insert(tk.INSERT, 7)

def put_8():
 '''Função para inserir contéudo no display'''
 display.insert(tk.INSERT, 8)

def put_9():
 '''Função para inserir contéudo no display'''
 display.insert(tk.INSERT, 9)

def put_point():
 '''Função para inserir contéudo no display'''
 display.insert(tk.INSERT, '.')

#2.3.3: Criando variáveis para alocar as duas parcelas das operações e indicar quais operações devem ser performadas ao clique de um botão
parcela1=tk.DoubleVar()
parcela2=tk.DoubleVar()
somar=tk.BooleanVar()
subtrair=tk.BooleanVar()
multiplicar=tk.BooleanVar()
dividir=tk.BooleanVar()

'''Módulo de teste de variáveis da calculadora, use um # após o teste'''
#parcela1=display.get()
#print(parcela1)


#2.3.4:Funções dos operadores matemáticos

def plus_minus():
 '''Função que inverte o sinal do número exibido no display da tela'''
 display_valor1=tk.DoubleVar()
 display_valor2=tk.DoubleVar()
 display_valor1.set(display.get())
 display_valor2=(-1.0)*display_valor1.get()
 display.delete(0, tk.END)
 display.insert(tk.INSERT, display_valor2) 

def add(parcela1):
 '''Função para executar a operação de soma'''
 global somar
 global subtrair
 global multiplicar
 global dividir
 somar=True
 subtrair=False
 multiplicar=False
 dividir=False
 parcela1.set(display.get())
 display.delete(0, tk.END)

def subtract(parcela1):
 '''Função para executar a operação de soma'''
 global somar
 global subtrair
 global multiplicar
 global dividir
 somar=False
 subtrair=True
 multiplicar=False
 dividir=False
 parcela1.set(display.get())
 display.delete(0, tk.END)

def multiply(parcela1):
 '''Função para executar a operação de soma'''
 global somar
 global subtrair
 global multiplicar
 global dividir
 somar=False
 subtrair=False
 multiplicar=True
 dividir=False
 parcela1.set(display.get())
 display.delete(0, tk.END)

def divide(parcela1):
 '''Função para executar a operação de soma'''
 global somar
 global subtrair
 global multiplicar
 global dividir
 somar=False
 subtrair=False
 multiplicar=False
 dividir=True
 parcela1.set(display.get())
 display.delete(0, tk.END)

def square_root(parcela1):
 '''Função para extrair a raíz quadrada de um número'''
 result=tk.DoubleVar()
 parcela1.set(display.get())
 display.delete(0, tk.END)
 result=sqrt(parcela1.get())
 display.insert(tk.INSERT, result)

def show_result(parcela1, parcela2):
 '''Função que recebe a segunda  parcela da operação e performa o resultado final'''
 parcela2.set(display.get())
 display_resultado=tk.DoubleVar()  
 display.delete(0, tk.END)
 if(somar==True and subtrair==False and multiplicar==False and dividir==False):
  display_resultado=parcela1.get()+parcela2.get()
 if(somar==False and subtrair==True and multiplicar==False and dividir==False):
  display_resultado=parcela1.get()-parcela2.get()
 if(somar==False and subtrair==False and multiplicar==True and dividir==False):
  display_resultado=parcela1.get()*parcela2.get()
 if(somar==False and subtrair==False and multiplicar==False and dividir==True):
  display_resultado=parcela1.get()/parcela2.get()
 display.insert(tk.INSERT, display_resultado)


#2.4:Criando os botões da calculadora
#2.4.1: Teclado numérico
zero_frame=tk.Frame(relief=tk.RAISED, borderwidth=1)
zero_frame.grid(row=4, column=0)
zero=tk.Button(text='0', master=zero_frame,command=put_0)
zero.pack()

um_frame=tk.Frame(relief=tk.RAISED, borderwidth=1)
um_frame.grid(row=3, column=0)
um=tk.Button(text='1', master=um_frame,command=put_1)
um.pack()

dois_frame=tk.Frame(relief=tk.RAISED, borderwidth=1)
dois_frame.grid(row=3, column=1)
dois=tk.Button(text='2', master=dois_frame,command=put_2)
dois.pack()

tres_frame=tk.Frame(relief=tk.RAISED, borderwidth=1)
tres_frame.grid(row=3, column=2)
tres=tk.Button(text='3', master=tres_frame,command=put_3)
tres.pack()

quatro_frame=tk.Frame(relief=tk.RAISED, borderwidth=1)
quatro_frame.grid(row=2, column=0)
quatro=tk.Button(text='4', master=quatro_frame, command=put_4)
quatro.pack()

cinco_frame=tk.Frame(relief=tk.RAISED, borderwidth=1)
cinco_frame.grid(row=2, column=1)
cinco=tk.Button(text='5', master=cinco_frame,command=put_5)
cinco.pack()

seis_frame=tk.Frame(relief=tk.RAISED, borderwidth=1)
seis_frame.grid(row=2, column=2)
seis=tk.Button(text='6', master=seis_frame,command=put_6)
seis.pack()

sete_frame=tk.Frame(relief=tk.RAISED, borderwidth=1)
sete_frame.grid(row=1, column=0)
sete=tk.Button(text='7', master=sete_frame,command=put_7)
sete.pack()

oito_frame=tk.Frame(relief=tk.RAISED, borderwidth=1)
oito_frame.grid(row=1, column=1)
oito=tk.Button(text='8', master=oito_frame, command=put_8)
oito.pack()

nove_frame=tk.Frame(relief=tk.RAISED, borderwidth=1)
nove_frame.grid(row=1, column=2)
nove=tk.Button(text='9', master=nove_frame, command=put_9)
nove.pack()

#2.4.2: Botões de operadores matemáticos
mais_ou_menos_frame=tk.Frame(relief=tk.RAISED, borderwidth=1)
mais_ou_menos_frame.grid(row=4, column=4)
mais_ou_menos_frame=tk.Button(text='+\-', master=mais_ou_menos_frame, command=plus_minus)
mais_ou_menos_frame.pack()

raiz_frame=tk.Frame(relief=tk.RAISED, borderwidth=1)
raiz_frame.grid(row=3, column=4)
raiz=tk.Button(text='√', master=raiz_frame, command=lambda: square_root(parcela1))
raiz.pack()


mais_frame=tk.Frame(relief=tk.RAISED, borderwidth=1)
mais_frame.grid(row=1, column=3)
mais=tk.Button(text='+', master=mais_frame, command=lambda: add(parcela1))
mais.pack()

menos_frame=tk.Frame(relief=tk.RAISED, borderwidth=1)
menos_frame.grid(row=2, column=3)
menos=tk.Button(text='-', master=menos_frame, command=lambda: subtract(parcela1))
menos.pack()

mult_frame=tk.Frame(relief=tk.RAISED, borderwidth=1)
mult_frame.grid(row=3, column=3)
mult=tk.Button(text='x', master=mult_frame, command=lambda: multiply(parcela1))
mult.pack()

div_frame=tk.Frame(relief=tk.RAISED, borderwidth=1)
div_frame.grid(row=4, column=3)
div=tk.Button(text='/', master=div_frame, command=lambda: divide(parcela1))
div.pack()

ponto_frame=tk.Frame(relief=tk.RAISED, borderwidth=1)
ponto_frame.grid(row=4, column=2)
ponto=tk.Button(text='.', master=ponto_frame, command=put_point)
ponto.pack()

igual_frame=tk.Frame(relief=tk.RAISED, borderwidth=1)
igual_frame.grid(row=4, column=1)
igual=tk.Button(text='=', master=igual_frame, command=lambda: show_result(parcela1, parcela2))
igual.pack()
 
#2.4.3: Botão de ligar e desligar

ce_frame=tk.Frame(relief=tk.RAISED, borderwidth=1)
ce_frame.grid(row=1, column=4)
ce=tk.Button(text='CE', master=ce_frame, bg='orange', fg='black', command=clean)
ce.pack()

off_frame=tk.Frame(relief=tk.RAISED, borderwidth=1)
off_frame.grid(row=2, column=4)
off=tk.Button(text='OFF', master=off_frame, bg='red', fg='white', command=sair)
off.pack()

#3:Exibindo a janela
janela.mainloop()
