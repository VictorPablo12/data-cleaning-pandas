# Data Cleaning with Pandas
![My_project](/readme/My_project.jpg)

## INTRO:
Para este proyecto, partimos de la base de datos facilitada, que está disponible aquí: 
[Global Shark Attacks 📚](https://www.kaggle.com/teajay/global-shark-attacks)      

## OBJETIVO:
La finalidad del ejercicio es poder poner en prática todo lo aprendido sobre **exploración, limpieza, análisis y visualización de datos.**

---
## REQUISITOS:
1. Debemos establecer al menos una `hipótesis` en base a la cual/es limpiaremos el dataset.
2. Hacer al menos `dos gráficos` que apoyen esas premisas.
3. Usar al menos `5 técnicas` de limpieza de datos distintas.
---

### HIPÓTESIS:

1. Nadar **no** es necesariamente la actividad más peligrosa
2. Los tiburones blancos son la especie que **más ataques** realiza


## ORGANIZACIÓN:

**1. Limpieza:**
- Realizada una breve exploración del tamaño y calidad de los datos, procedo a un primer desbastado básico
- En las siguientes fases he recorrido el archivo por columnas, evaluando la mejor manera de extraer la mayor cantidad de datos en función del contenido, el tipo de dato y la utilidad que nos podría proporcionar para futuras visualizaciones. 
- Este proceso está documentado en:
> [`clean.ipynb`](1_clean.ipynb) archivo comentado con el proceso de limpieza
> [`cleaning_functions.py`](src/cleaning_functions.py) funciones creadas ***ad hoc*** para la limpieza y extracción
> [`attack_limpio.csv`](data/attack_limpio.csv) archivo obtenido en el último paso una vez llevada a cabo la limpieza

**2. Análisis:**
- Una vez obtenido el archivo **limpio** se han realizado varias gráficas, apoyándome en distintas librerías, para poder 
apoyar de manera visual las conclusiones.
- Este proceso está documentado en:
> [`analysis.ipynb`](2_analysis.ipynb) archivo que incluye tanto los grafos como los conclusiones obtenidas del estudio
> [`/figures`](/figures) en esta carpeta se han exportado también los gráficos presentados en el estudio

## TECNOLOGY STACK:
* [Nunpy](https://numpy.org/doc/1.18/) Pyhton library
* [Pandas](https://pandas.pydata.org/) Pyhton library
* [Seaborn](https://seaborn.pydata.org/) Pyhton library
* [Maplotlib](https://matplotlib.org/) Pyhton library
* [Regex](https://docs.microsoft.com/es-es/dotnet/api/system.text.regularexpressions.regex?view=net-6.0) Pyhton library
* [Países.csv](https://gist.github.com/brenes/1095110) Archivo con refencias de países [@brenes](https://github.com/brenes)
