from traceback import print_tb
from turtle import st
import matplotlib.pyplot as plt
import csv
import math
import operator
import numpy
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.lines import Line2D

class Algoritmo:

    def __init__(self):
        self.x = []
        self.y = []
        self.clase = []
        self.contador=0
        self.colormap=[]
        self.k=0
        self.matrizDistancia=[]
        self.clasesCalculadas=[]
        self.listaK=[]
        self.listaKPonderado=[]
        self.grafico=None
        self.cantClases=[]
        self.listaLeyendas=[]
        self.contadorClase1=0
        self.contadorClase2=0
        self.contadorClase0=0
        self.listaAciertosXClases=[]
        for a in range(600):
            self.listaAciertosXClases.append([0,0,0,0,0,0])

    def limpiarDatos(self):
        self.x = []
        self.y = []
        self.clase = []
        self.contador=0
        self.colormap=[]
        self.k=0
        self.nuevoPunto=[]
        self.distanciasOrdenadas=[]
        self.vecino=[]
        self.vecinoPonderado=[]
        self.matrizDistancia=[]
        self.clasesCalculadas=[]
    
    #Lee el csv y guarda los datos en las listas x, y, clase
    def leerArchivo(self,nombreArchivo):
        with open(nombreArchivo, 'r') as file:
            plots = csv.reader(file, delimiter = ',')
            for row in plots:
                self.contador=self.contador+1
                if(self.contador!=1):
                    self.x.append(float(row[0]))
                    self.y.append(float(row[1]))
                    self.clase.append(float(row[2]))
                    if(self.clase[self.contador-2]==0):
                        self.contadorClase0+=1
                    if(self.clase[self.contador-2]==1):
                        self.contadorClase1+=1
                    if(self.clase[self.contador-2]==2):
                        self.contadorClase2+=1
        print(self.contadorClase0)
        print(self.contadorClase1)
        print(self.contadorClase2)
                    
        
    def obtenerKOptimo(self):
        for a in range(self.contador-1):
            self.listaK.append(0)
        for a in range(self.contador-1):
            vecinos={}
            self.cantClases.append(vecinos)
        bandera=False
        for i in range(1,self.contador-1):
            self.k=i
            for fila in range(self.contador-1):
                resultadoClase = self.obtenerClaseNuevoPunto(fila)
                if(len(resultadoClase)>1):
                    if(resultadoClase[0][1]==resultadoClase[1][1]):
                        bandera=False
                    else:
                        bandera=True
                else:
                    bandera=True
                if(resultadoClase[0][0]==self.clase[fila] and bandera):
                    self.listaK[i-1] = self.listaK[i-1] + 1
                    if(self.clase[fila]==0):
                        self.listaAciertosXClases[self.k-1][0]+=1
                    if(self.clase[fila]==1):
                        self.listaAciertosXClases[self.k-1][2]+=1
                    if(self.clase[fila]==2):
                        self.listaAciertosXClases[self.k-1][4]+=1
                bandera=False
            self.listaAciertosXClases[self.k-1][1]=self.contadorClase0-self.listaAciertosXClases[self.k-1][0]
            self.listaAciertosXClases[self.k-1][3]=self.contadorClase1-self.listaAciertosXClases[self.k-1][2]
            self.listaAciertosXClases[self.k-1][5]=self.contadorClase2-self.listaAciertosXClases[self.k-1][4]
            #print(i)
        #print(self.listaK)
        print(self.listaAciertosXClases)
        max_value = max(self.listaK)
        print('Maximum value:', max_value, "At index:", self.listaK.index(max_value)+1)
        return self.listaK.index(max_value)+1

    def obtenerKOptimoKnnPonderado(self):
        for a in range(self.contador-1):
            self.listaKPonderado.append(0)
        self.cantClases.clear()
        for a in range(self.contador-1):
            vecinos={}
            self.cantClases.append(vecinos)
        bandera=False
        for i in range(1,self.contador-1):
            self.k=i
            for fila in range(self.contador-1):
                resultadoClase = self.obtenerClaseNuevoPuntoPonderado(fila)
                if(len(resultadoClase)>1):
                    if(resultadoClase[0][1]==resultadoClase[1][1]):
                        bandera=False
                    else:
                        bandera=True
                else:
                    bandera=True
                if(resultadoClase[0][0]==self.clase[fila] and bandera):
                    self.listaKPonderado[i-1] = self.listaKPonderado[i-1] + 1
                bandera=False
            #print(i)
        #print(self.listaKPonderado)
        max_value = max(self.listaKPonderado)
        print('Maximum value:', max_value, "At index:", self.listaKPonderado.index(max_value)+1)
        return self.listaKPonderado.index(max_value)+1

    
    def calcularMatrizDistancias(self):
        self.matrizDistancia =  [ [ None for y in range(self.contador-1) ] for x in range( self.contador-1) ]   
        for fila in range(self.contador-1):       
            for columna in range(fila,self.contador-1):
                if(fila==columna):
                    self.matrizDistancia[fila][columna]=[0]
                else:
                    self.matrizDistancia[fila][columna]=[math.sqrt(((self.x[fila]-self.x[columna])**2+(self.y[fila]-self.y[columna])**2)),self.x[columna],self.y[columna],self.clase[columna]]
                    self.matrizDistancia[columna][fila]=[self.matrizDistancia[fila][columna][0],self.x[fila],self.y[fila],self.clase[fila]]
                    #self.matrizDistancia[fila][columna]
        #for fila in self.matrizDistancia:
        #    for valor in fila:
        #        print("\t", valor, end=" ")
        #print()
        print("------------------------------------------------")
        contadorAuxiliar=1
        filaAOrdenar=[]
        for fila in range(self.contador-1):
            for aux in range(self.contador-1):
                filaAOrdenar.append(self.matrizDistancia[fila][aux])
            filaOrdenada = sorted(filaAOrdenar, key=lambda x:x[0])
            for auxiliarOrdenar in range(len(filaOrdenada)):
                self.matrizDistancia[fila] = filaOrdenada
                #self.matrizDistancia[auxiliarOrdenar+contadorAuxiliar][columna]= -1
                #self.matrizDistancia[columna][auxiliarOrdenar+contadorAuxiliar]
            filaAOrdenar=[]
            contadorAuxiliar=contadorAuxiliar+1
        #for fila in self.matrizDistancia:
        #    for valor in fila:
        #        print("\t", valor, end=" ")
        #    print()
        print("++++++++++++++++++++++++++++++++++++++++++++")

    #Define el mapa de colores para el grafico, habria que hacerlo mas general porque ahora esta hecho para 3 clases
    def definirMapaDeColores(self):
        self.colormap.clear()
        self.listaLeyendas.clear()
        contador=0
        leyendaRoja=Line2D([0], [0], marker='o', color='w', label='Clase 0', markerfacecolor='red', markersize=12)
        leyendaVerde=Line2D([0], [0], marker='o', color='w', label='Clase 1', markerfacecolor='green',markersize=12)
        leyendaAzul=Line2D([0], [0], marker='o', color='w', label='Clase 2', markerfacecolor='blue',markersize=12)
        for color in self.clase:
            if(color==0):
                if(self.clasesCalculadas[contador]==0):
                    self.colormap.append('r')
                    if(leyendaRoja not in self.listaLeyendas):
                        self.listaLeyendas.append(leyendaRoja)
                else:
                    self.colormap.append('lightcoral')
            if(color==1):
                if(self.clasesCalculadas[contador]==1):
                    self.colormap.append('g')
                    if(leyendaVerde not in self.listaLeyendas):
                        self.listaLeyendas.append(leyendaVerde)
                else:
                    self.colormap.append('lightgreen')
            if(color==2):
                if(self.clasesCalculadas[contador]==2):
                    self.colormap.append('b')
                    if(leyendaAzul not in self.listaLeyendas):
                        self.listaLeyendas.append(leyendaAzul)
                else:
                    self.colormap.append('cyan')
            contador+=1
        #print(self.colormap)

    #Define el atributo K
    def setK(self,k):
        self.k=k

    #Define de que clase es el nuevo punto ingresado
    def obtenerClaseNuevoPunto(self,fila):
        auxiliar=self.matrizDistancia[fila][self.k][3]
        auxiliarClases=self.cantClases[fila]
        if(auxiliar in auxiliarClases):
            auxiliarClases[auxiliar]+=1
        else:
            auxiliarClases[auxiliar]=1
        vecinoOrdenado = sorted(auxiliarClases.items(), key=operator.itemgetter(1),reverse=True)
        return vecinoOrdenado

    def obtenerClaseNuevoPuntoPonderado(self,fila):
        auxiliar=self.matrizDistancia[fila][self.k][3]
        auxiliarClases=self.cantClases[fila]
        if(auxiliar in auxiliarClases):
            auxiliarClases[auxiliar]+=(1/((self.matrizDistancia[fila][self.k][0])**2))
        else:
            auxiliarClases[auxiliar]=(1/((self.matrizDistancia[fila][self.k][0])**2))
        vecinoOrdenadoPonderado = sorted(auxiliarClases.items(), key=operator.itemgetter(1),reverse=True)
        return vecinoOrdenadoPonderado

    def obtenerNuevaClaseKnn(self,fila):
        vecinos={}
        for cantidadK in range(self.k):
            auxiliar=self.matrizDistancia[fila][cantidadK+1][3]
            if(auxiliar in vecinos):
                vecinos[auxiliar]+=1
            else:
                vecinos[auxiliar]=1
        vecinoOrdenado = sorted(vecinos.items(), key=operator.itemgetter(1),reverse=True)
        return vecinoOrdenado

    def obtenerNuevaClaseKnnPonderado(self,fila):
        vecinos={}
        for cantidadK in range(self.k):
            auxiliar=self.matrizDistancia[fila][cantidadK+1][3]
            if(auxiliar in vecinos):
                vecinos[auxiliar]+=(1/((self.matrizDistancia[fila][cantidadK+1][0])**2))
            else:
                vecinos[auxiliar]=(1/((self.matrizDistancia[fila][cantidadK+1][0])**2))
        vecinoOrdenadoPonderado = sorted(vecinos.items(), key=operator.itemgetter(1),reverse=True)
        return vecinoOrdenadoPonderado

    #Genera el grafico
    def graficarResultado(self):
        return (self.x,self.y,self.colormap)
    
    def algoritmoKnn(self,k):
        self.setK(k)
        bandera=False
        for a in range(600):
            resultadoClase = self.obtenerNuevaClaseKnn(a)
            if(len(resultadoClase)>1):
                if(resultadoClase[0][1]==resultadoClase[1][1]):
                    bandera=False
                else:
                    bandera=True
            else:
                bandera=True
            if(bandera):
                self.clasesCalculadas.append(self.obtenerNuevaClaseKnn(a)[0][0])
            else:
                self.clasesCalculadas.append(-1)
            bandera=False
        self.definirMapaDeColores()
        return (self.x,self.y,self.colormap,self.listaLeyendas)

    def algoritmoKnnPonderado(self,k):
        self.setK(k)
        self.clasesCalculadas.clear()
        for a in range (600):
            self.clasesCalculadas.append(self.obtenerNuevaClaseKnnPonderado(a)[0][0])
        self.definirMapaDeColores()
        return (self.x,self.y,self.colormap,self.listaLeyendas)

    def limpiarVariables(self):
        self.colormap.clear()
        self.k=0
        self.clasesCalculadas.clear()

    def graficarBarras(self):
        listaAciertos=[]
        listaDeKs=[]
        colores=[]
        for a in range(15):
            listaAciertos.append(self.listaK[a])
            listaDeKs.append(str(a+1))
            colores.append('red')
        if(self.listaK.index(max(self.listaK))>14):
            listaAciertos.append(max(self.listaK))
            listaDeKs.append(str(self.listaK.index(max(self.listaK))+1))
            colores.append('red')
        return (listaAciertos,listaDeKs,colores)

    def graficarBarrasKnnPonderado(self):
        listaAciertos=[]
        listaDeKs=[]
        colores=[]
        for a in range(15):
            listaAciertos.append(self.listaKPonderado[a])
            listaDeKs.append(str(a+1))
            colores.append('red')
        if(self.listaKPonderado.index(max(self.listaKPonderado))>14):
            listaAciertos.append(max(self.listaKPonderado))
            listaDeKs.append(str(self.listaKPonderado.index(max(self.listaKPonderado))+1))
            colores.append('red')
        return (listaAciertos,listaDeKs,colores)