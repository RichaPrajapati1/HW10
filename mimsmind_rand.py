def get_randomdigit_Prajapati(length):
    # Generates a random string of the specified number of digits
    return ''.join(random.choice(string.digits) for _ in range(length))