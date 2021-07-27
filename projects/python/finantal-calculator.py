INPUT_MAX_LENGTH = 22
MAX_LENGTH_ERROR = "Error: valor de entrada debe contener: " + str(INPUT_MAX_LENGTH) + " caracteres y tiene:"
PARSE_ERROR = "Error: No fue posible convertir los valores"
INVALID_OPTION_ERROR = "Error: opción ingresada no es válida. Opciones disponibles: 1 al 5"
SELECT_OPTION = "----Seleccione una opción----\n"
MENU_OPTION_ONE = "1.- Indicador de UF y Dólar"
MENU_OPTION_TWO = "2.- Cálculo de UF"
MENU_OPTION_THREE = "3.- Cálculo de Dólar"
MENU_OPTION_FOUR = "4.- Cálculo de Valor Futuro"
MENU_OPTION_FIVE = "5.- Salir\n"
ENTER_OPTION = "Ingrese opción: "
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
        print(selectedOption)
      elif(selectedOption == 2):
        print(selectedOption)
      elif(selectedOption == 3):
        print(selectedOption)
      elif(selectedOption == 4):
        print(selectedOption)
      else:
        print(EXIT_MESSAGE)
        exit()
    else:
      print(INVALID_OPTION_ERROR)
  except:
    print(INVALID_OPTION_ERROR)