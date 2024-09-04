from dogos import Dog
import re

def readTobifile(file):
    with open(file, 'r') as f:
        print(f"Reading file {file}")
        lines = f.read().splitlines()
        for line in lines:
            dog_info = line.split(',')
            print(f"printing dog info {dog_info}")

    f.close()


def createFile(items, name: str="dogos.tobi"):
    print(f"Creating file {name}\n")
    with open(name, 'w' ) as f:
        for item in items:
            f.write(f"{item.UUID},{item.name},{item.age}\n")

    f.close
    print(f"{name} has been created")


def writeToFile(file, item):
    with open(file, 'a') as f:
        f.write(f"{item.UUID},{item.name},{item.age}\n")


def updateDogname(file, oldName, newName):
    """
    Maybe using re.groups()
    """
    pattern = f",{oldName},"
    newpattern = r",{newName},".replace('{newName}',newName)
    print(pattern)
    pattern = re.compile(re.escape(pattern), re.DOTALL | re.MULTILINE)
    print(pattern)
    with open(file, 'r+') as f:
        content = f.read()
        print(content)
        found = re.search(pattern,content)
        print(f"found value: {found}")
    
    if found:
        print(f"Found {found}")
        print(f"Updating {oldName} for {newName}")
        res = re.sub(pattern, newpattern, content)
        with open(file, 'w') as f:
            f.write(res)
    else:
        print("Not found")




def main():
    dognames = ["Toby", "Charlotte", "Koro", "Zeus", "Chiripa", "Mota"]
    dogs = []
    for dogname in dognames:
        dogs.append(Dog(dogname))

    for dog in dogs:
        print(f"Dog information for {dog}\n")


    createFile(dogs)



if __name__ == "__main__":
    main()
    readTobifile('dogos.tobi')
    name = input("Enter Dog name: ")
    dog = Dog(name)
    writeToFile('dogos.tobi',dog)
    readTobifile('dogos.tobi')
    search = input('Enter dog name for search: ')
    updateDogname('dogos.tobi', search, 'perrito')
    readTobifile('dogos.tobi')