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
        print(sac.poids)
        print(sac.valeurs)
            
    return sac

lire_sac("sad_4.txt")


