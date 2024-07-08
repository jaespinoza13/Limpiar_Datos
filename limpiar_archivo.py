import csv
import os
import unicodedata

# Función para eliminar tildes y la letra 'ñ'
def eliminar_tildes_y_enie(texto):
    return ''.join((c for c in unicodedata.normalize('NFD', texto) if unicodedata.category(c) != 'Mn'))

# Ruta del archivo CSV original y del archivo limpio
ruta_csv = r'C:\UTPL 2024\Scripts Python\limpieza_datos\defunciones2019.csv'
ruta_csv_limpio = r'C:\UTPL 2024\Scripts Python\limpieza_datos\defunciones2019_limpio.csv'

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
        filas_limpias = [filas[0]]  # Mantener el encabezado
        for fila in filas[1:]:
            fila_limpia = []
            eliminar_fila = False
            for i, valor in enumerate(fila):
                # Eliminar tildes y 'ñ'
                valor_limpio = eliminar_tildes_y_enie(valor)
                # Reemplazar valores 999, 9999, 99999 por 100
                if valor_limpio in ['0','999', '9999', '99999']:
                    valor_limpio = '100'
                # Marcar la fila para eliminar si contiene 'Exterior'
                if valor_limpio == 'Exterior':
                    eliminar_fila = True
                fila_limpia.append(valor_limpio)
            if not eliminar_fila:
                filas_limpias.append(fila_limpia)

    # Escribir el archivo CSV limpio
    with open(ruta_csv_limpio, 'w', newline='', encoding='utf-8') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerows(filas_limpias)

    print(f'Archivo CSV limpio guardado en {ruta_csv_limpio}')
