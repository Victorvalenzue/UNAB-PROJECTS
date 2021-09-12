# GENERADOR MATRIZ
# AUTOR Víctor Valenzuela Román
# VERSION 1.0.0
# FECHA 12/09/2021

# IMPORTS
from random import uniform

# FUNCIONES
def getFileName(name):
  return name + '.txt'

def initMatrix(n,m):
  matrix = []
  for i in range(n):
    a = [0]*m
    matrix.append(a)

  return matrix

def customMatrix(matrix):
  for i in range(len(matrix)):
    for j in range(len(matrix[i])):
      matrix[i][j]=round(uniform(0,100),1)

  return matrix

def showMatrix(matrix):
  print('La matriz es la siguiente: ')
  for row in matrix:
    for value in row:
      print('\t', value, end=' ')

    print()

  return print('Fin de Lectura')
          
def saveFile(matrix, name):
  file = open(name, 'w')
  row = []

  for fila in matrix:
    for valor in fila:
      valor = str(valor)
      row.append(valor)

    line = ' '.join(row)
    file.write(line + '\n')
    row = []
            
  file.close()
  
  return print('Grabacion ok Archivo ' + fileName)

def readFile(fileName):
  file = open(fileName, 'r')
  matrix = file.readlines()
  print('Inicio Lectura de Archivo ' + fileName)

  for line in matrix:
    i = line.split(' ')

    for j in i:
      print('\t', j, end=' ')

  return print('Fin Lectura de Archivo ' + fileName)

# BLOQUE PRINCIPAL
rows = int(input('ingrese N de la matriz: '))
columns = int(input('ingrese M de la matriz: '))
nombre = input('ingrese nombre del archivo: ')
fileName = getFileName(nombre)
matrix = initMatrix(rows, columns)
custom = customMatrix(matrix)

showMatrix(custom)
saveFile(custom, fileName)
readFile(fileName)
