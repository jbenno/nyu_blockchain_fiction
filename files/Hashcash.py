# HashCash

import hashlib # serves the hash algorishms; SHA = secure hash alogrithm
import secrets

filename = "/Users/jbenno/temp/email.html"
with open(filename, "rb") as f:
    inputBytes = f.read()

h = int(hashlib.sha256(inputBytes).hexdigest(),16) # we use SHA2 (SHA252), hash our input and convert it to a number in hex
difficulty = 2**254 # our hash has to get under this threshold

while h > difficulty: # we generate random nonces (that means random strings), concatenate them with our input and hash the resulting bytes (input + nonce). ; the smaller our difficulty, the more leading zeros, the more time it takes to find the nonce that does the trick
    nonce = secrets.token_urlsafe(32)
    nonceBytes = bytes(nonce, 'utf-8')
    testBytes = inputBytes + nonceBytes
    h = int(hashlib.sha256(inputBytes).hexdigest(),16)

print ("No. of iterations: ", i)
print ("The successful nonce: ", nonce)
print ("\n")
print ("Sha256: ", h)
print (" = ", "{:e}".format(h))
hbin = bin(h).zfill(256)
print ("\n")
print ("... in Bin:")
print (hbin)
