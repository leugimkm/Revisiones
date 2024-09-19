"""
Importaciones
"""
import tkinter as tk
"""
Fin Importaciones
"""
################################# CAPA DE PRESENTACIÓN #########################################
"""
Funciones para eventos
"""
def elemento_seleccionado(seleccion):
    #limpiar_ventana()
    if seleccion == "Circulo":
        vista_circulo()
    elif seleccion == "Triangulo":
        vista_general()
    else: # Si el resto de figuras tiene la misma entradas incluso se puede eliminar el elif anterior, sino habría que ir completando el if con el resto de figuras
        vista_general()
def dato_modificado(evento):
    dato_base = valor_base.get()
    dato_altura = valor_altura.get()
    seleccion = lista.get()
    resultado = calculos(seleccion,dato_base,dato_altura)
    mostrar_resultados(resultado)
"""
Fin Funciones para eventos
"""
"""
Funciones Generales
"""
# Función para mostrar los label y entry generales
def vista_general():
    # Label entry entrada datos 
    base.config(text='Valor de la base')
    base.place(x=400,y=60,width=100,height=20)
    valor_base.place(x=500,y=60,width=210,height=20)
    altura.place(x=400,y=90,width=100,height=20)
    valor_altura.place(x=500,y=90,width=210,height=20)
    # Label entry resultados   
    area.place(x=400,y=120,width=100,height=20)
    valor_area.place(x=500,y=120,width=210,height=20)
    perimetro.place(x=400,y=150,width=100,height=20)
    valor_perimetro.place(x=500,y=150,width=210,height=20)
# Función para limpiar la ventana de entry y label
def vista_circulo():
    vista_general() # Muestro todos los datos
    base.config(text='Valor del radio') # Cambio el testo del label
    #Oculto lo que no me interesa
    altura.place_forget()
    valor_altura.place_forget()
    perimetro.place_forget()
    valor_perimetro.place_forget()
def mostrar_resultados(resultado):
    valor_area.config(text=resultado)
"""
Fin Funciones Generales
"""
"""
Ventana principal
"""
ventana =tk.Tk()
ventana.title("Programa en fase beta")
ventana.resizable(False,True)
ventana.geometry("720x1280")
 
#fondo = tk.PhotoImage(file="fondo.gif")
#fondo = fondo.subsample(1,1)
#fondo1 = tk.Label(image=fondo)
#fondo1.place(x=0,y=0,relwidth=1.0,relheight=1.0)
 
bienvenida = tk.Label(ventana,text=' Bienvenido Kevin')
bienvenida.place(x=280,width=190,height=20)
bienvenida.pack
 
lista = tk.StringVar(ventana)
lista.set('Figura')
 
lista1 = tk.StringVar(ventana)
lista1.set('Método')
 
figuras = ['Circulo','Triangulo','Triangulo rectángulo','Rectángulo']
metodo = ['Trigonométrico','Teorema de Pitágoras']
 
opcion =tk.OptionMenu(ventana,lista,*figuras,command= lambda seleccion: elemento_seleccionado(seleccion))
opcion.config(width=20)
opcion.pack(side='left',padx=30,pady=30)
 
opcion2 =tk.OptionMenu(ventana,lista1,*metodo)
opcion2.config(width=20)
opcion2.pack(side='left',padx=30,pady=30)
 
solicitud = tk.Label(ventana,text='Ingresa los valores conocidos',bg='grey')
solicitud.place(x=530,y=30,width=160,height=20)
#solicitud.pack # No es necesario, ya estamos usando place
 
# Label entry entrada datos 
base = tk.Label(ventana)
valor_base = tk.Entry(ventana)
valor_base.bind("<KeyRelease>", dato_modificado)
altura = tk.Label(ventana,text='Valor de la altura')
valor_altura = tk.Entry(ventana)
valor_altura.bind("<KeyRelease>", dato_modificado)
# Label entry resultados   
area = tk.Label(ventana,text='Valor del área')
valor_area = tk.Label(ventana,text="aquí se muestra el resultado")
perimetro = tk.Label(ventana,text='Valor del perímetro')
valor_perimetro = tk.Label(ventana,text="aquí se muestra el resultado")
 
"""
Fin Ventana principal
"""
################################# CAPA DE TRABAJO #########################################
"""
 Clases
"""
class Figura:
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura
    def area(self):
        return self.base * self.altura
 
#figuras geométricas
class Triangulo(Figura):
    # Sobre escribo el método área y heredo el método __init__
    def area():
        return self.base * self.altura / 2
 
class Circulo(): # No hereda de figura ya que el método init y el método área son diferentes
    def __init__(self, radio):
        self.radio = radio
    def area():
        return 3.14159 * radio ** 2
        
        
class TrianguloRectangulo(Triangulo,Figura):
    def __init__(self):
        pass
 
class Rectangulo(Figura):
    pass # Como el método init y el método área son iguales solo creo la clase sin añadir nada
        
 
#métodos
class Metodo:
    def __init__(self,trigonometrico,teorema):
        self.trigonometrico = trigonometrico
        self.teorema = teorema
"""
 Fin Clases
"""
"""
Funciones Generales
"""
def calculos(figura,valor_base,valor_altura):
    try:
        if valor_base !="" and valor_altura !="":
            valor_base = float(valor_base)
            valor_altura = float(valor_altura)
        if figura == "Circulo":
            circulo = Circulo(valor_base)
            return circulo.area()
        elif figura == "Rectángulo":
            figura = Rectangulo(valor_base,valor_altura)
            return figura.area()
    except:
        pass
 
"""
Fin Funciones Generales
"""
 
ventana.mainloop() # comienza el programa