from ph_library import calculate_ph
def test_ph():
    assert round(calculate_ph(1), 2) == 0.00
    assert round(calculate_ph(0.1), 2) == 1.00
    assert round(calculate_ph(0.001), 2) == 3.00
    assert round(calculate_ph(0.0000001), 2) == 7.00

    try:
        calculate_ph(0)
        print("Test failed: zero concentration should raise an error.")
    except ValueError:
        print("Zero concentration test passed.")

    try:
        calculate_ph(-1)
        print("Test failed: negative concentration should raise an error.")
    except ValueError:
        print("Negative concentration test passed.")

    print("All pH calculation tests passed.")

test_ph()
