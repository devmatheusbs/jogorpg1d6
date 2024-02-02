import random
import persona
facil = {
    "A":"Rato Sombrio",
    "B":"Morcego Espectral",
    "C": "Goblin Vagante",
    "D": "Aranha Venenosa", 
    "E": "Espírito Travesso",
    "F": "Serpente Rastejante",
    "G": "Rato de Esgoto",
    "H": "Golem de Pedra Pequeno",
    "I": "Kobold Saltitante",
    "J": "Imp Luminoso"
}
medio =  {
    "A":"Orc Retalhador",
    "B":"Esqueleto Ardiloso",
    "C":"Harpia Cruel",
    "D":"Ladrão das Sombras",
    "E":"Dríade Enfeitiçadora",
    "F": "Lobo Sombrio"
    }
dificil= {
        "A": "Dragão das Trevas", 
        "B":"Lich Poderoso", 
        "C": "Minotauro Furioso", 
        "D": "Elemental da Tempestade", 
        "E": "Manticora Voraz" 
        }
boss = {
    "A": "Senhor do Abismo, Zephyrath, o Devorador de Mundos",
    "B": "Senhora das Sombras, Lilith, a Feiticeira Sombria",
    "C": "Vorax, o Behemoth Flamejante"
}
    
def inimigo_facil():
    inimigo_aleatorio = random.choice(list(facil.keys()))
    inimigo_facil = persona.Monstro(facil[inimigo_aleatorio], random.randint(1,6), random.randint(8,10), random.randint(5,15), 1)
    return inimigo_facil
      
def inimigo_medio():
    inimigo_aleatorio = random.choice(list(medio.keys()))
    inimigo_medio = persona.Monstro(medio[inimigo_aleatorio], random.randint(1,10), random.randint(10,12), random.randint(16,40), 2)
    return inimigo_medio
def inimigo_dificil():
    inimigo_aleatorio = random.choice(list(dificil.keys()))
    inimigo_dificil = persona.Monstro(dificil[inimigo_aleatorio], (random.randint(1,10)+random.randint(1,10)), random.randint(12,14), random.randint(41,80), 3)
    return inimigo_dificil

def inimigo_boss():
    inimigo_aleatorio = random.choice(list(boss.keys()))
    inimigo_boss = persona.Monstro(boss[inimigo_aleatorio], (random.randint(1,12)+random.randint(1,12)), random.randint(12,16), 100, 4)
    return inimigo_boss