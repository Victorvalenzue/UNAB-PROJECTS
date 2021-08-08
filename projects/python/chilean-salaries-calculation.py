UF = 	29764.36
TOPE_IMPONIBLE_SALUD = 80.2 * UF
DESCUENTO_MAXIMO_SALUD = TOPE_IMPONIBLE_SALUD * 0.07
TOPE_IMPONIBLE_CESANTIA = 122.7 * UF
DESCUENTO_MAXIMO_CESANTIA = TOPE_IMPONIBLE_CESANTIA * 0.03
opcion = 's'

while opcion == 's' or opcion == 'S':
  try:
    sueldo = int(input('Ingrese sueldo: '))
    afp = input('Ingrese AFP: ').upper()   
    descuentoAfp = sueldo * 0.1
    comision = 0.0
    
    if afp == 'CAPITAL':
      comision = 1.44
    elif afp == 'CUPRUM':
      comision = 1.44
    elif afp == 'HABITAT':
      comision = 1.27
    elif afp == 'MODELO':
      comision = 0.77
    elif afp == 'PLANVITAL':
      comision = 1.16
    elif afp == 'PROVIDA':
      comision = 1.451
    elif afp == 'UNO':
      comision = 0.69
    else:
      print('AFP ingresa no se reconoce')
      exit()
    
    descuentoComision = sueldo * comision / 100
    totalAfp = descuentoAfp + descuentoComision
    
    if sueldo > TOPE_IMPONIBLE_SALUD:
      salud = sueldo * DESCUENTO_MAXIMO_SALUD
    else:
      salud = sueldo * 0.07

    if sueldo > TOPE_IMPONIBLE_CESANTIA:
      cesantia = DESCUENTO_MAXIMO_CESANTIA
      porcentajeEmpleado = TOPE_IMPONIBLE_CESANTIA * 0.06
    else:
      cesantia = sueldo * 0.03
      porcentajeEmpleado = sueldo * 0.006
    
    cesantiaEmpleador = cesantia - porcentajeEmpleado
    liquido = sueldo - totalAfp - porcentajeEmpleado - salud
    factor = 0
    if liquido <= 704875.50:
      factor = 0
    elif liquido > 704875.50 and liquido <= 1566390:
      factor = 0.0004
    elif liquido > 1566390 <= 2610650:
      factor = 0.0008
    elif liquido > 2610650 <= 3654910:
      factor = 0.00135
    elif liquido > 3654910 <= 4699170:
      factor = 0.0023
    elif liquido > 4699170 <= 6265560:
      factor = 0.00304
    elif liquido > 6265560 <= 16186030:
      factor = 0.0035
    elif liquido > 16186030:
      factor = 0.004
    else:
      print('no fue posible calcular Factor')
      exit()
      
    segundaCatergoria = sueldo * factor
    sueldoFinal = liquido - segundaCatergoria
    
    print('Pago a AFP: ', descuentoAfp, '\n')
    print('Comisión AFP: ', descuentoComision, '\n')
    print('Pago a ISAPRE/FONADA: ', salud, '\n')
    print('Seguro de cesantía empleado: ', porcentajeEmpleado, '\n')
    print('Seguro de cesantía empleador: ', cesantiaEmpleador, '\n')
    print('Sueldo líquido imponible: ', liquido, '\n')
    print('Impuesto único segunda categoría a pagar: ', segundaCatergoria, '\n')
    print('Sueldo líquido a pagar: ', sueldoFinal, '\n')
    
    opcion = input('¿Desea realizar otro cálculo? Ingrese S o s si lo desea ')
  except:
    print('Input incorrectos intente nuevamente')
    
print('Hasta pronto!')

