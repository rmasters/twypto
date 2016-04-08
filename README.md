# Twypto: encrypted Twitter

This is a proof of concept of a Twitter-style messaging service that uses
public-key encryption. Each broadcast creates a new post for a follower that is
encrypted with their public key.

## Todo

* Add a backend (or some sort of storage)
* Allow for client-side decryption (get ciphertext)
