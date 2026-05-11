def is_hexadecimal(hex_string):
    try:
        int(hex_string, 16)
        print("True")
        return True
    except Exception:
        print("False")
        return False

is_hexadecimal("42")
