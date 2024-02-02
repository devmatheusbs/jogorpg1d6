import random
import sys
def combate(heroi, monstro):
    print(f'\nINICIANDO COMBATE\n {heroi.classe} VS {monstro.nome}\n')
    heroihptemp = heroi.hp
    while heroihptemp or monstro.hp != 0:
        dado_heroi = random.randint(1,20) + heroi.level % 3
        dado_monstro = random.randint(1,20)
        if (heroi.dano + dado_heroi) >= (monstro.defesa + dado_monstro) or heroi.classe == "Mago":
            print(f'{heroi.classe} acerta {monstro.nome}.')
            if dado_heroi >= 20:
                if heroi.classe == "Guerreiro":
                    acerto = random.randint(1, heroi.dano) *2
                elif heroi.classe == "Mago":
                    acerto = 0
                    for _ in range(heroi.level):
                        hit = random.randint(1, heroi.dano) *2
                        acerto += hit            
                print("ACERTO CRÍTICO!!!")
            else:
                if heroi.classe == "Guerreiro":
                    acerto = random.randint(1, heroi.dano) 
                elif heroi.classe == "Mago":
                    acerto = 0
                    for _ in range(heroi.level):                        
                        hit = random.randint(1, heroi.dano) 
                        acerto += hit             
            print(f'{heroi.classe} causou {acerto} de dano em {monstro.nome}.')
            monstro.hp -= acerto
            if monstro.hp <= 0:
                heroi.levelup()
                print(f'\nVitória, {monstro.nome} foi derrotado!')
                print(f'{heroi.classe} subiu para o level {heroi.level}')
                return
        else:
            print(f'{heroi.classe} errou!')            
        
        if (monstro.dano + dado_monstro) >= (heroi.defesa + dado_heroi):            
            print(f'{monstro.nome} acerta {heroi.classe}.')
            if dado_monstro >= 20:
                acerto = monstro.dano *2
                print("ACERTO CRÍTICO!!!")
            else:
                acerto = monstro.dano
            print(f'{monstro.nome}  causou {acerto} de dano em {heroi.classe}.')
            heroihptemp -= acerto
            if heroihptemp <= 0:
                print(f'\n{heroi.classe} foi derrotado por {monstro.nome}')
                print('Game Over')            
                sys.exit()
        else:
            print(f'{monstro.nome} errou!')