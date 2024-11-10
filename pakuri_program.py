from pakudex import *

if __name__ == "__main__":
  print("Welcome to Pakudex: Tracker Extraordinaire!")
  max_capacity = 0
  while max_capacity <= 0:
    try:
      max_capacity = int(input("Enter max capacity of the Pakudex: "))
      assert max_capacity > 0
    except:
      print("Please enter a valid size.")
      
  print(f"The Pakudex can hold {max_capacity} species of Pakuri.")
  p = Pakudex(max_capacity)

  while True:
    choice = 0
    while choice <= 0 or choice > 6:
      try:
         choice = int(input("\nPakudex Main Menu\n-----------------\n1. List Pakuri\n2. Show Pakuri\n3. Add Pakuri\n4. Evolve Pakuri\n5. Sort Pakuri\n6. Exit\n\nWhat would you like to do? "))
         assert choice > 0 and choice < 7
      except:
         print("Unrecognized menu selection!")
        
    if choice == 1:
      if not p.get_species_array() == None:
        print("Pakuri In Pakudex:")
        for i, species in enumerate(p.get_species_array()):
          print(f"{i+1}. {species}")
      else:
        print("No Pakuri in Pakudex yet!")

    elif choice == 2:
      requesting = input("Enter the name of the species to display: ")
      stats = p.get_stats(requesting)
      if stats == None:
        print("Error: No such Pakuri!")
      else:
        print(f"Species: {requesting}\nAttack: {stats[0]}\nDefense: {stats[1]}\nSpeed: {stats[2]}")
       
    
    elif choice == 3:
      if p.occupied >= p.max:
        print("Error: Pakudex is full!")
      else:
        adding = input("Enter the name of the species to add: ")
        if p.add_pakuri(adding):
          print(f"Pakuri species {adding} successfully added!")
        else:
          print("Error: Pakudex already contains this species!")

    elif choice == 4:
      evolving = input("Enter the name of the species to evolve: ")
      if p.evolve_species(evolving):
        print(f"{evolving} has evolved!")
      else:
        print("Error: No such Pakuri!")
    
    elif choice == 5:
      p.sort_pakuri()
      print("Pakuri have been sorted!")

    elif choice == 6:
      print("Thanks for using Pakudex! Bye!")
      break

