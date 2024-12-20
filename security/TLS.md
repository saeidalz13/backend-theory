# TLS

- Transport layer Security
- Web Encryption

TLS is about 3 main things

- Confidentiality -> data can't be read -> Encryption
- Integrity -> If data changes, it is detected -> Hashing
- Authentication -> Verifying client and server are who they claim to be -> Public Key Infrastructure

## Key Players

- Client

  - Entity initiating TLS handshake
  - Web browsers

  * Optionally authenticated (Rare)

- Server

  - Entity receving TLS handshake
  - Apache, IIS, Nginx
  - Load balancer or SSK accelerator
  - Always Authenticated -> it always provides a certificate

- Certificate Authority (CA)
  - How does a server get the certificate?
  - **Certificate Authority**
    - The governing authority that issues the certificates
    - Trusted by both Client and Server
    - Trust Anchor -> Even if client doesn't trust server, because it trusts CA, therefore it trusts server with a valid certificate
    - GoDaddy, IdenTrust, DigiCert, Sectigo, GlobalSign

## Versions

SSL

- 1.0
- 2.0
- 3.0 -> Foundation of TLS
  - introduced concept of certificate chains
  - Added compression capability -> vulnerable tho and not used

and then TLS:

- 1.0
- 1.1
- 1.2
- 1.3

So many cuz:

- Attacks are updated every year!
- Security engineer balances Security Vs. Accessibility

## One Problem

HTTP > TCP > IP > Ethernet \
Where do we put the encryption?

They decided to put TLS between HTTP and TCP \
Basically another layer (header) to the message

## Name

- SSL 3.0 finally changed to TLS
- one standard to rule them all

## How does it work?

It sits on top of TCP (basically has nothing to do with HTTP) and it can be used for other things but HTTP. \
FTPS, HTTPS \

what cipher? (it is communicated)
secret key?
authentication? (at least one of the parties need to be ceritified) -> public key and cryptography
robust? (man in the middle attack, replay attack, downgrade attack)

## TLS Handshake

- To have a protected tunnel between client and server
- handshake is illustrated on a Record by Record basis

  - Records != Packets

- key exchange: RSA
- throughout this process, server and client exchange and calculate values

0. For now Server has its own -> ceritifacte, public key, private key

1. Client hello

   - TLS version -> highest that CLIENT supports
   - random number -> 32 bytes / 256 bits
     - First four bytes -> timestamp
   - Session ID
     - 8 byte / 32 bits
     - all 0's in hello client (for our purpose)
     - the server will generate a session ID with a reference to this
   - Ciphers suites
     - List of Cipher Suites supports
   - Extenstions
     - Any additional extension
     - For now empty
     - Could be various things and might affect the whole process

2. Server responds with server hello
   - **the same five fields\***
   - TLS version -> highest that SERVER supports
   - random number -> 32 bytes / 256 bits
     - First four bytes -> timestamp
   - Session ID
     - 8 byte / 32 bits
     - generated by SERVER to identify ensuing session keys
   - Ciphers suites
     - Cipher Suite selected by SERVER
   - Extenstions
     - Any additional extension
     - For now empty
     - Could be various things and might affect the whole process

Now they both have information about

- TLS version
- Client Random number
- Server Random number
- Session ID
- Cipher Suite

3. Server sends certificate
   - certifiate chain

Now the client knows Certificate and Public Key

4. Server send "HELLO DONE"

- indication that this transaction is done

5. Client needs to ask these from itself

   - Is the certificate legit?
     - based on the signature and the public key
   - Is the server is the true owner of the cert?
     - NOW we get to the next step

6. Client Key Exchange

- Establish Mututal Keying Material (SEED value)
- Proves server is true owner of cert

Both of the goals need **"Pre Master Secret"**. This will be sent **encrypted**.
48 bytes \
-> 2 bytes TLS/SSL version \
-> 46 bytes Random \
Then it is encrypted with **server public key**. This is sent on the wire. the only person who can access it
is the one who has the private key! only SERVER has this!!

**THIS IS RSA Key Exchange**

Server now has "pre master secret"

- It uses the values below to create **"master secret"**
  - Pre Master Secret
  - "master secret" (The literal string)
  - Client Random
  - Server Random

**Both parties now can generate master's secret**
Now it's time for both to generate **session keys**

- What we need is:
  - Master Secret
  - "key expansion" (The literal string)
  - Client Random
  - Server Random
- Four keys are generate
  1. Client Enc Key
  2. Client HMAC key
  3. Server Enc Key
  4. Server HMAC Key

So why 2 sets?

- TLS is creating two separate tunnels - one to protect data from client to server - one to protect data from server to client
  This protects the bulk data. \
  These are the steps to calculate Server and Client I.V. (Initialized Vector?)

7. Client just sent the "Client Key Exchange". Still it doesn't know if Server has calculated the things.
   Neither the SERVER!

Client now sends Change Cipher Spec

- indicates CLIENT has everything necessary to speak securely

8. Client send "Finished"

- Proves to the SERVER taht CLIENT has correct Session Keys
- Client calculates Hash of all Handshake Records seen so far
  **Handshake Hash** comprises of:
  - Client Hello
  - Server Hello
  - Certificate
  - Server Hello Done
  - Client Key Exchange

Then **Verification Data** is created using:

- Master Secret
- "client finished" (literal string)
- handshake hash

Finally, Verification Data gets encrypted with CLIENT session keys \
To have **Encrypted Verification** to be sent on the wire

Since SERVER has the ingredients to generate the env ver, it should be able to generate it itself.

SO:

- Server gets Encrypted Verification from CLIENT
- It decrypts it with its own pair of keys
- Compares to the Verification Data it generated itself
- This also proves they both saw the same handshake records

9. Now, SERVER repeats the step before!!
   "client finished" would be "server finished"

## TLS Handshake (1.2) (Not good)

A lot of cipher suits but the most common -> TLS_ECDHE_RSA_WITH_AES_128_COM_SHA256

ECDHE -> Key exchange (Diffie Hellman) \
RSA -> Public Key authentication mechanism (make sure the server is whoever they say they are) \
**This was the handshake part** \
AES -> Cipher \
128 -> Key size \
SHA256 -> Hash function

1. Client sends hello

   - Conatains Max TLS version that the client can support
   - List of cipher suits

2. Server responds hello
   - Chosen TLS
   - Chosen Cipher suite
   - A random number

- If none of the client TLS or cipher suits version work, the server will send failure message

3. Server sends ceritificate

   - PK attached to it
   - Server key exchange (parameters for Diffie Hellman exchange)
   - Digital signature
   - Finally "server hello done"

4. Now client replies with "client key exchange"
