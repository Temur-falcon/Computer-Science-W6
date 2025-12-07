from cs50 import get_int

def main():
    while True:
        h = get_int("Height: ")
        if 1 <= h <= 8:
            break

    for i in range(1, h + 1):
        # Left spaces
        print(" " * (h - i), end="")
        # Left pyramid
        print("#" * i, end="")
        # Gap
        print("  ", end="")
        # Right pyramid
        print("#" * i)


if __name__ == "__main__":
    main()
