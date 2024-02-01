import persona
from random import randint
def combate(heroi, monstro):
    print(f'\nINICIANDO COMBATE {heroi.classe} VS {monstro.nome}')
    heroihptemp = heroi.hp
    while heroihptemp or monstro.hp != 0:
        if (heroi.dano + randint(0,6)) >= monstro.defesa:
            acerto = randint(1, heroi.dano)
            print(f'{heroi.classe} acertou {monstro.nome} causando {acerto} de dano.')
            monstro.hp -= acerto            
        if monstro.hp <= 0:
            heroi.levelup()
            print(f'Vitória, {monstro.nome} foi derrotado!')
            print(f'{heroi.classe} subiu para o level {heroi.level}')
            return 
        if (monstro.dano + randint(0,6)) >= heroi.defesa:            
            acerto = randint(1, monstro.dano)
            print(f'{monstro.nome} acertou {heroi.classe} causando {acerto} de dano.')
            heroihptemp -= acerto
        if heroihptemp <= 0:
            global gameover
            gameover += 1
            print('Game Over')
            return
                     
             
gameover = 0
    
heroi = persona.Heroi('Guerreiro')
for i in range(3):
    morcego = persona.Monstro('Morcego', randint(2,4), randint(2,4), randint(4,6))
    combate(heroi, morcego)
for i in range(2):
    vampiro = persona.Monstro('Vampiro', randint(6,8), randint(3,6), randint(10,16))
    combate(heroi, vampiro)        
vampiro_lord = persona.Monstro('Vampiro Lord', randint(15,16), randint(10,12), randint(18,25))
combate(heroi, vampiro_lord)
    
