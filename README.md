# Worksheet infinita

Este proyecto es una herramienta para generar hojas de trabajo y exámenes en formato PDF utilizando LaTeX; colocando números diferentes en las preguntas para de esta forma reciclar el mismo formato. El funcionamiento de esta se basa en reemplazar el caracter de `␀` (\u2400) a números del uno al nueve. Colocando mas de estos caracteres, se pueden crear números de n número de cifras. (Para entender mejor, favor de checar: `RAMI_PRUEBA/examples/questions.tex`)

## Estructura del proyecto
- `main.py`: Script para compilar el PDF
- `output/`: Carpeta donde se guardan los archivos PDF generados.
- `RAMI_Prueba/`: Una plantilla completa sobre una actividad estructurada.
- `_logs/`: Archivos de registro de la generación.

## Requisitos
- Python 3
- LaTeX instalado en el sistema

## Uso
1. Configura los archivos de preguntas y curso en la carpeta correspondiente.
2. Ejecuta `main.py` para generar el PDF.
3. El archivo generado estará en la carpeta `output/`.


### NOTA LEGAL
Este documento creado a partir de una plantilla en Overleaf cuya licencia cae en Creative Commons CC BY 4.0. 
Referencia: R. Wahyudi. (2025). _Template Dokumen Soal Ujian Itera_. Overleaf. Recuperado de https://www.overleaf.com/latex/templates/template-dokumen-soal-ujian-itera/csqpqtmjzyjm