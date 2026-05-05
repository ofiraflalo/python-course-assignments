import sys
from ph_library import calculate_ph
try:
    if len(sys.argv) != 2:
        print("Usage: python ph_command_line.py <hydrogen_concentration>")
    else:
        h_concentration = float(sys.argv[1])
        ph = calculate_ph(h_concentration)
        print(f"The pH of the solution is: {ph:.2f}")

except ValueError as error:
    print(f"Error: {error}")
