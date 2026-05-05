from henderson import henderson_ratio

try:
    ph = float(input("Enter pH: "))
    pka = float(input("Enter pKa: "))

    ratio = henderson_ratio(ph, pka)

    print(f"[A-]/[HA] ratio is: {ratio:.2f}")

    if ph > pka:
        print("Base (A-) is dominant")
    elif ph < pka:
        print("Acid (HA) is dominant")
    else:
        print("Equal amounts")

except ValueError:
    print("Invalid input")
