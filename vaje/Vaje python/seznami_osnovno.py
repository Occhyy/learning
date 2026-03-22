'''•napiši metodo, ki sprejme seznam in vrne število podseznamov,'''
def steviloPs(seznam):
    return len(seznam)
    
'''napiši metodo, ki sprejme seznam in vrne število negativnih števil na seznamu,'''
def negativnost(seznam):
    stevilo = 0
    for item in seznam:
        for i in item:
            if i < 0:
                stevilo = stevilo + 1
    return stevilo
    
'''napiši metodo, ki sprejme seznam in vrne povprečno vrednost števil na seznamu,'''
def povprecje(seznam):
    vsota = 0
    stevilo = 0
    for item in seznam:
        for i in item:
            vsota = vsota + i
            stevilo = stevilo + 1
    return vsota/stevilo
    
'''napiši metodo, ki sprejme seznam in vrne največje in najmanjše število na seznamu,'''
def minMax(seznam):
    mn, mx = 25, -25
    for item in seznam:
        for i in item:
            if i < mn:
                mn = i
            if i > mx:
                mx = i
    return mn, mx 