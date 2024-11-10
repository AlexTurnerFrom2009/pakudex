from pakuri import Pakuri
class Pakudex:

  def __init__(self, capacity=20):
    self.max = capacity
    self.stored = {}
    self.species_list = list(stored.keys())

  def get_size(self):
    return len(self.stored)

  def get_capacity(self):
    return self.max

  def get_species_array(self):
    if len(self.stored) > 0:
      return self.species_list
    return None

  def get_stats(self, species):
    for pakuri in self.species_list:
      if pakuri == species:
        stats = [self.stored[pakuri].attack, self.stored[pakuri].defense, self.stored[pakuri].speed]
        return stats
      else:
        return None

  def sort_pakuri(self):
    new_species_list = sorted(self.species_list)
    new_stored = {species: self.stored[species] for species in new_species_list}
    self.stored = new_stored
    self.species_list = new_species_list

  def add_pakuri(self, species):
    if species in self.species_list:
      return False
    self.stored.update({species: Pakuri(species)})
    self.species_list.append(species)

  def evolve_species(self, species):
      if species in self.species_list:
        self.stored[species].evolve()
        return True
      else:
        return False




  
