from random import randint
class Heroi:
    def __init__(self, classe) -> None:
        self.classe = classe
        self.level = 1        
        if classe == 'Guerreiro':
            self.dano = 8
            self.defesa = 12
            self.hp = 10
        elif classe == 'Mago':
            self.dano = 4
            self.defesa = 10
            self.hp = 4      
    
    def levelup(self):
        self.level += 1
        if self.classe == 'Guerreiro':
            self.hp += randint(1,10)
            self.dano += 1
            
            
        elif self.classe == 'Mago':
            self.hp += randint(1,4)
            
class Monstro:
    def __init__(self, nome, dano, defesa, hp, dif) -> None:
            self.nome = nome
            self.dano = dano
            self.defesa = defesa
            self.hp = hp
            self.dif = dif
        