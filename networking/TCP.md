# TCP

Source: \
**YouTube Channel: Practical Networking**
The purpose of Layer 4 is service to service delivery.

## Core attributes

### Connection Oriented

- There is an official "start" and "end" unlike UDP.

### Reliable

- Provides confirmation of data delivery (recipient sends it)
- Sender is aware of errors
- Data is delivered in order
  - Segments are labeled

### Flow Control

- Adjusts transmission rate to safely use max available bandwidth without exceeding it
  - The bandwidth is different throughout the path of the packets
  - This difference might cause packet loss. TCP controls and adjusts this

### More overhead

- Size of the header added to the data (from 5, 6, and 7 layers)
  - Makes sense! It has more featurs such as sequence number, ack number, TCP flags, etc.

## Debunking Myths

1. "UDP is faster"

- Speed is actually identical!!
- What affects speed is **latency** which is unaffected by TCP or UDP
- It just has less overhead

2. "TCP is more secure"

- This is WRONG!
- Security is identical
- SSL is the security! (IPSec or SSL)

3. "UDP is unreliable"

- UDP doesn't provide reliablity at L4
- The odds of delivery is identical

4. "TCP is guaranteed delivery"

- TCP just provides confirmation!!
- If something is wrong with the wire, TCP doesn't guarantee shit!
- It does have retransmission

## 12 Ideas That Capture TCP

### Sequence and Ackbnowledgment number

- seq tracks what is sent
- ack tracks what is received

Side note: seq/ack numbers are a measure of bytes NOT packets

1. First

- seq = 1001 [200 bytes]
  So consider each [] as a byte. These will be 200 bytes
  [1201][1202][1203][1204][1205]...[1396][1397][1398][1399][1400]
- ack - 1201 (1001 + 200)
  This means I'm ready for byte "1201"

2. Second

- seq = 1201 [200 bytes]
- ack = 1401 (1201 + 200)

3. Third

- seq = 1401 [100 bytes]
- ack = 1501 (1401 + 100)

### Retransmission

- TCP caches everything sent for duration of "Retransmission Timeout".
- if no ACK is received, segment is resent.

1. Alice sends seq = 1501 [200 bytes]
2. She creates a cache of this with a timeout and waits for Bob.
3. Bob sends 1701 ack back to Alice
4. Alice now clears the cache and timeout knowing that Bob has the package

**If Alice didn't receive ACK, Alice will retransmit it**

NOTE: If Alice timeout runs out and Bob still hasn't sent back anything, Alice will send the packet again \
This will cause Bob to have a duplicate. In this way Bob knows Alice didn't receive his ACK. So he will \
resend it.

### Delayed Acknowledgement

Initially, we said that there was an ACK with every SEQ \
But now we can discuss the delayed ack for this. \
ACK is sent every other segment

Example:

Alice sends the packet below:
seq = 1001 [200 bytes] \
AND \
seq = 1201 [200 bytes]

Now -> Bob sends ACK = 1401

BUT what if odd number of segments?

- There is a timeout of 500 ms.
- even if odd number, ACK is sent

### Window Size ("bytes is flight")

How much data can the sender can send until ACK is received?

- Bob (Receiver) detemines this "Window Size" (let's say 500 bytes)

1. Alice sends

- seq = 1001 [200 bytes] -> window size = 300
- seq = 1201 [200 bytes] -> window size = 100
- seq = 1401 [100 bytes] -> window size = 0
  no more to send!

2. Bob now sends ACK

- ack = 1501

3. Alice window size resets to 500

### Window size is sent in each segment (it's in header)

- **But how did Alice know before Bob sent the window size?**
- more on this later...

This window size is in addition to delayed ACK.

This is resulting in dynamically updated through connection (Flow Control) \
Window size can go up or down to 0! (if Bob is too busy with other tasks) \

Receiver is always fine tuning the flow.

### TCP is bidirectional

- Both peers have SEQ and ACK.

1. Alice sends SEQ = 1001 | ACK = 3001 [200 bytes]
2. Bob sends SEQ = 3001 | ACK = 1201 [300 bytes]
   - Bob has SEQ alongside with ACK.
   - He is just sending something else
3. Bob again sends SEQ = 3301 | ACK - 1201 [300 bytes]
   - Only SEQ has changed but not ACK
4. Alice sends SEQ = 1201 | ACK = 3601 [200 bytes]
   - Alice is acknowledging the reception of segment WHILE sending another SEQ

**Each party can send "0 bytes ack" -> SEQ = 1001 | ACK = 1601 [0 bytes]** \
**After 3. we have duplicate ACKs**

### Initial Sequence Numbers (ISN)

- Each sender chooses a random SEQ
- These random numbers are chosen shared through the handshake

**-> The core purpose of the 3-way handshake is to exchange these sequence numbers <-**

### How does the connection start?

It includes 4 events:

1. Alice sends a SYN with a ISN [x] to share with Bob
2. Bob sends a ACK with readiness of [x + 1]
   - Bob also sends SYN with ISN of [y]
3. Alice sends a ACK with the readiness for [y + 1]

So let's say an example

1. Alice sends SEQ = 1000 | ACK = 0000 [0 bytes] -> With flag of S

   - 1000 is ISN

2. Bob sends back SEQ = 3000 | ACK = 1001 [0 bytes] -> with flag of A and S

3. Alice sends SEQ = 1001 | ACK = 3001 [0 bytes] -> With flag of A

What about Receive Window Size?

1. In this alongside SEQ and ACK, Alice sends a random [WIN n] where n is a random integer
2. Bob sends [WIN m] where m is a random integer

#### Phantom byte

Notice in the stages, Alice sent SEQ=1000 but with 0 bytes. Bob sent back the ACK and next time, \
Alice sent the SEQ=1001. But no bytes were sent in the first place!! \
This is called a **phantom byte**. Although no data was sent, ACK had to be sent anyways. So, we'd \
have this increse by one even though no data was transmitted.

**You should know that in all the segments, ACK flag is always on EXCEPT FOR the intial sender SYN**

### Connection End

Two ways to do this:

1. Graceful method
   - Using FIN flag (F)
2. Ungraceful
   - Using RST flag (R)

#### Graceful

Four-way closure:

1. One side sends flag F with last sequence number of X
2. The other side sends ACK with X + 1
3. The other side sends FIN with Y
4. One side sends ACK Y + 1

**Phantom byte also happens here!**

#### Ungraceful

One-way with RST flags, when something goes wrong (Eject seat!!)

- Either of the party sends RST and TCP is gone!
- **RST is unacknowledged**
