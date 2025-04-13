def caesar_cipher(word, shift):
    
    text = ""
    
    for char in word:
        if char.isalpha():
            
            if char.isupper():
                x = ord('A')  
            else:
                x = ord('a')
            
            text += chr((ord(char) - x + shift) % 26 + x)
        else:
            text += char

    return text

def all_shifts(word):
    
    for shift in range(1,26):
        encrypted_text = caesar_cipher(word, shift)
        print(f"{shift} : {encrypted_text}")

all_shifts("mohammed")
