import re
import os
import argparse

def readFile(path):
    try:
        with open(path, 'r', encoding = 'utf-8') as file:
            contents = file.read()
        return contents
    except FileNotFoundError:
        print(f"O arquivo {path} não foi encontrado.")
        exit()
    except IOError:
        print(f"Não foi possível ler o arquivo {path}.")
        exit()

def writeFile(path, content):
    try:
        directory = os.path.dirname(path)
        
        if not os.path.exists(directory):
            os.makedirs(directory)

        with open(path, 'w', encoding ='utf-8') as file:
            file.write(str(content))
    except IOError as error:
        print(f"Não foi possível escrever no arquivo {path}: {error}")


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

        text +=  ascii_char

    return text

def generateKey(string, length): 
    if(len(string) >= length):
        return string[:length]
    
    key = (string * (length // len(string) + 1))[:length]
 
    return key

def xor(binaryString, binaryKey):
    xor_result = ''
    
    for index in range(len(binaryString)):
        if(binaryString[index] != binaryKey[index]):
            xor_result += '1'
        else:
            xor_result += '0'
    
    xor_result = ''.join(xor_result)
    xor_result = toString(xor_result) 

    return xor_result

def encrypt(filePath, key_pattern):
    plain_text = readFile(filePath)
    key = generateKey(key_pattern, len(plain_text))

    binaryPlainText = toBinary(plain_text)
    binaryKey = toBinary(key)
   
    encrypted_text = xor(binaryPlainText, binaryKey) 

    file_name = os.path.splitext(os.path.basename(filePath))[0]

    writeFile( f'./output/{file_name}_cripto.txt', encrypted_text)
 
def decrypt(file_path, key_pattern): 
    encrypted_text = readFile(file_path)
    key = generateKey(key_pattern, len(encrypted_text)) 

    binaryEncryptedText = toBinary(encrypted_text)
    binaryKey = toBinary(key)

    decrypted_text = xor(binaryEncryptedText, binaryKey)

    file_name = os.path.splitext(os.path.basename(file_path))[0]

    writeFile( f'./output/{file_name}_decrypted.txt', decrypted_text)
    
parser = argparse.ArgumentParser(description='Encryption')
parser.add_argument('filename', nargs='?', default='', help='Caminho do arquivo')
parser.add_argument('key',  nargs='?',  default='', help='Chave de criptografia (max. 12 caracteres)')
parser.add_argument('-a', '--action', help='Ação escolhida (encrypt | decrypt)')
args = parser.parse_args()

def main(args):
    file_name = args.filename
    key = args.key
    action = args.action

    if len(key) > 12:
        print(f"Chave [ {key} ] precisa ter menos de 12 caracteres.")
        exit()

    if action == 'encrypt':
        encrypt(file_name, key)
    if action == 'decrypt':
        decrypt(file_name, key)

main(args)



