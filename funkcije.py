Python 3.3.2 (v3.3.2:d047928ae3f6, May 16 2013, 00:03:43) [MSC v.1600 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> import likovi
import math
from math import pi

def opseg(parametar):
    if isinstance(parametar, likovi.Kruznica):
        return 2 * parametar.radijus * pi
    elif isinstance(parametar, likovi.Kvadrat):
        return 4 * parametar.stranica

def povrsina(parametar):
    if isinstance(parametar, likovi.Kruznica):
        return math.pow(parametar.radijus, 2) * pi
    elif isinstance(parametar, likovi.Kvadrat):
        return 4 * parametar.stranica

if __name__ == '__main__':
    print('*** test funkcije ***')
    print(opseg.__name__)
    print(povrsina.__name__)
