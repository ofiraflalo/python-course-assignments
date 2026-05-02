from ph_library import calculate_ph
try:
    h_concentration = float(input("Enter hydrogen ion concentration [H+] in mol/L: "))
    ph = calculate_ph(h_concentration)
    print(f"The pH of the solution is: {ph:.2f}")
except ValueError as error:  
    print(f"Error: {error}")
