# Encryption

This algorithm is used to provide confidentiality. Meaning only the recepient is able to read it.

## Simple Enc and Problems

The diagram of a **simple encryption**:

(or clear text)
[**plain text**] ----(enc alg)----> [**cipher text**]

Problems:

1. Doesn't scale
2. Hard to do securely
3. Cannot use a standard algorithm

## Key based enc

Combines industry vetted alg with a secret key.

- Algs are by mathematicians
- Secrets are generated randomly

### Symmetric (one key)

Let's imagine this. We have the alphabet.
abcdefjhijklmnopqrstuvwxyz

let's say that our algorithm is to move each letter of the message by n to the right.

Enc:
hello ----(n=3)----> khoor

Dec:
khoor ----(n=3)----> hello

So same key was used for both enc and dec.

Algs:
inscure:
- DES
- RC4
- 3DES
secure:
- AES
- ChaCha20

### Asymmetric (different keys)

Similar to sym, let's say we work with the alphabet. \
But this time you can't go backwards that amount. This is designed by mathematicians and the algs are **trap door** algs. \
These are mathemtical operations that are one-way!

Enc: \
hello ----(n=5)----> mjqqt \

Dec: \
mjqqt ----(n=21)---> hello \

now we have to go 21 forward again to reach the original message.

Features: \

1. enc and dec keys here are **mathematically related**

- What's enc with first key, can ONLY be dec using the specific dec key.

2. Industy does this

- One key will be made public
- One key will be private

Algs:
- DSA
- RSA
- Diffie-Hillman
- ECDSA (elliptive curve)
- ECDH


### Public and Private Key

Confidentiality:
- Jim and Pam both have their own public and private key
  - Remember, what's encrypted with one's public key can only be decrypted with their private key
- Jims uses Pam's public key to encrypt a message (**Confidentiality**)
  - The message can be sent over the wire since only Pam can decrypt it


Authentication:
- Pam wants to send a message but doesn't care if someone reads the messsage
  - She just wants to prove that she was the sender
- Now if Jim encrypts the message successfully with Pam's public key
  * It proves Pam must have sent the message (Authentication)
  * Jim knows message was not modified (Integrity)

BUT, since the message could be long, so we **hash** it first and then encrypt it.
This is **Signature**.

BUT limitation:
- Asymm enc is expensive
- Bulk data should be protected with Symmetric Enc
  - But the problem with that is transferring that one key securely to other party
**Why don't we use Asym keys to share Sym keys?** \
**That's what SSL/TLS actually does!!** \
**This is also called Hybrid Encryption**




## Purpose

- Transforms data into a different format (cipher text)
- It's to protect its confidentiality
- Only authorized parties can read the data

## Reversibility

- This is a **two-way** function
  - data is encrypted into ciphertext.
  - decrypted back to its original using a key

## Use Cases

- To secure senstitive data (emails, messages, files)
- we make them unreadable

## Examples

- AES
- RSA
- DES
