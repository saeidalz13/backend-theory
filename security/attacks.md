# Attack


## Replay Attacks

Imagine one request that increases the bank account by $100
with TLS, you can't:
- read the data
- change the data
- or spoof (fake who you are)

BUT, you can repeat the same request over and over! 

**This is where TLS impelements Anti-Replay mechanism, the requests are numbered sequentially**. If you wanted to repeat \
the same piece of data, the server will understand.


## Repudiation

Refusing to have anything to do with something. \
Happens when a client sends a message, but refuses to accept that they did!

TLS structure protects us by its essence. Non-Repudiation feature is a by-product of integrity and authentication.