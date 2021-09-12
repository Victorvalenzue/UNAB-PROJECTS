# LOTERIA
# AUTOR Víctor Valenzuela Román
# VERSION 1.0.0
# FECHA 12/09/2021

# CONSTANTES
ASK_NUMBER_INPUT = "** Por Favor ingresa un número entero: "
INVALID_OPTION_ERROR = "Error: opción ingresada no es válida. Opciones disponibles: 1 al 2"
INVALID_INT_ERROR = "Error: valor ingresado no es válido. Ingrese valor entero \n"
REPEATED_VALUE_ERROR = "Error: valor ya ingresado \n"
SELECT_OPTION = "\n----Seleccione una opción----\n"
MENU_OPTION_ONE = "1.- Jugar"
MENU_OPTION_TWO = "2.- Salir\n"
ENTER_OPTION = "** Ingrese opción: "
EXIT_MESSAGE = "\n¡Gracias, Hasta pronto! 👋\n"

# IMPORTS
from random import sample
from random import randint

# FUNCIONES UTILITARIAS
def ok(message):
  print('\033[92m'+message+'\033[0m')
  
def bold(message):
  print('\033[1m'+message+'\033[0m')
  
def warning(message):
  print('\033[93m'+message+'\033[0m')
  
def error(message):
  print('\033[91m'+message+'\033[0m')
  
def menu():
  warning(SELECT_OPTION)
  bold(MENU_OPTION_ONE)
  bold(MENU_OPTION_TWO)
  
# BLOQUE PRINCIPAL
lotoList = []

while len(lotoList) < 40:
  value = randint(1, 100)
  try:
    lotoList.index(value)
  except:
    lotoList.append(value)

attempts = 0
total = 0
selectedOption = 0

while(selectedOption != 2):
  try:
    menu()
    userInput = int(input(ENTER_OPTION))
    
    if userInput > 0 and userInput < 3:
      selectedOption = userInput
      
      if selectedOption == 1:
        attempts += 1
        winnerNumbers = sample(lotoList, 6)
        print(winnerNumbers)
        userNumbers = []
        prize = 0
        points = 0

        while len(userNumbers) < 6:        
          try:
            value = int(input(ASK_NUMBER_INPUT)) 
          except:
            warning(INVALID_INT_ERROR)
  
          try:
            userNumbers.index(value)          
            warning(REPEATED_VALUE_ERROR)
          except:
            userNumbers.append(value)

        for i in range(len(winnerNumbers)):
          for j in range(len(userNumbers)):
            if winnerNumbers[i] == userNumbers[j]:
                points += 1

        if points == 3:
          prize += 1770
        if points == 4:
          prize += 9080
        if points == 5:
          prize += 294440
        if points == 6:
          prize += 272279360
          
        total += prize
        
        warning('Los números ganadores: ' + str(winnerNumbers))  
        bold('Cantidad de aciertos: ' + str(points))
        bold('Ganancia actual: $' + str(prize))
        
        
        bold('Total de intentos: ' + str(attempts))
        ok('Total de ganancias: $' + str(total))
      else:
        bold(EXIT_MESSAGE)
    else:
      error(INVALID_OPTION_ERROR)
  except:
    error(INVALID_OPTION_ERROR)