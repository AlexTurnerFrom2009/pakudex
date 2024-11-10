import pakuri
from pakudex import Pakudex

if __name__ == "__main__":
  print("Welcome to Pakudex: Tracker Extraordinaire!")
  max_capacity = input("Enter max capacity of the Pakudex:")
  print(f"The Pakudex can hold {max_capacity} species of Pakuri.")
  p = Pakudex(20)

  while True:
    choice = input("\nPakudex Main Menu\n-----------------\n1. List Pakuri\n2. Show Pakuri\n3. Add Pakuri\n4. Evolve Pakuri\n5. Sort Pakuri\n6. Exit")
    
    if choice == 1:
      for i, species in emurate(p.species_list):
        print(f"{i}. {species}")