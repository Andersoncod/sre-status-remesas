📑 Tabla de Contenido

Descripción

1. Objetivos
2. Archivos del Proyecto
3. Diccionario de Estados y Acciones de Soporte
4. Estructura del Proyecto
5. Ejecución
6. Resultado
7. Tecnologías Utilizadas

📌 Descripción

Este proyecto simula un sistema de monitoreo de infraestructura aplicado a remesas.

El script:
Lee números de remesa desde un archivo remesas.txt
Busca cada remesa en un archivo de registros json_data.txt
Extrae únicamente los campos:
* remesa
* step
* cause
Muestra los resultados en consola
Genera automáticamente un archivo de reporte
Este tipo de automatización es común en equipos:
SRE (Site Reliability Engineering)
Soporte Tecnológico
Operaciones Financieras
Monitoreo de transacciones

🎯 Objetivos
Objetivo General

Automatizar la consulta del estado de remesas mediante un script en Python.

Objetivos Específicos

Implementar lectura y escritura de archivos TXT
Procesar datos estructurados en formato JSON
Aplicar modularización mediante funciones reutilizables
Implementar manejo de errores con try/except
Generar reportes automáticos de monitoreo

📁 Archivos del Proyecto

remesas.txt → contiene los números de remesa a consultar
json_data.txt → contiene los registros JSON simulados
monitor_remesas.py → script principal
reporte_monitoreo.log → reporte generado automáticamente


📘 Diccionario de Estados y Acciones de Soporte
| Estado (step)                 | Significado                        | Acción Recomendada           |
| ----------------------------- | ---------------------------------- | ---------------------------- |
| RECEIVED_PEND_NOTIFY          | Recibido pendiente de notificación | Esperar procesamiento        |
| READY_TO_PAY_PEND_BUSINESS    | Pendiente validación comercial     | Revisar reglas de negocio    |
| READY_TO_PAY_PEND_CIB_FINACLE | Pendiente validación bancaria      | Validar integración bancaria |
| PAID_NOTIFIED                 | Remesa pagada correctamente        | Proceso finalizado           |
| FAILED                        | Error en la transacción            | Revisar logs y reintentar    |



🗂️ Estructura del Proyecto
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
└── README.md

▶️ Ejecución

Ubicarse en la carpeta raíz del proyecto y ejecutar:

python src/monitor_remesas.py

Si se ejecuta desde la carpeta src, usar:

python monitor_remesas.py

📊 Resultado

El programa mostrará en consola el estado de cada remesa en el siguiente formato:

remesa: R25981271593 | step: PAID_NOTIFIED | cause:

Además, generará automáticamente el archivo:

logs/reporte_monitoreo.log

Este archivo contiene el mismo resultado mostrado en consola y sirve como evidencia del monitoreo realizado.

🛠️ Tecnologías Utilizadas

Python 3

Manejo de archivos TXT
Procesamiento de JSON
Programación modular
Manejo de excepciones


