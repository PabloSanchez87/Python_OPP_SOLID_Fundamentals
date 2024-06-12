## IMPORTAR ARCHIVOS CON NUMPY
import numpy as np

# Escribir con numpy.
# Crear datos de ejemplo.
data = np.array([[1,2,3],[4,5,6],[7,8,9]])   
# Guardar datos en un archivo CSV
np.savetxt("/home/pablost/Python_OPP_SOLID_Fundamentals/Python_Fundamentals/Ficheros/datos.csv", 
           data, delimiter=",")
# Guardar datos en un archivo de texto.
np.savetxt("/home/pablost/Python_OPP_SOLID_Fundamentals/Python_Fundamentals/Ficheros/datos.txt",
           data)
# Guardar datos en un archivo con encabezados.
header = "columna1,columna2,columna3"
np.savetxt("/home/pablost/Python_OPP_SOLID_Fundamentals/Python_Fundamentals/Ficheros/datos2.csv",
           data, delimiter=",", header=header, comments="")

# Leer datos de un arhivo CSV
data_csv = np.loadtxt("/home/pablost/Python_OPP_SOLID_Fundamentals/Python_Fundamentals/Ficheros/datos.csv",
                      delimiter=",")
# Leer datos de un archivo de texto
data_txt = np.loadtxt('/home/pablost/Python_OPP_SOLID_Fundamentals/Python_Fundamentals/Ficheros/datos.txt')
# Leer datos de un archivo con encabezados.
data_csv_header = np.genfromtxt("/home/pablost/Python_OPP_SOLID_Fundamentals/Python_Fundamentals/Ficheros/datos2.csv",
                                delimiter=",",skip_header=1)

print("Datos desde CSV sin encabezados:\n", data_csv)
print("Datos desde archivo de texto:\n", data_txt)
print("Datos desde CSV con encabezados:\n", data_csv_header)

print("·"*40)