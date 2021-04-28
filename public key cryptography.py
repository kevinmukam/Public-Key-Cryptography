# Network Security
# Public-Key Cryptography
# April 21, 2021

UID = 116430197
Last_Name = "Mukam"
First_Name = "Kevin"

from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_v1_5
import binascii

# --------------------------------- Public Key Encryption ----------------------------#

def rsa_enc_public(inputblock, keypair):
    # inputblock is a plaintext defined as a byte sequence
    plain_text = bytes(inputblock, 'utf-8')

    # The public key extracted from the keypair
    public_key = keypair.publickey()

    # ciphertext is the encrypted data as byte sequence encrypted using the public key
    encryptor = PKCS1_v1_5.new(public_key)
    ciphertext = encryptor.encrypt(plain_text)

    return ciphertext


# --------------------------------- Private Key Decryption ----------------------------#

def rsa_dec_private(cipherblock, keypair):
    # cipherblock is a given ciphertext defined as a byte sequence
    decryptor = PKCS1_v1_5.new(keypair)
    # plaintext is the decrypted data as byte sequence decrypted using the private key
    decrypted = decryptor.decrypt(cipherblock, None)

    return plaintext


# --------------------------- Main code with testing --------------------------#

if __name__ == "__main__":
    plaintext = "Hey guys, this is Kevin."
    keyPair = RSA.generate(2048)  # This line generates the keypair.

    print("The initial message is: ", plaintext)

    # Encrypting with the public key
    encrypted = rsa_enc_public(plaintext, keyPair)
    print("The encrypted version of the message above is: ", encrypted)

    # Decrypting with the private key
    decrypted = rsa_dec_private(encrypted, keyPair)
    print("The original message is: ", decrypted)
