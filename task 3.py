import random

def generatePassword(pwlength):
    """
    Generates random passwords of specified lengths.

    Args:
    pwlength (list of int): List containing lengths of passwords to be generated.

    Returns:
    list of str: List of randomly generated passwords.
    """
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    passwords = [] 

    for length in pwlength:
        password = "" 
        for _ in range(length):
            next_letter_index = random.randrange(len(alphabet))
            password += alphabet[next_letter_index]
        
        password = replaceWithNumber(password)
        password = replaceWithUppercaseLetter(password)
        
        passwords.append(password) 
    
    return passwords


def replaceWithNumber(pword):
    """
    Replaces characters in the password with random numbers.

    Args:
    pword (str): Password string.

    Returns:
    str: Password string with characters replaced by random numbers.
    """
    for _ in range(random.randrange(1, 3)):
        replace_index = random.randrange(len(pword) // 2)
        pword = pword[:replace_index] + str(random.randrange(10)) + pword[replace_index + 1:]
    return pword


def replaceWithUppercaseLetter(pword):
    """
    Replaces characters in the password with random uppercase letters.

    Args:
    pword (str): Password string.

    Returns:
    str: Password string with characters replaced by random uppercase letters.
    """
    for _ in range(random.randrange(1, 3)):
        replace_index = random.randrange(len(pword) // 2, len(pword))
        pword = pword[:replace_index] + pword[replace_index].upper() + pword[replace_index + 1:]
    return pword


def main():
    """
    Main function to generate random passwords based on user input.
    """
    numPasswords = int(input("How many passwords do you want to generate? "))
    print("Generating " + str(numPasswords) + " passwords")
    
    passwordLengths = []
    print("Minimum length of password should be 3")

    for i in range(numPasswords):
        length = int(input("Enter the length of Password #" + str(i + 1) + " "))
        if length < 3:
            length = 3
        passwordLengths.append(length)
    
    passwords = generatePassword(passwordLengths)

    for i, password in enumerate(passwords):
        print("Password #" + str(i + 1) + " = " + password)

if __name__ == "__main__":
    main()
