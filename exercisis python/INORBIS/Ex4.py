

from array import array

# %2== 0 =parell
def ImparellParell(num): #imparell=false #parell=true
    num=0
    for num in range(0, 100):
        num==[numer]
        num==num+2
        

    if (num == [numer] ):
        return (True)
    else:
        return (False)


def Corrector():
    array_numeros=[22,33,44,50,100,55,74,73,2]
    array_resultat=[True,False,True,True,True,False,True,False,True]
    array_resultat_alumne=[]
    for numero in array_numeros:
        array_resultat_alumne.append(ImparellParell(array_numeros))
    
    if(array_resultat==array_resultat_alumne):
        print("TEST OK")
    else:
        print("TEST NOT OK")

        
        

Corrector()