
class Pakudex:
  stored_pakuri = []
  species_list = [pakuri.species for pakuri in self.stored_pakuri]
  def __init__(self, capacity=20):
    self.max = capacity
  def get_size(self):
    return len(self.stored_pakuri)
  def get_capacity(self):
    return self.max
  def get_species_array(self):
    return self.species_list
  def get_stats(self, species):
    if not species in self.species_list:
      return None
    for pakuri in self.stored_pakuri


  
