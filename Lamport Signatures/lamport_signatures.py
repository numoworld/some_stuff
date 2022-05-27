import secrets
import hashlib
import sys


CHAR_ENC = 'utf-8'  # needed to encode string to bytes
BYTE_ORDER = sys.byteorder  # https://pythontic.com/modules/socket/byteordering-coversion-functions


# key pair creation
def keygen():
    # initializing two arrays with 2*256 elements each
    sk = [[0]*256, [1]*256]  # 0 and 1 are just visual representation of two rows, you can use any sentinel value
    pk = [[0]*256, [1]*256]
    for i in range(256):
        # generating secret key, replacing each element in each row with random 256 bit long sequence
        sk[0][i] = secrets.token_bytes(32)
        sk[1][i] = secrets.token_bytes(32)

        # generating public key, hashing each corresponding sequence
        pk[0][i] = hashlib.sha256(sk[0][i]).digest()
        pk[1][i] = hashlib.sha256(sk[1][i]).digest()

    return sk, pk


# Signing message using our secret key
def sign(sk, msg):
    sig = [0] * 256
    hashed_msg = int.from_bytes(hashlib.sha256(msg.encode(CHAR_ENC)).digest(), BYTE_ORDER)
    for i in range(0, 256):
        # What we do here is we reading right-most bit on every iteration:
        # For example, we have 1011110, then 1011110 & 0000001 will give us 0,
        # and in the next iteration we shift number, so it's going to be 101111 & 1 = 1
        b = hashed_msg >> i & 1

        # Then we use this bit to get row - either 1 or 0 of our secret key
        sig[i] = sk[b][i]

    return sig


# Verify the signature using generated private key
def verify(sig, msg, pk):
    hashed_msg = int.from_bytes(hashlib.sha256(msg.encode(CHAR_ENC)).digest(), BYTE_ORDER)
    for i in range(0, 256):
        b = hashed_msg >> i & 1

        # hashing secret key element contained in signature
        check = hashlib.sha256(sig[i]).digest()

        # checking if the preimage was correct
        if pk[b][i] != check:
            return False

    return True


sk, pk = keygen()
message = 'Zachary Ratliff is cool! 1d8a8b7def'
sig = sign(sk, message)
is_valid_signature = verify(sig, message, pk)