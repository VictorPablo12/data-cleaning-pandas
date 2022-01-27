import re
import numpy as np
import pandas as pd
ruta = '/mnt/c/Users/victo/OneDrive/Escritorio/Data/Ironhack/data-cleaning-pandas/src/paises.csv' # Ruta excell cogido de Githun para limpiar paises de lista dada 

def BC(string):
    """Mira en la cadena que le pasemos (pensado para el contenido de lddf.Date) nos va a devolver 0 
    en caso de que encuentre dentro de la cadena algo del tipo BC ó bc, para luego esos CEROS, convertirlos a null
    en nuestro df sobre el que vamos a graficar """
    try:
        x = re.findall('(?i)B\.(?i)C', str(string))
        if x == []: #No hay match dentro de la cadena ("Date" de la fila en la que estemos)
            return string
        else:
            return np.nan #Si encuentra un Bc lo convierte en NaN
    except IndexError:
        return string

def interval_years(string):
    """Mira en la cadena que le damos si corresponden con stirngs de datos del tipo YYYY - YYYY o del tipo
    YYYY and YYYY, para poder hacer la media de este intervalo y ponerlo en la celda df.Year de esa fila"""
    try:
        y = re.findall('^\d{4}-\d{4}', str(string)) 
        if y != None:
            return int((int(y[0][:4])+int(y[0][5:]))//2) #Media del entero de los 4 primeros digitos + 4 siguientes
        else:
            return string
    except IndexError:
        return string

def sueltos (string): #4 Digitos aislados
    """Miramos los año sueltos que estan puesto solo como texto y un solo año"""
    try:
        z = re.findall("\d{4}", str(string))
        if z != None:
            return z[0]
        else:
            return 0
    except IndexError:
        return 0

#todo - Ver como meter los early´s que tambien hay dentro de los datos
def rescatar_fechas(string): #Clean column
    """A través de esta funcion aplicamos funcion BC y funcion interval_years en ese orden a lo largo de la string
    que le metamos, en principio elementos de la columna df.Date"""
    string = BC(string)
    string = sueltos(string)
    string = interval_years(string)
    if int(string) == 0:
         return np.nan
    else:
        return string
#def cambiar_year (): #year replacement

def actividad(string):
    """Con esto corregimos los datos erroneos en actividades y los agrupamos en actividades que nos interesen, swimming, diving,
    fishing, standing"""
    string = str(string).lower().strip()
    if string != string:
        return np.nan
    elif "swimming" in string or"bathing" in string or "floating" in string or "splashing" in string or "jumped into the water" in string or "playing" in string:
        return "swimming"
    elif "diving" in string or "snorkel" in string:
        return "diving"
    elif "fishing" in string:
        return "fishing"
    elif "surf" in string or "body boarding" in string or "body-boarding" in string or "boogie boarding" in string or "paddleskiing" in string:
        return "surf"
    elif "standing" in string:
        return "standing"
    elif "kayaking" in string or "ship" in string or "sail" in string or "boat" in string or "canoeing" in string or "board" in string or "rowing" in string or "fell into the water" in string:
        return "boating"
    elif "disaster" in string:
        return "sea disaster"
    elif "wading" in string or "walking" in string or "treading water" in string:
        return "walking"
    else:
        return np.nan

paises = pd.read_csv(ruta,encoding='utf-8')

lista_paises = paises[" name"].tolist()
def paises (string):
    """"La funcion recorre la lista de países importada y va comparando conteido de la columna Country
    con el de países que se encuentra en data"""
    if string!=string:
        return np.nan
    string = str(string).lower().title().strip()
    if string!=string:
        return np.nan
    if "Usa" == string:
        string = "United States of America"
    if string == "England":
        string = "United Kingdom"
    if string == "Columbia":
        string = "Colombia"
    if string == "Scotland":
        string = "United Kingdom"
    if string == "Okinawa":
        string = "Japan"
    if string not in lista_paises:
        return np.nan
    else:
        return string

def lesiones (string):
    x = str(string).lower() # para no tener que meter mas cosas en los filtros d elos bucles
    if "fatal" in x and "non" not in x:
        return "fatal"
    elif "no injury" in x or "not injured" in x: #Por la mierda de coincidencias que tenían non y daban 
        return "no injury"
    else:
        return "injury"

def fatal (string):
    if string in ['N', 'M',' N', 'N ']:
        return "N"
    elif string in ['Y','y']:
        return "Y"
    else:
        return np.nan

def species (string):
    x = str(string).lower()
    if "whitetip" in x or "whtietip" in x:
        return "whitetip reef"
    elif "white" in x:
        return "white"
    elif "bull" in x or "zambesi" in x:
        return "bull"
    elif "tiger" in x:
        return "tiger"
    elif "lemon" in x:
        return "lemon"
    elif "nurse" in x:
        return "nurse"
    elif "caribbean" in x:
        return "caribbean reef"
    elif "blacktip" in x or "blacktail" in x:
        return "blacktip"
    elif "grey" in x or "gray" in x:
        return "grey reef shark"
    elif "wobbegong" in x:
        return "wobbegong"
    elif "blue" in x:
        return "blue"
    elif "spinner" in x:
        return "spinner"
    elif "unconfirmed" in x or "questionable " in x:
        return np.nan
    elif "galapagos" in x:
        return "galapagos"
    elif "porbeagle" in x:
        return "porbeagle"
    elif "hammerhead" in x:
        return "hammerhead"
    elif "mako" in x:
        return "mako"
    elif "goblin" in x:
        return "goblin"
    elif "sandbar" in x or "raggedtooth" in x:
        return "sand tiger"
    elif "angel" in x:
        return "angel"
    elif "silky" in x:
        return "silky"
    elif "whaler" in x:
        return "bronze whaler"
    elif "sevengill " in x:
        return "broadnose sevengill"
    elif "nan" == x:
        return np.nan
    else:
        return np.nan