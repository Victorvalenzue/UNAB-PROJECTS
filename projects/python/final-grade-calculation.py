TAMANIO_INPUT = 28
NOTA_EXIMIR = 5
inputUsuario = input('Favor ingrese string: ')

if len(inputUsuario) != TAMANIO_INPUT:
  print('Lo sentimos, no podemos trabajar así. Tamaño requerido: ', TAMANIO_INPUT)
  exit()
  
try:
  anio = inputUsuario[0:4]
  mes = inputUsuario[4:6]
  dia = inputUsuario[6:8]
  porcentajeUno = float(inputUsuario[8:10])
  notaUno = float(int(inputUsuario[10:12]) / 10)
  porcentajeDos = float(inputUsuario[12:14])
  notaDos = float(int(inputUsuario[14:16]) / 10)
  porcentajeTarea = float(inputUsuario[16:18])
  tarea = float(int(inputUsuario[18:20]) / 10)
  porcentajeActividad = float(inputUsuario[20:22])
  notaActividad = float(int(inputUsuario[22:24]) / 10)
  porcentajeEDX = float(inputUsuario[24:26])
  notaEDX = float(int(inputUsuario[26:28]) / 10)

  print('Con fecha ', dia, '/', mes, '/', anio, '\n')
  print('Nota Solemne1 que corresponde al ', porcentajeUno ,'porciento la nota es ', notaUno, '\n')
  print('Nota Solemne2 que corresponde al ', porcentajeDos ,'porciento la nota es ', notaDos, '\n')
  print('Nota de Tarea que corresponde al ', porcentajeTarea ,'porciento la nota es ', tarea, '\n')
  print('Nota de Actividades que corresponde al ', porcentajeActividad ,'porciento la nota es ', notaActividad, '\n')
  print('Nota de EDX que corresponde al ', porcentajeEDX ,'porciento la nota es ', notaEDX, '\n')
  
  notaUnoFinal = notaUno * porcentajeUno
  notaDosFinal = notaDos * porcentajeDos
  notaTareaFinal = tarea * porcentajeTarea
  notaActividadFinal = notaActividad * porcentajeActividad
  edxFinal = notaEDX * porcentajeEDX
  notaFinal = (notaUnoFinal + notaDosFinal + notaTareaFinal + notaActividadFinal + edxFinal) / 100
  notaPresentacion = round(notaFinal, 1)
  
  print('La nota de presentación corresponde a: ', notaPresentacion, '\n')
  
  if notaPresentacion >= NOTA_EXIMIR:
    print('Felicitaciones esta eximido') 

except:
  print('Ocurió al obtener valores, intente más tarde')

