# Cryptographic signing

Cryptographic signing, also known as digital signing, is a process used to prove the authenticity and integrity of data, ensuring that the data hasn’t been tampered with and that it was created by the known sender. It involves the use of asymmetric cryptography (public-key cryptography).

## How?

1. Sender hashes the message or the document
2. Sender encrypts the resulting hash using a private key
   - **This is the digital signature**
3. Recipient can verify the signature using senders' public key.

## Digital signatures

- Verify the identity of the people in the conversation
- I have someting that I want to send u but a proof that IIIIIII send it
- The recipient needs a way to know if it was me

### Signer

- We have a thing (doc, file, string)
- Encrypt it with private key -> signature
- Send the signature over the internet

BUT!! The problem is

- what if the doc is too large!
- or actually very very short (Encrytion of "1" with any type and key is "1")

**we're going to insert a Hash Function**

- Any message length to 256 bits for instance (SHA256)
- Maybe we add paddings
- **NOW we can encrypt the hashed value**

### Verifier

- Decrypt the signature with the pubic key
