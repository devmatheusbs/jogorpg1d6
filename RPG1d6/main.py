import persona
import monster
import combate
print("BEM VINDO A ARENA!")
while True:
    contador = 0
    heroi = None    
    escolha = input('Escolha seu Heroi: (G)uerreiro ou (M)ago?: ')
    if escolha.lower() == "g":         
        heroi = persona.Heroi('Guerreiro')
    elif escolha.lower() == "m":
        heroi = persona.Heroi('Mago')
    else:
        print('Favor, escolha uma opção válida. Para (s)air, digite (s): ')
    if isinstance(heroi, persona.Heroi):   
        for i in range(4):
            contador += 1
            print("\n", contador,"a luta.") 
            inimigo = monster.inimigo_facil()
            combate.combate(heroi, inimigo)
        for i in range(3):
            contador += 1
            print("\n", contador,"a luta.") 
            inimigo = monster.inimigo_medio()
            combate.combate(heroi, inimigo)      
        for i in range (2):
            contador += 1
            print("\n", contador,"a luta.") 
            inimigo = monster.inimigo_dificil()
            combate.combate(heroi, inimigo)

        print('\n!!!LUTA FINAL!!!')
        boss = monster.inimigo_boss()
        combate.combate(heroi, boss)
