class Pet:
    def __init__(self, name, species):
        # attributes represent qualities & characteristics
        self.name = name
        self.species = species

    def __str__(self):
        return f"{self.name} the {self.species}"

    def call(self):
        print(f"Come here, {self.name}!")


# make an instance of pet
nutmeg = Pet(name="Nutmeg", species="dog")
# use method to call pet
nutmeg.call()

pet_data = [("Derbs", "cat"), ("Zeke", "dog"), ("Valvano", "dog")]
pets = []
for name, species in pet_data:
    new_pet = Pet(name=name, species=species)
    pets.append(new_pet)

for pet in pets:
    print(pet)
