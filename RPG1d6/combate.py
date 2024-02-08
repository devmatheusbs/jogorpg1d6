import random
import sys
import time
def combate(heroi, monstro):
    print_lento(f'\nINICIANDO COMBATE\n {heroi.classe}({heroi.hp}) VS {monstro.nome}({monstro.hp})\n')
    heroihptemp = heroi.hp
    while heroihptemp or monstro.hp != 0:
        dado_heroi = random.randint(1,20) + heroi.level % 3
        dado_monstro = random.randint(1,20)
        if (heroi.dano + dado_heroi) >= (monstro.defesa + dado_monstro) or heroi.classe == "Mago":
            print_lento(f'{heroi.classe}({heroihptemp}) acerta {monstro.nome}({monstro.hp}).')
            if dado_heroi >= 20:
                if heroi.classe == "Guerreiro":
                    acerto = random.randint(1, heroi.dano) *2
                elif heroi.classe == "Mago":
                    acerto = 0
                    for _ in range(heroi.level):
                        hit = random.randint(1, heroi.dano) *2
                        acerto += hit            
                print_lento("ACERTO CRÍTICO!!!")
            else:
                if heroi.classe == "Guerreiro":
                    acerto = random.randint(1, heroi.dano) 
                elif heroi.classe == "Mago":
                    acerto = 0
                    for _ in range(heroi.level):                        
                        hit = random.randint(1, heroi.dano) 
                        acerto += hit             
            monstro.hp -= acerto
            print_lento(f'{heroi.classe}({heroihptemp}) causou {acerto} de dano em {monstro.nome}({monstro.hp}).')
            if monstro.hp <= 0:
                levelup = heroi.levelup()
                print_lento(f'\nVitória, {monstro.nome} foi derrotado!')
                print_lento(f'{heroi.classe} subiu para o level {heroi.level}')
                print(f'Hp+{levelup}')
                return
        else:
            print_lento(f'{heroi.classe} errou!')            
        
        if (monstro.dano + dado_monstro) >= (heroi.defesa + dado_heroi):            
            print_lento(f'{monstro.nome}({monstro.hp}) acerta {heroi.classe}({heroihptemp}).')
            if dado_monstro >= 20:
                acerto = monstro.dano *2
                print_lento("ACERTO CRÍTICO!!!")
            else:
                acerto = monstro.dano
            heroihptemp -= acerto
            print_lento(f'{monstro.nome}({monstro.hp}) causou {acerto} de dano em {heroi.classe}({heroihptemp}).')
            
            if heroihptemp <= 0:
                print_lento(f'\n{heroi.classe}({heroihptemp}) foi derrotado por {monstro.nome}({monstro.hp})')
                print_lento('Game Over')            
                sys.exit()
        else:
            print_lento(f'{monstro.nome}({monstro.hp}) errou!')

def print_lento(texto):
    for letra in texto:
        sys.stdout.write(letra)
        sys.stdout.flush()
        time.sleep(0.04)
    print("\n")