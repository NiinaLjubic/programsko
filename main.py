Python 3.3.2 (v3.3.2:d047928ae3f6, May 16 2013, 00:03:43) [MSC v.1600 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> from vjezba_9.Mine.Polje import Polje 
 
 
 
 
 p = Polje(5,2) 
 for red in p._Polje__kvadrati: 
     for k in red: 
         k.otkrij() 
         print(k, end = '|') 
     print() 
 
 
 print('\n*** test 2 ***') 
 print('*** rezultat varira zbog slucajnog izbora mina koristenjem random modula ***') 
 p = Polje(5,2) 
 for red in p._Polje__kvadrati: 
     for k in red: 
         k.otkrij() 
 print(p) 
