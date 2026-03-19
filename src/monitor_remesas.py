"""
=========================================================
SCRIPT DE MONITOREO DE REMESAS
=========================================================

Descripción:
Este script simula un proceso de monitoreo de remesas.

El programa realiza las siguientes tareas:

1. Lee un archivo de texto (remesas.txt) que contiene
   números de remesa.
2. Lee un archivo de texto (json_data.txt) donde cada
   línea contiene un objeto JSON con información de una
   remesa.
3. Busca cada remesa dentro de los registros JSON.
4. Extrae únicamente dos campos del JSON:
      - step  -> paso actual del proceso
      - cause -> causa del estado
5. Muestra el resultado en pantalla y genera un log.

Estructura esperada del proyecto:

Exam/
│
├── src/
│   └── monitor_remesas.py
│
├── data/
│   ├── remesas.txt
│   └── json_data.txt
│
├── logs/
│   └── reporte_monitoreo.log
│
Autor: Anderson Rivera 
Lenguaje: Python
"""

# ---------------------------------------------------------
# IMPORTACIÓN DE LIBRERÍAS
# ---------------------------------------------------------

import json  # Permite trabajar con archivos JSON
import os    # Permite manejar rutas del sistema operativo


# DEFINICIÓN DE RUTAS DEL PROYECTO

# Obtiene la ruta absoluta del script actual
# __file__ representa la ubicación del archivo python
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Define la carpeta donde se almacenan los datos
DATA_DIR = os.path.join(BASE_DIR, "data")

# Define la carpeta donde se guardarán los logs
LOG_DIR = os.path.join(BASE_DIR, "logs")

# Ruta completa del archivo de remesas
archivo_remesas = os.path.join(DATA_DIR, "remesas.txt")

# Ruta completa del archivo con los JSON
archivo_json = os.path.join(DATA_DIR, "json_data.txt")

# Ruta donde se guardará el log de resultados
archivo_reporte = os.path.join(LOG_DIR, "reporte_monitoreo.log")


# FUNCIÓN: LEER REMESAS

def leer_remesas():
    """
    Lee el archivo remesas.txt y retorna una lista
    con todos los números de remesa.
    """

    try:
        # Abre el archivo en modo lectura
        with open(archivo_remesas, "r", encoding="utf-8") as f:

            # strip() elimina saltos de línea
            return [line.strip() for line in f]

    except FileNotFoundError:

        # Manejo de error si el archivo no existe
        print("Error: No se encontró remesas.txt")

        return []


# FUNCIÓN: LEER JSON

def leer_json():
    """
    Lee el archivo json_data.txt.

    Cada línea del archivo contiene un JSON que
    representa el estado de una remesa.
    """

    datos = []

    try:

        with open(archivo_json, "r", encoding="utf-8") as f:

            # Lee el archivo línea por línea
            for linea in f:

                try:

                    # Convierte el texto en un objeto JSON
                    datos.append(json.loads(linea))

                except json.JSONDecodeError:

                    # Se ejecuta si un JSON está mal formado
                    print("Error: JSON inválido detectado")

    except FileNotFoundError:

        print("Error: No se encontró json_data.txt")

    return datos


# FUNCIÓN: BUSCAR REMESA

def buscar_remesa(remesa, data):
    """
    Busca una remesa dentro de los registros JSON.

    Parámetros:
    remesa -> número de remesa a buscar
    data   -> lista con los registros JSON

    Retorna:
    step y cause si la remesa es encontrada.
    """

    for item in data:

        try:

            # Verifica si el orderId coincide con la remesa
            if item["orderId"]["S"] == remesa:

                # Extrae el paso actual del proceso
                step = item["state"]["M"]["step"]["S"]

                # Extrae la causa del estado
                cause = item["state"]["M"]["cause"]["S"]

                return step, cause

        except KeyError:

            # Se ejecuta si la estructura del JSON cambia
            print("Error en estructura JSON")

    return None, None


# FUNCIÓN: GUARDAR REPORTE

def guardar_reporte(registros):
    """
    Guarda los resultados del monitoreo
    dentro de la carpeta logs.
    """

    # Crea la carpeta logs si no existe
    os.makedirs(LOG_DIR, exist_ok=True)

    with open(archivo_reporte, "w", encoding="utf-8") as f:

        # Escribe cada resultado en una línea del log
        for r in registros:
            f.write(r + "\n")

# FUNCIÓN PRINCIPAL

def ejecutar_monitoreo():
    """
    Ejecuta todo el proceso de monitoreo.
    """

    # Lee remesas desde el archivo
    remesas = leer_remesas()

    # Lee registros JSON
    data = leer_json()

    resultados = []

    # Recorre cada remesa
    for r in remesas:

        # Busca la remesa dentro de los JSON
        step, cause = buscar_remesa(r, data)

        if step:

            # Ahora incluye el número de remesa
            registro = f"remesa: {r} | step: {step} | cause: {cause}"

        else:

            registro = f"remesa: {r} | step: NO_ENCONTRADO | cause: NO_ENCONTRADO"

        # Muestra resultado en consola
        print(registro)

        resultados.append(registro)

    # Guarda el resultado final
    guardar_reporte(resultados)

# PUNTO DE ENTRADA DEL SCRIPT

if __name__ == "__main__":

    # Ejecuta el monitoreo cuando el script se corre
    ejecutar_monitoreo()