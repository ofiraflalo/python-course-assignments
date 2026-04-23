import math

h_concentration = float(input("Enter hydrogen ion concentration [H+] in mol/L: "))

if h_concentration <= 0:
    print("Error: concentration must be greater than 0.")
else:
    ph = -math.log10(h_concentration)
    print(f"The pH of the solution is: {ph:.2f}")
