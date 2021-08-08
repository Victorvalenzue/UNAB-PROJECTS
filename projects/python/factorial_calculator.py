resultadoFactorial = 1

try:
    numero = int(input("ingrese número para el factorial: "))
except:
    print("Ingrese un valor númerico entero")
    exit()

if numero < 0:
  print("no se puede calcular factorial")
  exit()

if numero == 0:
  print("el factorial de cero es 1")
  exit()

for aMultiplicar in range(1,numero + 1):
    resultadoFactorial = resultadoFactorial * aMultiplicar

print("El factorial del número ", numero ,"corresponde a ", resultadoFactorial)