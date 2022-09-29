import string
class Cipher():
    def Cypher(self,input_from_user):
        r=1
        while r==1:
            a=input("Do want to break some ciphers: (Y/N)")
            if a == 'Y':
                print("Which kind of Cipher you want to use :")
                print("1. Caesar Cipher")
                print("2. Base64 Decoder")
                print("3. Vignere Cipher")
                print("4. Exit")
                input_one=int(input("Enter the options from above: "))
                if input_one==1:
                    
                    import platform
                    my_os=platform.system()
                    with open('myOS.txt','w') as file:
                        file.writelines(str(my_os))
                    with open('myOS.txt','r') as file:
                        lines=file.read()
                        first=lines.split('\n',1)[0]
                        print(first)
                        if(first=='Windows'):
                            import os
                            os.system('cls')
                        else:
                            import os
                            os.system('clear')
                    print("Caesar cipher is one of the simplest and most widely known encryption techniques. It is a type of substitution cipher in which each letter in the plaintext is replaced by a letter some fixed number of positions down the alphabet. For example, with a left shift of 3, D would be replaced by A, E would become B, and so on. The method is named after Julius Caesar, who used it in his private correspondence.")
                    print("The encryption step performed by a Caesar cipher is often incorporated as part of more complex schemes, such as the Vigenère cipher, and still has modern application in the ROT13 system. As with all single-alphabet substitution ciphers, the Caesar cipher is easily broken and in modern practice offers essentially no communications security. Source: Wikipedia")
                    def caesar(text, shift, alphabets):
                        def shift_alphabets(alphabet):
                            return alphabet[shift:]+alphabet[:shift]
                        shifted_alphabets=tuple(map(shift_alphabets, alphabets))
                        final_alphabets=''.join(alphabets)
                        final_shifted_alphabet=''.join(shifted_alphabets)
                        table=str.maketrans(final_alphabets,final_shifted_alphabet)
                        return text.translate(table)
                    plain_text=input("Enter the Cipher/Plain Text to Encode/Decode: \n")
                    b=int(input("Enter the number to use the shift: \n"))
                    if(b<=26):
                        print(caesar(plain_text,b,[string.ascii_lowercase, string.ascii_uppercase, string.punctuation]))
                    else:
                        print("Enter a value below or equal to 26")
                elif input_one==2:
                    import platform
                    my_os=platform.system()
                    with open('myOS.txt','w') as file:
                        file.writelines(str(my_os))
                    with open('myOS.txt','r') as file:
                        lines=file.read()
                        first=lines.split('\n',1)[0]
                        print(first)
                        if(first=='Windows'):
                            import os
                            os.system('cls')
                        else:
                            import os
                            os.system('clear')
                    print("""In computer programming Base64 is a group of binary-to-text encoding schemes that represent binary data more specifically a sequence of 8-bit bytes in sequences of 24 bits that can be represented by four 6-bit Base64 digits.Common to all binary-to-text encoding schemes Base64 is designed to carry data stored in binary formats across channels that only reliably support text content. Base64 is particularly prevalent on the World Wide Web where one of its uses is the ability to embed image files or other binary assets inside textual assets such as HTML and CSS files.Base64 is also widely used for sending e-mail attachments. This is required because SMTP in its original form was designed to transport 7-bit ASCII characters only. This encoding causes an overhead of 33 to 37% (33 by the encoding itself; up to 4% more by the inserted line breaks).Source: Wikipedia""")
                    import base64
                    a=input("Enter the Text: ")
                    y=bytes(a,"utf-8")
                    print(y)
                    s=int(input("Choose from the following options:\n 1. To Encode the Text\n 2. To Decode the Text\n"))
                    if(s==1):
                        z=base64.b64encode(y)
                        print(z)
                    if(s==2):
                        a=base64.b64decode(z)
                        print(a)

                elif input_one==3:
                    print("""The Vigenère cipher is a method of encrypting alphabetic text by using a series of interwoven Caesar ciphers, based on the letters of a keyword. It employs a form of polyalphabetic substitution.First described by Giovan Battista Bellaso in 1553, the cipher is easy to understand and implement, but it resisted all attempts to break it until 1863, three centuries later. This earned it the description le chiffrage indéchiffrable (French for 'the indecipherable cipher'). Many people have tried to implement encryption schemes that are essentially Vigenère ciphers. In 1863, Friedrich Kasiski was the first to publish a general method of deciphering Vigenère ciphers. Source: Wikipedia""")
                    import platform
                    my_os=platform.system()
                    with open('myOS.txt','w') as file:
                        file.writelines(str(my_os))
                    with open('myOS.txt','r') as file:
                        lines=file.read()
                        first=lines.split('\n',1)[0]
                        print(first)
                        if(first=='Windows'):
                            import os
                            os.system('cls')
                        else:
                            import os
                            os.system('clear')
                    print("""The Vigenère cipher is a method of encrypting alphabetic text by using a series of interwoven Caesar ciphers, based on the letters of a keyword. It employs a form of polyalphabetic substitution.

First described by Giovan Battista Bellaso in 1553, the cipher is easy to understand and implement, but it resisted all attempts to break it until 1863, three centuries later. This earned it the description le chiffrage indéchiffrable (French for 'the indecipherable cipher'). Many people have tried to implement encryption schemes that are essentially Vigenère ciphers. In 1863, Friedrich Kasiski was the first to publish a general method of deciphering Vigenère ciphers. Source: Wikipedia""")
                    def _pad_key(plaintext, key):
                        padded_key = ''
                        i = 0
                        for char in plaintext:
                            if char.isalpha():
                                padded_key += key[i % len(key)]
                                i += 1
                            else:
                                padded_key += ' '
                        return padded_key

                    def _encrypt_decrypt_char(plaintext_char, key_char, mode='encrypt'):
                        if plaintext_char.isalpha():
                            first_alphabet_letter = 'a'
                            if plaintext_char.isupper():
                                first_alphabet_letter = 'A'
                                old_char_position = ord(plaintext_char) - ord(first_alphabet_letter)
                                key_char_position = ord(key_char.lower()) - ord('a')
                                if mode == 'encrypt':
                                        new_char_position = (old_char_position + key_char_position) % 26
                                else:
                                    new_char_position = (old_char_position - key_char_position + 26) % 26
                                return chr(new_char_position + ord(first_alphabet_letter))
                        return plaintext_char
                    def encrypt(plaintext, key):
                        ciphertext = ''
                        padded_key = _pad_key(plaintext, key)
                        for plaintext_char, key_char in zip(plaintext, padded_key):
                            ciphertext += _encrypt_decrypt_char(plaintext_char, key_char)
                        return ciphertext
                    def decrypt(ciphertext, key):
                        plaintext = ''
                        padded_key = _pad_key(ciphertext, key)
                        for ciphertext_char, key_char in zip(ciphertext, padded_key):
                            plaintext += _encrypt_decrypt_char(ciphertext_char, key_char, mode='decrypt')
                        return plaintext

                    plaintext = input('Enter a message: ')
                    key = input('Enter a key: ')

                    ciphertext = encrypt(plaintext, key)
                    decrypted_plaintext = decrypt(ciphertext, key)

                    print(f'Ciphertext: {ciphertext}')
                    print(f'Decrypted Plaintext: {decrypted_plaintext}')
                else:
                    r=2
            else:
                r=2

