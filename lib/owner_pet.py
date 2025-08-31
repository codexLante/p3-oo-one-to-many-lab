# owner_pet.py

class Pet:
    PET_TYPES = ['dog', 'cat', 'rodent', 'bird', 'reptile', 'exotic']
    all = []

    def __init__(self, name, pet_type, owner=None):
        if pet_type not in Pet.PET_TYPES:
            raise Exception("Invalid pet type")
        self.name = name
        self.pet_type = pet_type
        self.owner = owner
        Pet.all.append(self)

    def __repr__(self):
        return f"<Pet name={self.name}, type={self.pet_type}>"


class Owner:
    def __init__(self, name):
        self.name = name

    def pets(self):
        """Return all pets owned by this Owner"""
        return [pet for pet in Pet.all if pet.owner == self]

    def add_pet(self, pet):
        """Validate pet instance and assign to this owner"""
        if not isinstance(pet, Pet):
            raise Exception("Must be a Pet instance")
        pet.owner = self

    def get_sorted_pets(self):
        """Return pets sorted by name"""
        return sorted(self.pets(), key=lambda pet: pet.name)

    def __repr__(self):
        return f"<Owner name={self.name}>"