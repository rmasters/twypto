from Crypto.PublicKey import RSA
from Crypto import Random


class PostFactory:
    def create(self, message, fromUser, toUser):
        """
        With public-key encryption, we input a plain text and encryption key,
        we output a derived public key and encrypted text
        """

        ciphertext = toUser.publicKey.encrypt(message, 32)

        return ciphertext

    def read(self, post, privateKey):
        if privateKey:
            return privateKey.decrypt(post.cipherText)

        return "encrypted"


class Keyring:
    def __init__(self):
        self.keys = {}

    def add(self, username, privateKey):
        self.keys[username] = privateKey

    def get(self, username):
        return self.keys[username] if username in self.keys else None
    
    def generate(self, username):
        random_generator = Random.new().read
        key = RSA.generate(1024, random_generator)

        self.add(username, key)

        return self.get(username)

