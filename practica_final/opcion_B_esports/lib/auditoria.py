# 5.	Para cada fichero, crea una función que analice y cuente:
# •	Valores vacíos por campo: None, cadena vacía, "N/A", "-", "no disponible", etc.
# •	Duplicados exactos y parciales (mismo dato escrito diferente, ej: "Los Rebeldes" vs "los rebeldes").
# •	Formatos inconsistentes: ¿cuántas variaciones distintas hay para un mismo tipo de campo?
# •	Valores fuera de rango: precios negativos, edades imposibles, etc.
# •	Espacios extra: campos con espacios al principio, al final o dobles en medio.
# # 
import csv
from openpyxl import load_workbook
import json

valores_vacios = ["", None, "N/A", "-", "no disponible"]


