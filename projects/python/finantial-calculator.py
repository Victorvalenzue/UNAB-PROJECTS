# CALCULADORA FINANCIERA
# AUTOR Víctor Valenzuela Román y Heinz Schmidt Cifuentes 
# VERSION 1.0.0
# FECHA 22/08/2021

# CONSTANTES
INPUT_MAX_LENGTH = 22
ENTRY_VALUE = "\033[95m Ingrese valor de entrada: \033[0m"
MAX_LENGTH_ERROR = "Error: valor de entrada debe contener: " + str(INPUT_MAX_LENGTH) + " caracteres y tiene: "
PARSE_ERROR = "Error: No fue posible convertir los valores"
INVALID_OPTION_ERROR = "Error: opción ingresada no es válida. Opciones disponibles: 1 al 5"
INVALID_INT_ERROR = "Error: valor ingresado no es válido. Ingrese valor entero \n"
SELECT_OPTION = "\n----Seleccione una opción----\n"
MENU_OPTION_ONE = "1.- Indicador de UF y Dólar"
MENU_OPTION_TWO = "2.- Cálculo de UF"
MENU_OPTION_THREE = "3.- Cálculo de Dólar"
MENU_OPTION_FOUR = "4.- Cálculo de Valor Futuro"
MENU_OPTION_FIVE = "5.- Salir\n"
ENTER_OPTION = "** Ingrese opción: "
DOLAR_VALUE = "El valor deL Dólar es: $"
UF_VALUE = "El valor de la UF es: "
ASK_UF_INPUT = "** Por Favor ingresa un monto en UF: "
ASK_DOLAR_INPUT = "** Por Favor ingresa un monto en DOLAR: "
ASK_PESOS_INPUT = "** Por Favor ingresa el valor Presente de un monto en Pesos: "
ASK_PERIOD_INPUT = "** Por favor Ingresa el periodo en Meses: "
VALUE_TO_PESOS = "El valor equivalente en Pesos es: $"
VALUE_FUTURE_PESOS = "El valor futuro equivalente en Pesos es: $"
VALUE_FUTURE_UF = "El valor futuro equivalente en UF es: "
VALUE_FUTURE_DOLAR = "El valor futuro equivalente en DOLAR es: $"
EXIT_MESSAGE = "\n¡Gracias, Hasta pronto! 👋\n"

# FUNCIONES
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
  bold(MENU_OPTION_THREE)
  bold(MENU_OPTION_FOUR)
  bold(MENU_OPTION_FIVE)
  
def futureValue(present, rate, period):
  return present * ((1+rate)**period)

# EJEMPLO DE ENTRADA 2021071929747097487052
inputText = input(ENTRY_VALUE)
inputLen = len(inputText)

if(inputLen != INPUT_MAX_LENGTH):
  error(MAX_LENGTH_ERROR + str(inputLen))
  exit()

try:
  year = inputText[0:4]
  month = inputText[4:6]
  day = inputText[6:8]
  absoluteUF = inputText[8:13]
  ufDecimal = inputText[13:15]
  uf = float(absoluteUF + "." + ufDecimal)
  absoluteDolar = inputText[15:18]
  dolarDecimal = inputText[18:20]
  dolar = float(absoluteDolar + "." + dolarDecimal)
  absoluteRate = inputText[20:21]
  rateDecimal = inputText[21]
  rate = float(absoluteRate + "." + rateDecimal)
  percentRate = rate / 100
except:
  error(PARSE_ERROR)
  exit()
  
# BLOQUE PRINCIPAL
selectedOption = 0

while(selectedOption != 5):
  try:
    menu()

    userInput = int(input(ENTER_OPTION))
    
    if(userInput > 0 and userInput < 6):
      selectedOption = userInput
      
      if(selectedOption == 1):  
        ok(UF_VALUE + '{:.2f}'.format(uf) + 'UF')
        ok(DOLAR_VALUE + '{:.2f}'.format(dolar))

      elif(selectedOption == 2):
        try:
          ufInput = int(input(ASK_UF_INPUT))
          ufToPesos = ufInput * uf
          
          ok(VALUE_TO_PESOS + '{:.2f}'.format(ufToPesos))
          
        except:
          warning(INVALID_INT_ERROR) 

      elif(selectedOption == 3):
        try:
          dolarInput = int(input(ASK_DOLAR_INPUT))
          dolarToPesos = dolarInput * dolar
          
          ok(VALUE_TO_PESOS + '{:.2f}'.format(dolarToPesos))
          
        except:
          warning(INVALID_INT_ERROR)   

      elif(selectedOption == 4):     
        try:
          presentValue = int(input(ASK_PESOS_INPUT))
          period = int(input(ASK_PERIOD_INPUT))
          
          future = futureValue(presentValue, percentRate, period)
          futureUF = future / uf
          futureDolar = future / dolar

          ok(VALUE_FUTURE_PESOS + '{:.2f}'.format(future))
          ok(VALUE_FUTURE_UF + '{:.2f}'.format(futureUF))
          ok(VALUE_FUTURE_DOLAR + '{:.2f}'.format(futureDolar))
  
        except:
          warning(INVALID_INT_ERROR)     
    
      else:
        bold(EXIT_MESSAGE)
    else:
      error(INVALID_OPTION_ERROR)
  except:
    error(INVALID_OPTION_ERROR)