import persona
import monster
import combate

contador = 0
print("BEM VINDO A ARENA!")         
heroi = persona.Heroi('Guerreiro')
for i in range(4):
    contador += 1
    print("\n", contador, "a luta.") 
    inimigo = monster.inimigo_facil()
    combate.combate(heroi, inimigo)
for i in range(3):
    contador += 1
    print("\n", contador, "a luta.") 
    inimigo = monster.inimigo_medio()
    combate.combate(heroi, inimigo)      
for i in range (2):
    contador += 1
    print("\n", contador, "a luta.") 
    inimigo = monster.inimigo_dificil()
    combate.combate(heroi, inimigo)

print('\n!!!LUTA FINAL!!!')
boss = monster.inimigo_boss()
combate.combate(heroi, boss)
