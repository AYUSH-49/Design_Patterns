from Enemy_call import Enemy_call


if __name__ == "__main__":

    TypeofEnemy = input("Enter the type of enemy (Orc/Gobline/Zombie): ").strip().lower()
    NoOfClones = int(input("Enter the number of clones: "))
  
    Enemy=Enemy_call(TypeofEnemy, NoOfClones).create_enemy()
    print(Enemy)
   