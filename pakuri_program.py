from pakudex import *
import pakuri

if __name__ == "__main__":
  print("Welcome to Pakudex: Tracker Extraordinaire!")
  max_capacity = input("Enter max capacity of the Pakudex:")
  print(f"The Pakudex can hold {max_capacity} species of Pakuri.")
  p = Pakudex(20)

  while True:
    choice = int(input("\nPakudex Main Menu\n-----------------\n1. List Pakuri\n2. Show Pakuri\n3. Add Pakuri\n4. Evolve Pakuri\n5. Sort Pakuri\n6. Exit"))
    
    if choice == 1:
      if not p.get_species_array() == None:
        print("Pakuri in Pakudex:")
        for i, species in enumerate(p.get_species_array()):
          print(f"{i}. {species}")
      else:
        print("No Pakuri in Pakudex yet!")

    elif choice == 2:
      requesting = input("Enter the name of the species to display:")
      stats = p.get_stats(requesting)
      if not stats == None:
        print(f"Species: {requested}\nAttack: {stats[0]}\nDefense: {stats[1]}\nSpeed: {stats[2]}")
      else:
        print("Error: No such Pakuri!")
    
    elif choice == 3:
      adding = input("Enter the name of the species to add:")
      if p.add_pakuri(adding):
        print(f"Pakuri species {adding} successfully added!")
      elif p.occupied >= p.max:
        print("Error: Pakudex is full!")
      else:
        print("Error: Pakudex already contains this species!")

    elif choice == 4:
      evolving = input("Enter the name of the species to evolve:")
      if p.evolve(evolving):
        print(f"{evolving} has evolved!")
      else:
        print("Error: No such Pakuri!")
    
    elif choice == 5:
      p.sort_pakuri()
      print("Pakuri have been sorted!")

    elif choice == 6:
      print("Thanks for using Pakudex! Bye!")
      break

