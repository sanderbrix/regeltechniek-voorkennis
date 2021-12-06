#priemgetallen tussen 0 en 350
for getal in range(0,101): 
    if getal > 1:                   #getallenreeks met getallen groter dan 1 t/m 350
        for p in range(2,101):
            if (getal % p) == 0 and not getal == p:    #getallen met rest gelijk aan 0 als ze worden alleen bij deling door zelf 
                break
        else:
            print(getal)            #print deze getallen met rest 0 alleen bij deling door zelf (priemgetallen)