from random import randint
class Heroi:
    def __init__(self, classe) -> None:
        self.classe = classe
        self.level = 1        
        if classe == 'Guerreiro':
            self.dano = 4
            self.defesa = 6
            self.hp = 6
        elif classe == 'Mago':
            self.dano = 6
            self.defesa = 4
            self.hp = 4      
    
    def levelup(self):
        self.level += 1
        if self.classe == 'Guerreiro':
            self.hp += randint(2,6)
            self.dano +=  randint(0,1)
            self.defesa += randint(1,2)
        elif self.classe == 'Mago':
            self.hp += randint(1,4)
            self.dano += randint(1,2)
            self.defesa += randint(0,1)

class Monstro:
    def __init__(self, nome, dano, defesa, hp) -> None:
            self.nome = nome
            self.dano = dano
            self.defesa = defesa
            self.hp = hp
        