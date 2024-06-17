import csv
import os
import unicodedata

# Función para eliminar tildes y la letra 'ñ'
def eliminar_tildes_y_enie(texto):
    return ''.join((c for c in unicodedata.normalize('NFD', texto) if unicodedata.category(c) != 'Mn'))

# Ruta del archivo CSV original y del archivo limpio
ruta_csv = r'C:\Users\jespinoza\Documents\Jhonny Docs\Python\Limpiar archivo\defunciones2019.csv'
ruta_csv_limpio = r'C:\Users\jespinoza\Documents\Jhonny Docs\Python\Limpiar archivo\defunciones2019_limpio.csv'

# Verificar que el archivo original existe
if not os.path.isfile(ruta_csv):
    print(f'El archivo {ruta_csv} no existe.')
else:
    # Leer el archivo CSV y limpiar las comillas dobles del encabezado
    with open(ruta_csv, newline='', encoding='utf-8') as csvfile:
        reader = csv.reader(csvfile)
        filas = list(reader)
        encabezado = [col.replace('"', '') for col in filas[0]]
        filas[0] = encabezado

        # Recorrer las filas y aplicar limpieza de tildes y 'ñ', y reemplazar valores específicos
        for fila in filas[1:]:
            for i, valor in enumerate(fila):
                # Eliminar tildes y 'ñ'
                fila[i] = eliminar_tildes_y_enie(valor)
                # Reemplazar valores 999, 9999, 99999 por 100
                if fila[i] in ['999', '9999', '99999']:
                    fila[i] = '100'

    # Escribir el archivo CSV limpio
    with open(ruta_csv_limpio, 'w', newline='', encoding='utf-8') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerows(filas)

    print(f'Archivo CSV limpio guardado en {ruta_csv_limpio}')
