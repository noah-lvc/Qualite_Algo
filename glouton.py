import re

class Sac_a_dos:
    def __init__(self, N, W):
        self.N = N
        self.W = W
        self.poids = [0]*N
        self.valeurs = [0]*N

def lire_sac(fichier: str) -> Sac_a_dos:
    with open(fichier, 'r') as f:
        N, W = map(int, f.readline().split())
        sac = Sac_a_dos(N, W)
        for i in range(N):
            valeur, poids = map(int, f.readline().split())
            sac.poids[i] = poids
            sac.valeurs[i] = valeur
        print("---------------------SAC A DOS CREER---------------------")
        print("poids : " + str(sac.poids))
        print("valeurs : " + str(sac.valeurs))
            
    return sac

def glouton(sad:Sac_a_dos): 

    ratio = [sad.valeurs[i] / sad.poids[i] for i in range(len(sad.poids))]      
    res = [] 
    
    while sad.W > 0 and len(ratio) > 0:
        max_index = ratio.index(max(ratio))    
        if sad.W >= sad.poids[max_index]:
            res.append(["poids", sad.poids[max_index], "valeur", sad.valeurs[max_index]])
            sad.W -= sad.poids[max_index]  
        ratio.pop(max_index)
        sad.poids.pop(max_index)
        sad.valeurs.pop(max_index)
    
    print("---------------------METHODE GLOUTON---------------------")
    print("Resultat : " + str(res))
    poid_totale = sum(poid[1] for poid in res)
    valeur_totale = sum(val[3] for val in res)
    print("Poid totale :", poid_totale)
    print("Valeur totale :", valeur_totale)
    return res

def dynamique(sad:Sac_a_dos):
    tab = [[0]* sad.W for i in range(sad.W-1)]

    for w in range(1, len(tab[n])):
        if w < sad.poids[n-1]:


    print("---------------------METHODE DYNAMIQUE---------------------")
    for ligne in res2d:
        print(ligne)

    return res2d




sac4 = lire_sac("sad_4.txt")
#glouton(sac4)
dynamique(sac4)