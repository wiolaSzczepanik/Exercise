def _n_chars(number, sign):
    return number * str(sign)

number = int(input("Enter the number: "))
sign = str(input("Enter the sign: "))
print(_n_chars(number, sign))