def caesar_decoder(message, offset):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    punctuation = ".,?'! "
    translated_message = ""
    for letter in message:
        if not letter in punctuation:
            letter_value = alphabet.find(letter)
            translated_message += alphabet[(letter_value + offset) %26]
        else:
            translated_message += letter
    return translated_message

message = "dej fuddo'i reqj"
offset=10
print(caesar_decoder(message,offset))

def caesar_coder(message,offset):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    punctuation = ".,?'! "
    translated_message = ""
    for letter in message:
        if not letter in punctuation:
            letter_value = alphabet.find(letter)
            translated_message += alphabet[(letter_value - offset) %26]
        else:
            translated_message += letter
    return translated_message

message = "we have to go back, kate. we have to go back!"
offset = 10
print(caesar_coder(message,offset))

def vigenere_decoder(coded_message, keyword):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    punctuation = ".,?'! "
    letter_pointer = 0
    keyword_final = ''
    for i in range(0,len(coded_message)):
        if coded_message[i] in punctuation:
            keyword_final += coded_message[i]
        else:
            keyword_final += keyword[letter_pointer]
            letter_pointer = (letter_pointer+1)%len(keyword)
    translated_message = ''
    for i in range(0,len(coded_message)):
        if not coded_message[i] in punctuation:
            ln = alphabet.find(coded_message[i]) - alphabet.find(keyword_final[i])
            translated_message += alphabet[ln % 26]
        else:
            translated_message += coded_message[i]
    return translated_message

message = "dcpn a ssmlzv gg aguaefk, emfi n egnmnr'f ehymrvfy xwnsf, ay az iiwj gfte n exwn, m'yd vi fwygzbrb jbj qiz"
keyword = "sufjanstevens"

print(vigenere_decoder(message, keyword))

def vigenere_coder(message, keyword):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    punctuation = ".,?'! "
    letter_pointer = 0
    keyword_final = ''
    for i in range(0,len(message)):
        if message[i] in punctuation:
            keyword_final += message[i]
        else:
            keyword_final += keyword[letter_pointer]
            letter_pointer = (letter_pointer+1)%len(keyword)
    translated_message = ''
    for i in range(0,len(message)):
        if message[i] not in punctuation:
            ln = alphabet.find(message[i]) + alphabet.find(keyword_final[i])
            translated_message += alphabet[ln % 26]
        else:
            translated_message += message[i]
    return translated_message

message_from_ben = "you'll understand soon enough that there are consequences to being chosen, because destiny, john, is a fickle bitch"
ben_keyword = "lost"

print(vigenere_coder(message_from_ben,ben_keyword))
print(vigenere_decoder(vigenere_coder(message_from_ben, ben_keyword), ben_keyword))

