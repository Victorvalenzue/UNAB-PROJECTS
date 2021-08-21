# CALCULADORA FINANCIERA
# AUTOR Víctor Valenzuela
# VERSION 1.0.0
# FECHA 20/08/2021

# BLOQUE DE DEFINICIONES - VARIABLES GLOBALES
# Ejemplo de entrada: 2021071929747097487052
entrada = input('Ingrese valor de entrada: ')
largo = len(entrada)

if(largo != 22):
  print('Ha ocurrido un error: utilice input con 22 caracteres')
  exit()

try:
  # año
  anio = entrada[0:4]
  # mes
  mes = entrada[4:6]
  # dia
  dia = entrada[6:8]
  # uf
  uFEntera = entrada[8:13]
  uFDecimal = entrada[13:15]
  uf = float(uFEntera + "." + uFDecimal)
  # dolar
  dolarEntero = entrada[15:18]
  dolarDecimal = entrada[18:20]
  dolar = float(dolarEntero + "." + dolarDecimal)
  # interes
  interesEntero = entrada[20:21]
  interesDecimal = entrada[21]
  interes = float(interesEntero + "." + interesDecimal)
  porcentajeInteres = interes / 100
  
except:
  print('Ha ocurrido un error al procesar los datos de entrada')
  exit()

# FUNCIONES
def Menu():
  print("1. Indicador de UF y Dólar")
  print("2. Calculo de UF")
  print("3. Calculo de Dólar")
  print("4. Calculo de Valor Futuro")
  print("5. Salir")

# BLOQUE PRINCIPAL
opcion = 0
salida = 10
while(opcion != 5):
  Menu()
  
  try:
    opcion = int(input('Ingrese una opción: '))
    
    if opcion == 5:
      print('Seleccionó salir')
      
    if opcion == 1:
      # Mostrar el valor de la UF y del Dólar a la fecha ingresada, por ejemplo
      # Para el día 20210719
      # El valor de la UF es: 29747.09
      # El valor del Dólar es: 748.70
      print('El valor de la UF es: ', uf)
      print('El valor del Dólar es: ', dolar)
    if opcion == 2:
      # Mostrar el cálculo en pesos al ingresar un monto en UF, por ejemplo
      # Por Favor ingresa un monto en UF: 200
      # El valor equivalente en Pesos es: 5949418,00
      ufEntrada = 0
      while(ufEntrada == 0):
        try:
          ufEntrada = int(input('Por Favor ingresa un monto en UF: '))
        except:
          print('Ingrese monto uf válido')
      
      print('El valor equivalente en Pesos es: $', '{:.2f}'.format(ufEntrada * uf))
    if opcion == 3:
      # Mostrar el cálculo en pesos al ingresar un monto en DOLAR, por ejemplo
      # Por Favor ingresa un monto en DOLAR: 15
      # El valor equivalente en Pesos es: 11230.50
      dolarEntrada = 0
      while(dolarEntrada == 0):
        try:
          dolarEntrada = int(input('Por Favor ingresa un monto en DOLAR: '))
        except:
          print('Ingrese monto dolar válido')
      
      print('El valor equivalente en Pesos es: $', '{:.2f}'.format(dolarEntrada * dolar))
    if opcion == 4:
      # Mostrar el cálculo en pesos, UF y Dólar al ingresar un monto (Valor Presente) en Pesos,
      # por ejemplo:
      # Por Favor ingresa el valor Presente de un monto en Pesos: 1000000
      # Por favor Ingresa el periodo en Meses: 2
      valorPresente = 0
      while(valorPresente == 0):
        try:
          valorPresente = int(input('Por Favor ingresa el valor Presente de un monto en Pesos: '))
        except:
          print('Ingrese monto pesos válido')

      periodo = 0
      while(periodo == 0):
        try:
          periodo = int(input('Por favor Ingresa el periodo en Meses: '))
        except:
          print('Ingrese periodo válido')
      # El valor futuro equivalente en Pesos es: 1106704,00
      # El valor futuro equivalente en UF es: 37,20
      # El valor futuro equivalente en DOLAR es: 1478,16
      
      # Nota: La fórmula del valor futuro está dada por:
      # VF = VP * (1+i)^n
      # Donde:
      # VF=Valor Futuro
      # VP=Valor Presente
      # I= interés
      # n=periodo en meses    
      valorFuturo = valorPresente * ((1+porcentajeInteres)**periodo)
      valorEnUF = valorFuturo / uf
      valorEnDolares = valorFuturo / dolar

      print('El valor futuro equivalente en Pesos es: $', '{:.2f}'.format(valorFuturo))
      print('El valor futuro equivalente en UF es: ', '{:.2f}'.format(valorEnUF))
      print('El valor futuro equivalente en DOLAR es: ', '{:.2f}'.format(valorEnDolares))
  except:
    print('Opción inválida')

#SALIDAS
print('Hasta pronto')
