# JWT and Paseto

- Platform Agnostic Security Tokens are a better solution to JSON Web Tokens.

## Token-Based Authentication

These are the steps:

1. User logs in with their credentials.
2. The app authenticates the user based on the provided credentials.
3. If success, the app generates a token containing information and signature.
   - This acts as a secure representation of the user
4. The app sends this token through the header or the body (also setting cookies from server side)
5. Client saves this token is sessionStorage, localStorage. (Cookies should be set by sercer with HTTPOnly true flag)
6. ...

## JWT

It has 3 parts

- Header

```json
{
  "alg": "HS256",
  "typ": "JWT"
}
```

- Payload

```json
// User and some additional data (expiry date)
{
    "sub": "232323",
    "name": "some name",
    "iat", 3422344,
}

```

- Signature
  - Verifies the token authenticity
  - combining encoded header, encoded payload, a secret, and the specified signing algorithm.

```bash
HMACSHA256(
  base64UrlEncode(header) + "." +
  base64UrlEncode(payload),
  secret)
```

## PASETO

The structure looks like this:

1. Header
    - identifies paseto version and purpose (local or public)
    - specific type of cryptographic alg used

2. Payload
    - Contains claims representing information about an entity (user) 
    - Any additional data

3. Footer
    - additional authenticated data, extra security and context to the token


**It's a string with the segments below:**
- Version
- Type (public OR private)
- Payload -> Put whatever you want here
- Footer

Some common payload attributes
* iss -> issuer
* sub -> subject
* exp -> expiration time
* iat -> issued at
* jit -> token ID 


### Why Paseto?

- Eliminates the risk of algorithm confusion. Devs wouldn't choose unsafe options


### Types:

- Local
    - use symmetric-key cryptography
    - same key is used for both encryption and decryption
    - suitable for server side session management
    - these are simple

You have a json to transmit
you have a secret key
=> you will create a local paseto with these two

one key to both encrypt and decrypt

- Public
    - involved a public key and private key
    - public for encryption and private for decryption
    - These are not encrypted
    - complicated
    - asymmetric

one private and one public key 