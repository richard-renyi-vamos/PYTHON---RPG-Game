import random

# Define the player class
class Player:
    def __init__(self, name, health, attack, defense):
        self.name = name
        self.health = health
        self.attack = attack
        self.defense = defense
        self.weapon = None

    def equip_weapon(self, weapon):
        self.weapon = weapon

    def attack_enemy(self, enemy):
        if self.weapon:
            damage = self.attack + self.weapon.damage - enemy.defense
        else:
            damage = self.attack - enemy.defense

        if damage > 0:
            enemy.health -= damage
            print(f"{self.name} attacks {enemy.name} for {damage} damage!")
        else:
            print(f"{self.name} attacks but does no damage to {enemy.name}!")

    def is_alive(self):
        return self.health > 0


# Define the enemy class
class Enemy:
    def __init__(self, name, health, attack, defense):
        self.name = name
        self.health = health
        self.attack = attack
        self.defense = defense

    def attack_player(self, player):
        damage = self.attack - player.defense
        if damage > 0:
            player.health -= damage
            print(f"{self.name} attacks {player.name} for {damage} damage!")
        else:
            print(f"{self.name} attacks but does no damage to {player.name}!")

    def is_alive(self):
        return self.health > 0


# Define the weapon class
class Weapon:
    def __init__(self, name, damage):
        self.name = name
        self.damage = damage


# Define the game loop
def game():
    # Create player and enemy
    player = Player("Hero", 100, 20, 10)
    enemy = Enemy("Goblin", 50, 15, 5)

    # Create a weapon and equip it to the player
    sword = Weapon("Sword", 10)
    player.equip_weapon(sword)

    # Game loop
    while player.is_alive() and enemy.is_alive():
        print("\nChoose an action:")
        print("1. Attack")
        print("2. Run")
        action = input("Enter the number of your action: ")

        if action == "1":
            player.attack_enemy(enemy)
            if enemy.is_alive():
                enemy.attack_player(player)
        elif action == "2":
            print("You ran away!")
            break
        else:
            print("Invalid action! Please choose 1 or 2.")

        # Check if anyone is dead
        if not player.is_alive():
            print(f"\n{player.name} has been defeated! Game Over!")
        elif not enemy.is_alive():
            print(f"\n{enemy.name} has been defeated! You win!")

# Start the game
game()
