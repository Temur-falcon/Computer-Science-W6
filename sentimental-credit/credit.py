from cs50 import get_string

def luhn(card_number):
    total = 0
    reverse = card_number[::-1]

    for i, digit in enumerate(reverse):
        n = int(digit)
        if i % 2 == 1:
            n *= 2
            if n > 9:
                n -= 9
        total += n

    return total % 10 == 0

def main():
    number = get_string("Number: ")

    # Check if all digits
    if not number.isdigit():
        print("INVALID")
        return

    # Luhn check
    if not luhn(number):
        print("INVALID")
        return

    length = len(number)
    start2 = int(number[:2])
    start1 = int(number[0])

    # Check card type
    if length == 15 and (start2 == 34 or start2 == 37):
        print("AMEX")
    elif length == 16 and 51 <= start2 <= 55:
        print("MASTERCARD")
    elif (length == 13 or length == 16) and start1 == 4:
        print("VISA")
    else:
        print("INVALID")


if __name__ == "__main__":
    main()
