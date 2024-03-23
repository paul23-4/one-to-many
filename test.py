from collection import Owner, Pet

def test_owner_initialization():
    owner = Owner("John")
    assert owner.name == "John"

def test_pet_initialization():
    pet = Pet("Fido", "dog")
    assert pet.name == "Fido"
    assert pet.pet_type == "dog"

def test_pet_invalid_type():
    try:
        pet = Pet("Fluffy", "horse")
    except Exception as e:
        assert str(e) == "Invalid pet type: horse"

def test_owner_add_pet():
    owner = Owner("Jane")
    pet = Pet("Whiskers", "cat")
    owner.add_pet(pet)
    assert owner.pets() == [pet]

def test_get_sorted_pets():
    owner = Owner("Alice")
    pet1 = Pet("Spot", "dog")
    pet2 = Pet("Felix", "cat")
    pet3 = Pet("Tweety", "bird")
    owner.add_pet(pet1)
    owner.add_pet(pet2)
    owner.add_pet(pet3)
    assert [pet.name for pet in owner.get_sorted_pets()] == ["Felix", "Spot", "Tweety"]


def test_invalid_add_pet():
    owner = Owner("Bob")
    try:
        owner.add_pet("Invalid Pet")
    except Exception as e:
        assert str(e) == "Invalid pet: must be an instance of Pet"