import re
import os

# plaintext = 'q2z'
# key = '#w>'

def readFile(path):
    with open(path, 'r') as file:
        contents = file.read()

    return contents

def writeFile(path, content):
    with open(path, 'w', encoding='utf-8') as file:
        file.write(str(content))

def toBinary(string):
    binaryChars = []

    for letter in string:
        binaryLetter = f'{ord(letter):08b}'
        binaryChars.append(binaryLetter)
    
    binaryString = ''.join(binaryChars)

    return binaryString

def toString(binaryText):
    text = ''

    binaryText = re.findall('........', binaryText)
   
    for binaryValue in binaryText:
        ascii_int = int(binaryValue, 2) 
        ascii_char = chr(ascii_int)

        text += ascii_char

    return text

def generateKey(string, length): 
    if(len(string) >= length):
        return string[:length]

    key = (string * (length // len(string) + 1))[:length]

    return key

def encrypt(plainText, key):
    ciphertext = []
    binaryPlainText = toBinary(plainText)
    binaryKey = toBinary(key)

    for index in range(len(binaryPlainText)):
        if(binaryPlainText[index] != binaryKey[index]):
            ciphertext.append('1')
        else:
            ciphertext.append('0')
    
    ciphertext = ''.join(ciphertext)
    ciphertext = toString(ciphertext)   
    
    return ciphertext

def encriptionMenu():
    file = input('Informe o nome_do_arquivo.txt: ')
    key_pattern = ''

    while(len(key_pattern) > 12 or len(key_pattern) < 1):
        key_pattern = input('Informe a chave padrão (limite de caracteres: 12): ')

    plain_text = readFile(file)
    key = generateKey(key_pattern, len(plain_text))

    encrypted_text = encrypt(plain_text, key)

    file_name = os.path.splitext(os.path.basename(file))[0]

    writeFile( f'./output/{file_name}_encripted.txt', encrypted_text)

def menu():
    while True:
        print("\n1 - Encriptar Mensagem")
        print("2 - Sair\n")
        option = input('Escolha a opção: ')

        if option == "2":
            break

        match option:
            case '1':
                encriptionMenu()

menu()



