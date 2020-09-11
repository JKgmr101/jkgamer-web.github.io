
import random



blockornot = "no"
enemyhealth = 3000
health = 3000
attackornot = "no"
enemyattackornot = "no"
enemyblockornot = "no"

def start():
    print("BATTLE ENGINE 2.0")
    startornot = input("Do you want to start?")
    if startornot == "yes":
        attack()
    elif startornot == "how do you play":
        print("This is RNG based so just use attack to deal damage or block to defend. The enemy also has a counter attack so be careful and don't spam attacks")
        start()
    else:
        print("You ran away from cowardness")
        storycontinues()

def attack():
    global enemyhealth
    global attackornot
    global blockornot
    global enemyattackornot
    global enemyblockornot
    blockornot = "no"
    attackornot = "no"
    enemyattackornot = "no"
    enemyblockornot ="no"
    attackorblock = input("Do you want to attack or block or heal?")
    if attackorblock == "attack":
        attackornot = "yes"
        enemyattack()
    elif attackorblock == "block":
        block()
    elif attackorblock == "heal":
        heal()
    else:
        print("I dont understand")
        attack()


def block():
    global blockornot
    blockornot = "yes"
    enemyattack()




def enemyblock():
    global enemyblockornot
    enemyblockornot = "yes"
    
def enemyattack():
    global health
    global enemyhealth
    if health <= 0:
        print("You lose against the beast")
    elif enemyhealth <= 0:
        print("You Won!")
    while health > 1 and enemyhealth > 1:
        global enemyattackornot
        global enemyblockornot
        global blockornot
        global attackornot
        enemyattack = random.randint(1,3)
        if enemyattack == 1:
            enemyattackornot = "yes"
        elif enemyattack == 2:
            enemyblock()
        elif enemyattack == 3:
            enemyattackornot = "counter-attack"

        
        if enemyattackornot == "yes" and attackornot == "yes":
            print("You dealt 300 damage")
            print("Enemy dealt 400 damage")
            health = health - 400
            enemyhealth = enemyhealth - 300
            print("HP:", health)
            print("EnemyHP:", enemyhealth)
            attack()
        elif enemyblockornot == "yes" and attackornot == "yes":
            print("You swung but the enemy blocked")
            print("Enemy block was weak. You dealt 150 damage")
            enemyhealth = enemyhealth - 150
            print("HP:", health)
            print("EnemyHP:", enemyhealth)
            attack()
        elif blockornot == "yes" and enemyattackornot == "yes":
            print("You blocked and enemy attacked. No damage was dealt")
            print("HP:", health)
            print("EnemyHP:", enemyhealth)
            attack()
        elif enemyblockornot == "yes" and blockornot == "yes":
            print("Nothing happend")
            print("HP:", health)
            print("EnemyHP:", enemyhealth)
            attack()
        elif enemyattackornot == "counter-attack" and attackornot == "yes":
            print("Enemy used counter-attack")
            print("You dealt 150 damage and Enemy dealt 350 damage")
            health = health - 350
            enemyhealth = enemyhealth - 150
            print("HP:", health)
            print("EnemyHP:", enemyhealth)
            attack()
        elif enemyattackornot == "counter-attack" and blockornot == "yes":
            print("Enemy used counter-attack")
            print("You blocked so nothing happened")
            print("HP:", health)
            print("EnemyHP:", enemyhealth)
            attack()
        elif attackornot == "heal" and enemyattackornot == "yes":
            print("You healed but got attacked!")
            health = health - 400
            print("HP:", health)
            print("EnemyHP:", enemyhealth)
            attack()
        elif attackornot == "heal" and enemyblockornot == "yes":
            print("You healed peacfully")
            print("HP:", health)
            print("EnemyHP:", enemyhealth)
            attack()
        elif attackornot == "heal" and enemyattackornot == "counter-attack":
            print("You healed but took some damage from counter attack")
            health = health - 100
            print("HP:", health)
            print("EnemyHP:", enemyhealth)
            attack()
            


def storycontinues():
    print("because you ran away from the mosnter you ran away from fame")

def heal():
    global health
    global attackornot
    print("You healed 200 health")
    health = health + 200
    print("HP:", health)
    print("EnemyHP:", enemyhealth)
    attackornot = "heal"
    enemyattack()



start()
