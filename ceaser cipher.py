def caesar_cipher(text, shift, mode='encrypt'):
    
    if mode == 'decrypt':
        shift = -shift
    
    result = ""
    for char in text:
        if char.isalpha():
            shift_amount = shift % 26
            start = ord('A') if char.isupper() else ord('a')
            char = chr(start + (ord(char) - start + shift_amount) % 26)
        result += char

    return result

# Example usage:
plaintext = "Hello, World!"
shift = 3

# Encrypting the plaintext
encrypted_text = caesar_cipher(plaintext, shift, mode='encrypt')
print(f"Encrypted: {encrypted_text}")

# Decrypting the ciphertext
decrypted_text = caesar_cipher(encrypted_text, shift, mode='decrypt')
print(f"Decrypted: {decrypted_text}")
