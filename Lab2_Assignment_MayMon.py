# On One Sunny Sunday, My little nephew asked me to take him to the zoo.
# So, let's enjoy our journey to zoo.
# In the zoo, we are going there as the audience to see the animals
# But I also wonder about how the authority manage zoo system. 


from abc import ABC, abstractmethod  #need this for abstract classes

#start
class Animal(ABC):
    def __init__(self, name, species, age, food):
       # classify the name according to general animals
        self.name = name
        self.species = species
        self.age = age
        self.food = food
    
    def __str__(self):
        return f"{self.name} is a {self.species} aged {self.age} years"
    
    @abstractmethod  
    def make_sound(self):
        def feed(self):
            return f"{self.name} eats {self.food}"
        

# this one is to show inheritance 
class Mammal(Animal):
    def __init__(self, name, species, age, food, has_fur):
        # Call parent class constructor using super()
        super().__init__(name, species, age, food)
        self.has_fur = has_fur

# added some common animals at the zoo (especially in zoo in Myanmar)
# I want to add cat but cat is not common :)
class Lion(Mammal):
    def __init__(self, name, age):
        super().__init__(name, "Lion", age, "meat", True)
    
    def make_sound(self):
        return "Roar!"

class Bird(Animal):
    def __init__(self, name, species, age, food, can_fly):
        super().__init__(name, species, age, food)
        self.can_fly = can_fly

class Eagle(Bird):
    def __init__(self, name, age):
        super().__init__(name, "Eagle", age, "small animals", True)
    
    def make_sound(self):
        return "Screech!"

class Reptile(Animal):
    def __init__(self, name, species, age, food, has_scales):
        super().__init__(name, species, age, food)
        self.has_scales = has_scales


class Snake(Reptile):
    def __init__(self, name, age):
        super().__init__(name, "Snake", age, "mice", True)
    
    def make_sound(self):
        return "Hiss!"


# after defining class for animals and their characteristics, we move to function
# the main function of zoo is to keep animals with safety and to show the animals to people at a distance
# when we want to initalize the zoo system, we have to consider the list of animals, new animals,and daily updated one.

class Zoo:
    def __init__(self):
        self.animals = []
    
    def add_animal(self, animal):
        self.animals.append(animal)
        print(f"{animal.name} has been added to the zoo!")
    
    def list_animals(self):
        print("\nAnimals in the zoo:")
        for animal in self.animals:
            print(str(animal))
    
    def make_all_sounds(self):
        print("\nZoo animals are making sounds:")
        for animal in self.animals:
            print(f"{animal.name} says: {animal.make_sound()}")
    
    def feed_all_animals(self):
        print("\nFeeding all animals:")
        for animal in self.animals:
            print(animal.feed())

# this function will tell how zoom systems works
# so we recall and define the function

def main():
    my_zoo = Zoo()
    # gave crazy name to some animals
    # Create some animals
    lion1 = Lion("King", 5)
    eagle1 = Eagle("EE", 3)
    snake1 = Snake("Baki", 2)
    
    # Add animals to the zoo
    my_zoo.add_animal(lion1)
    my_zoo.add_animal(eagle1)
    my_zoo.add_animal(snake1)
    
    # shows zoo functionalities
    my_zoo.list_animals()
    my_zoo.make_all_sounds()
    my_zoo.feed_all_animals()

if __name__ == "__main__":
    main()

# after calling the main final function, our visit to zoo journey ended here.


