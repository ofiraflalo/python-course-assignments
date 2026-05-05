import math
def calculate_ph(h_concentration):
  if h_concentration <= 0:
  raise ValueError("Concentration must be greater than 0.")
       return -math.log10(h_concentration)
