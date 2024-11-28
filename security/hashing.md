# Hashing

Mathemtical formula that takes an input and produces an output a "fingerprint" of the original message.

Let's say we have a hashing algorithm that works like this:

- With a given string, it sees what number of the alphabet each letter is and sums it up to have our hash.
- Hello
  - 8 + 5 + 12 + 12+ 15 = 52
  - **our hashed value from hellow is 52**
  - **the result of a hashing alg is referred to as "digest" (also hash, checksum, fingerprint, CRC, etc.)**

You can compare if two messages to see if they're the same.
So:
- If you change "hello" to "cello", your digest will be 47!
- That means that the message has been tampered with

Real world algs must satisfy the requirements of:
- Infeasible to find out the algorithm
- Imposisble to get the original message 
- Slight change to message will produce a drastic different digest
- Resulting digest must be the same length (avalanche effect)

## Collisions

- Two messages resulting in idential digests!
- They're unavoidable as it's a by product of the feature "fixed width digest"
- but we can make them rare
  - Higher bit outputs -> more secure and rare possibility of collisions

## Types
- MD5 -> 128 bits
- SHA/SHA1 -> 160 bits
- SHA2 Family (numbers are bits):
  * SHA-224
  * SHA-256
  * SHA-384
  * SHA-512


## Data Integrity

Simply hashing something and sending it over the wire ain't cut. \
with a man-in-the-middle attack, they can just guess the hashing alg and produce a new message.

You need to add a secret to the message and then hash it!

### Message Authentication Code (MAC)

- Combining message and secret key when calculating digest
- Provides integrity and authentication
 
Now it matters how you combine the message and secret! For this we have a standard.

#### Hash based Message Authentication Code (HMAC)

This is the industry implementation. (RFC 2104)

## Salting

Hashing often uses "salt" -> A random data added to the input
- This makes it even more secure
- Hashing is used for data verification and is NOT reversible

## Extra

They have 3 major features

1. They have to be fast (big files in a second or 2) BUT not too fast!
2. One bit gets flipped, you'd have the avalanch effect
3. No collisions -> two contents should never have the same hash

### SHA1

- **Not for passwords**

  - file verification

- Takes a string and ALWAYS spits out 160 bits (160 zeros and ones)

### Types

#### Document Hashing

To ensure accuracy

Think of hashing as a digital signature.

#### Password Hashing

There is thing called rainbow tables. A huge table of cracked hashes. Hackers have all the easy ones!
What we can do is use "salt".
Adding a unique string to the password and then hashing.

`bcrypt` is designed to be slow!! to make it secure
