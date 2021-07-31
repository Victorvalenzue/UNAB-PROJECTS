INPUT_MAX_LENGTH = 22
MAX_LENGTH_ERROR = "Error: valor de entrada debe contener: " + str(INPUT_MAX_LENGTH) + " caracteres y tiene:"
PARSE_ERROR = "Error: No fue posible convertir los valores"
INVALID_OPTION_ERROR = "Error: opción ingresada no es válida. Opciones disponibles: 1 al 5"
INVALID_INT_ERROR = "Error: valor ingresado no es válido. Ingrese valor entero \n"
SELECT_OPTION = "----Seleccione una opción----\n"
MENU_OPTION_ONE = "1.- Indicador de UF y Dólar"
MENU_OPTION_TWO = "2.- Cálculo de UF"
MENU_OPTION_THREE = "3.- Cálculo de Dólar"
MENU_OPTION_FOUR = "4.- Cálculo de Valor Futuro"
MENU_OPTION_FIVE = "5.- Salir\n"
ENTER_OPTION = "Ingrese opción: "
DOLAR_VALUE = "El valor deL Dólar es: "
UF_VALUE = "El valor de la UF es: "
ASK_UF_INPUT = "Por Favor ingresa un monto en UF: "
ASK_DOLAR_INPUT = "Por Favor ingresa un monto en DOLAR: "
ASK_PESOS_INPUT = "Por Favor ingresa el valor Presente de un monto en Pesos: "
ASK_PERIOD_INPUT = "Por favor Ingresa el periodo en Meses: "
VALUE_TO_PESOS = "El valor equivalente en Pesos es: "
VALUE_FUTURE_PESOS = "El valor futuro equivalente en Pesos es: "
VALUE_FUTURE_UF = "El valor futuro equivalente en UF es: "
VALUE_FUTURE_DOLAR = "El valor futuro equivalente en DOLAR es: "
EXIT_MESSAGE = "\n¡Gracias, Hasta pronto!\n"

inputText = '2021071929747097487052'
inputLen = len(inputText)

if(inputLen != INPUT_MAX_LENGTH):
  print(MAX_LENGTH_ERROR, inputLen)
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
except:
  print(PARSE_ERROR)
  exit()
  
selectedOption = 0

while(selectedOption != 5):
  print(SELECT_OPTION)
  print(MENU_OPTION_ONE)
  print(MENU_OPTION_TWO)
  print(MENU_OPTION_THREE)
  print(MENU_OPTION_FOUR)
  print(MENU_OPTION_FIVE)
    
  try:
    userInput = int(input(ENTER_OPTION))
    
    if(userInput > 0 and userInput < 6):
      selectedOption = userInput
      
      if(selectedOption == 1):  
        print(UF_VALUE, uf, "\n")
        print(DOLAR_VALUE, dolar)

      elif(selectedOption == 2):
        try:
          ufInput = int(input(ASK_UF_INPUT))
          ufToPesos = ufInput * uf
          
          print(VALUE_TO_PESOS, ufToPesos)
          
        except:
          print(INVALID_INT_ERROR)

      elif(selectedOption == 3):
        try:
          dolarInput = int(input(ASK_DOLAR_INPUT))
          dolarToPesos = dolarInput * dolar
          
          print(VALUE_TO_PESOS, dolarToPesos)
          
        except:
          print(INVALID_INT_ERROR)  

      elif(selectedOption == 4):     
        try:
          # Mostrar el cálculo en pesos, UF y Dólar
          
          # al ingresar un monto (Valor Presente) en Pesos, por ejemplo: 
          # Por Favor ingresa el valor Presente de un monto en Pesos: 1000000
          # Por favor Ingresa el periodo en Meses: 2
          pesosInput = int(input(ASK_PESOS_INPUT))
          print(pesosInput)

          # El valor futuro equivalente en Pesos es: 1106704,00
          # El valor futuro equivalente en UF es: 37,20
          # El valor futuro equivalente en DOLAR es: 1478,16
          
          # Nota: La fórmula del valor futuro está dada por:
          # VF = VP * (1+ i)^n
          
          # Donde:
          # VF= Valor Futuro 
          # VP= Valor Presente 
          # I= interés
          # n= periodo en meses
  
        except:
          print(INVALID_INT_ERROR)     
    
      else:
        print(EXIT_MESSAGE)
        exit()
    else:
      print(INVALID_OPTION_ERROR)
  except:
    print(INVALID_OPTION_ERROR)