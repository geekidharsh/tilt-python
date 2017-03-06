# Write a module that enables the robots to easily recall their passwords through codes when they return home.
# The cipher grille and the ciphered password are represented as an array (tuple) of strings.
# Input: A cipher grille and a ciphered password as a tuples of strings.
# Output: The password as a string.

# Precondition: len(cipher_grille) == 4
# len(ciphered_password) == 4
# all(len(row) == 4 for row in ciphered_password)
# all(len(row) == 4 for row in cipher_grille)
# all(all(ch in string.ascii_lowercase for ch in row) for row in ciphered_password)
# all(all(ch == "X" or ch == "." for ch in row) for row in cipher_grille)