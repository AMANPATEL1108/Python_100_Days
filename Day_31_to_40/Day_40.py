import random
import string

def generate_random_chars():
    return ''.join(random.choices(string.ascii_letters + string.digits, k=3))

def encode(message):
    words = message.split()
    encoded_words = []
    for word in words:
        if len(word) >= 3:
            random_chars = generate_random_chars()
            encoded_word = random_chars + word[1:] + word[0] + generate_random_chars()
            encoded_words.append(encoded_word)
        else:
            encoded_words.append(word[::-1])
    return ' '.join(encoded_words)

def decode(message):
    words = message.split()
    decoded_words = []
    for word in words:
        if len(word) < 3:
            decoded_words.append(word[::-1])
        else:
            word = word[3:-3]
            decoded_word = word[-1] + word[:-1]
            decoded_words.append(decoded_word)
    return ' '.join(decoded_words)

def main():
    action = input("Do you want to 'encode' or 'decode'? ").strip().lower()
    message = input("Enter your message: ").strip()

    if action == 'encode':
        print("Encoded message: ", encode(message))
    elif action == 'decode':
        print("Decoded message: ", decode(message))
    else:
        print("Invalid choice! Please choose either 'encode' or 'decode'.")

if __name__ == "__main__":
    main()
