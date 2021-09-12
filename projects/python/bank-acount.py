# CUENTA BANCARIA
# AUTOR Víctor Valenzuela Román
# VERSION 1.0.0
# FECHA 12/09/2021

# CONSTANTES
RUT_ENTRY_VALUE = "\033[95m Ingrese RUT sin puntos, guión ni dígito verificador: \033[0m"
PASSWORD_ENTRY_VALUE = "\033[95m Ingrese contraseña: \033[0m"
ASK_AMOUNT_INPUT = "** Por Favor ingresa un monto: "
INVALID_OPTION_ERROR = "Error: opción ingresada no es válida. Opciones disponibles: 1 al 4"
INVALID_INT_ERROR = "Error: valor ingresado no es válido. Ingrese valor entero \n"
BALANCE_EXCEEDED_ERROR = "Error: no es posible retirar más que el saldo disponible \n"
NOT_FOUND_USER_ERROR = "Error: usuario no encontrado, credenciales incorrectas \n"
SELECT_OPTION = "\n----Seleccione una opción----\n"
ACOUNT_INFORMATION = "\n----Información de la cuenta----\n"
MENU_OPTION_ONE = "1.- Información de la cuenta"
MENU_OPTION_TWO = "2.- Realizar depósito"
MENU_OPTION_THREE = "3.- Realizar retiro"
MENU_OPTION_FOUR = "4.- Salir\n"
ENTER_OPTION = "** Ingrese opción: "
EXIT_MESSAGE = "\n¡Gracias, Hasta pronto! 👋\n"

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
  bold(MENU_OPTION_THREE)
  bold(MENU_OPTION_FOUR)
  
def findByCredentials(list, id, password):
  for user in list:
    if user.rut == id and user.password == password:
      return user
    
# CLASES
class Usuario():
  balance = 0
  name = None
  rut = None
  password = None

  def __init__(self, balance, name, rut, password):
    self.balance = balance
    self.name = name
    self.rut = rut
    self.password = password
      
  def deposit(self, amount):
    self.balance += amount
    ok('Saldo actualizado: $' + str(self.balance))
    
  def withdraw(self, amount):
    if self.balance < amount:
      error(BALANCE_EXCEEDED_ERROR)
      return

    self.balance -= amount
    ok('Saldo actualizado: $' + str(self.balance))
  
  def showInformation(self):
    warning(ACOUNT_INFORMATION)
    bold('Nombre: ' + self.name)
    bold('Saldo: $' + str(self.balance))
      
# USUARIOS DE PRUEBA
usuarioUno = Usuario(500000, 'Carlos Alfredo Gajardo', 12222333, 'password1')
usuarioDos = Usuario(1500000, 'Valeria Florinda Vidal', 16888111, 'password2')
users = [usuarioUno, usuarioDos]

# BLOQUE PRINCIPAL
try:
  rut = int(input(RUT_ENTRY_VALUE))
  password = input(PASSWORD_ENTRY_VALUE)
except:
  error(INVALID_INT_ERROR)
  exit()

founded = findByCredentials(users, rut, password)
if not founded:
  error(NOT_FOUND_USER_ERROR)
  exit()

selectedOption = 0

while(selectedOption != 4):
  try:
    menu()
    userInput = int(input(ENTER_OPTION))
    
    if userInput > 0 and userInput < 5:
      selectedOption = userInput
      
      if selectedOption == 1:  
        founded.showInformation()

      elif selectedOption == 2:
        try:
          amount = int(input(ASK_AMOUNT_INPUT))    
          founded.deposit(amount)       
        except:
          warning(INVALID_INT_ERROR)

      elif selectedOption == 3:
        try:
          amount = int(input(ASK_AMOUNT_INPUT))    
          founded.withdraw(amount)       
        except:
          warning(INVALID_INT_ERROR)
    
      else:
        bold(EXIT_MESSAGE)
    else:
      error(INVALID_OPTION_ERROR)
  except:
    error(INVALID_OPTION_ERROR)