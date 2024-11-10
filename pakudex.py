import pakuri

class Pakudex:
  def __init__(self, capacity=20):
    self.max = capacity
    self.stored = {}
    self.species_list = list(self.stored.keys())
    self.occupied = 0

  def get_size(self):
    return len(self.stored)

  def get_capacity(self):
    return self.max

  def get_species_array(self):
    if self.occupied > 0:
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
    self.species_list.sort()
    new_stored = {species: self.stored[species] for species in species_list}
    self.stored = new_stored


  def add_pakuri(self, species):
    if species in self.species_list and self.occupied >= self.max:
      return False
    self.stored.update({species: Pakuri(species)})
    self.species_list.append(species)
    self.occupied += 1
    return True

  def evolve_species(self, species):
      if species in self.species_list:
        self.stored[species].evolve()
        return True
      else:
        return False




  



  
