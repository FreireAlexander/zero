from uuid import uuid4


class Dog():

    def __init__(self, name) -> None:
        self.__name = name
        self.__UUID = uuid4()
        self.age = 0


    def __str__(self) -> str:
        json = {
            'id': self.UUID,
            'name': self.name,
            'age': self.age
        }

        return str(json)


    
    @property
    def UUID(self):
        return self.__UUID
    

    @UUID.setter
    def setID(self, value):
        self.__UUID = value
    
    @property
    def name(self):
        return self.__name
    

    @UUID.setter
    def setName(self, value):
        self.__name = value






def main():
    dognames = ["Toby", "Charlotte", "Koro", "Zeus", "Chiripa", "Mota"]
    dogs = []
    for dogname in dognames:
        dogs.append(Dog(dogname))

    for dog in dogs:
        print(f"Dog information for {dog}\n")



if __name__ == "__main__":
    main()