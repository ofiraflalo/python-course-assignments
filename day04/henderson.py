def henderson_ratio(ph, pka):
    """
    Calculate the ratio [A-]/[HA] using Henderson-Hasselbalch equation
    """
    return 10 ** (ph - pka)
