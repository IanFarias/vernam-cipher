# vernam-cipher

Vernam cipher algorithm bitwise XOR with Python 3.11.2

# About

https://adacomputerscience.org/concepts/encrypt_vernam?examBoard=all&stage=all
https://www.geeksforgeeks.org/vernam-cipher-in-cryptography/
https://wiki.imesec.ime.usp.br/books/ctf-starter-pack/page/one-time-pad

# Inputs

- A plain text message (\*.txt File)
- A Key with maximum length of 12 characters
- Script action (encrypt or decrypt)

In order to facilitate usability, it was defined that only a key with a maximum length of 12 characters can be sent as a parameter. If the plain text message has a longer length, the key is completed with itself until it reaches the length of the plain text message.

# Outputs

- The encrypted file is save in the "output" directory: ./output/file_name_cripto.txt
- The decrypted file is save in the "output" directory: ./output/file_name_decrypted.txt

# Commands

Run script

```
python vernam.py <file.txt> "<key>" -a <encrypt | decrypt>
```

Help

```
python vernam.py --help
```

# Example

message.txt = "q2z"

Encrypt

```
python vernam.py message.txt "#w>" -a encrypt

/*
 Result: RED
*/
```

Decrypt

```
python vernam.py ./output/message_cripto.txt "#w>" -a decrypt

/*
 Result: q2z
*/
```
