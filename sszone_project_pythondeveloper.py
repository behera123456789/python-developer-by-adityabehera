class TranspositionCipher:
    def __init__(self, key):
        self.key = key
    def encrypt(self, plaintext):
        num_columns = len(self.key)
        num_rows = -(-len(plaintext) // num_columns)
        plaintext += ' ' * (num_columns * num_rows - len(plaintext))
        grid = [['' for _ in range(num_columns)] for _ in range(num_rows)]
        for i in range(len(plaintext)):
            row = i // num_columns
            col = i % num_columns
            grid[row][col] = plaintext[i]
        encrypted_message = ''
        for col in self.key:
            col_index = int(col) - 1
            for row in range(num_rows):
                encrypted_message += grid[row][col_index]

        return encrypted_message
cipher = TranspositionCipher('2413')
plaintext = "This is a secret message"
encrypted_message = cipher.encrypt(plaintext)
print("Encrypted message:", encrypted_message)