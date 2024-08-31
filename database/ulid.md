# ULID

ULID (Universally Unique Lexicographically Sortable Identifier) is a specific type of unique identifier that provides both uniqueness and lexicographical sorting. It was designed to overcome some of the limitations of UUIDs (Universally Unique Identifiers) while maintaining the ability to generate IDs in a distributed environment.

How ULID Works Under the Hood
A ULID is composed of two main components: a timestamp and randomness. The total length of a ULID is 26 characters, and it's encoded in a base32 format, making it URL-safe and easy to use in various contexts.

1. Structure of a ULID

A ULID is typically represented as a 26-character string, where:

The first 10 characters represent the timestamp.
The remaining 16 characters represent randomness.
Example ULID: 01H4Z5TP9RB2VXFA7EJ9ZNM1ZJ

This ULID can be broken down into:

01H4Z5TP9R: Timestamp part (10 characters)
B2VXFA7EJ9ZNM1ZJ: Random part (16 characters) 2. Timestamp Component

The first part of the ULID encodes the timestamp:

Bits: 48 bits (6 bytes) are allocated for the timestamp.
Time: The timestamp represents the number of milliseconds since the Unix epoch (1970-01-01T00:00:00Z).
Encoding: This 48-bit number is converted into 10 characters using a base32 encoding (which uses the characters 0123456789ABCDEFGHJKMNPQRSTVWXYZ).
Why is this useful?

The timestamp ensures that ULIDs generated later will sort after those generated earlier, even if they come from different systems.
Example:

A timestamp might be 1692304000000 milliseconds since the Unix epoch.
This is encoded into the base32 string part 01H4Z5TP9R. 3. Randomness Component

The second part of the ULID adds 80 bits (10 bytes) of randomness:

Bits: 80 bits (10 bytes) are allocated for randomness.
Purpose: This randomness ensures that even if two ULIDs are generated at the same exact millisecond, they will still be unique.
Encoding: This 80-bit random number is also encoded into base32, resulting in a 16-character string.
Why is this useful?

The randomness component ensures uniqueness even within the same millisecond, making collisions extremely unlikely.
Example:

A random 80-bit number might be 0x4B2VXFA7EJ9ZNM1ZJ.
This is encoded into the base32 string part B2VXFA7EJ9ZNM1ZJ. 4. Lexicographical Sorting

One of the main features of a ULID is that it is lexicographically sortable. This means that if you sort ULIDs as strings, they will be sorted in the same order as their creation times.

Timestamp Sorted: The first part of the ULID (the timestamp) ensures that earlier IDs come before later ones.
Consistency: This sorting feature is particularly useful in databases and distributed systems where maintaining a natural order is important. 5. Generation Process

Here’s a high-level overview of how a ULID is generated:

Generate Timestamp: Get the current time in milliseconds since the Unix epoch.
Encode Timestamp: Convert the 48-bit timestamp into a 10-character base32 string.
Generate Randomness: Generate a secure random 80-bit number.
Encode Randomness: Convert the 80-bit random number into a 16-character base32 string.
Concatenate: Combine the timestamp and randomness parts to form a 26-character ULID.
