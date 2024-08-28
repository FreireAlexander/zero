from dogos import Dog

def readTobifile(file):
    with open(file, 'r') as f:
        lines = f.readlines()
        for line in lines:
            dog_info = line.replace('\n','').split(',')
            print(f"printing dog info {dog_info}")



def createFile(items, name: str="dogos.tobi"):
    print(f"Creating file {name}\n")
    with open(name, 'w' ) as f:
        for item in items:
            f.write(f"{item.UUID},{item.name}\n")

    f.close
    print(f"{name} has been created")


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