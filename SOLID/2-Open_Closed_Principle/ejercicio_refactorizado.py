# Código no refactorizado.
print("·"*35)
print(" ·· No refactorizado ..")
class Superhero:
    def __init__(self, name, health, attack_type):
        self.name = name
        self.health = health
        self.attack_type = attack_type

    # Si quisieramos añadir otra característica tendríamos que mofidicar.
    def attack(self):
        if self.attack_type == "punch":
            return f"{self.name} attacks with a powerful punch!"
        elif self.attack_type == "laser":
            return f"{self.name} attacks with a laser beam!"
        else:
            return f"{self.name} attacks with a regular attack!"


class Game:
    def __init__(self):
        self.superheroes = []

    def add_superhero(self, superhero):
        self.superheroes.append(superhero)

    def superhero_actions(self):
        for superhero in self.superheroes:
            print(superhero.attack())


game = Game()
superhero1 = Superhero("Superman", 100, "punch")
superhero2 = Superhero("Cyclops", 80, "laser")
game.add_superhero(superhero1)
game.add_superhero(superhero2)
game.superhero_actions()


# Código refactorizado.   
print("·"*35)
print(" ·· Refactorizado ..")
from abc import ABC, abstractmethod


class AttackManager(ABC):
    @abstractmethod
    def attack(self, superhero):
        pass
    
class PunchAttack(AttackManager):
    def attack(self, superhero:Superhero):
        return f"{superhero.name} attacks with a powerfull punch!!"
    
class LaserAttack(AttackManager):
    def attack(self, superhero:Superhero):
        return f"{superhero.name} attacks with a strong laser!!"
    
class FireballAttack(AttackManager):
    def attack(self, superhero:Superhero):
        return f"{superhero.name} attacks with a big fireball!!"
    
    
class Superhero:
    def __init__(self, name, health, AttackManager:AttackManager) -> None:
        self.name = name
        self.health = health
        self.AttackManager = AttackManager
    
    def attack(self):
        return self.AttackManager.attack(self)
        
    
class Game:
    def __init__(self) -> None:
        self.superheroes = [] 
        
    def add_superheroes(self, superhero):
        self.superheroes.append(superhero)
        
    def superheroe_action(self):
        for superhero in self.superheroes:
            print(superhero.attack())
            
game = Game()
superman = Superhero("Superman", 100, PunchAttack())
cyclops = Superhero("Cyclops", 80, LaserAttack())
fireman = Superhero("Cyclops", 120, FireballAttack())

game.add_superheroes(superman)
game.add_superheroes(cyclops)
game.add_superheroes(fireman)

game.superheroe_action()