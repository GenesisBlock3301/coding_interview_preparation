# Secret message to be encoded
message = "Hello World!"

# Convert message to binary
message_binary = "".join(bin(ord(char))[2:] for char in message)

# Define a secret key
key = "10101001"

# Pad the key to match the message length
key_padded = key * (len(message_binary) // len(key)) + key[:len(message_binary) % len(key)]

# Apply XOR operation
encoded_message = "".join([str(int(a) ^ int(b)) for a, b in zip(message_binary, key_padded)])

print("Original message:", message)
print("Binary message:", message_binary)
print("Secret key:", key)
print("Padded key:", key_padded)
print("Encoded message:", encoded_message)

# Decode the message using the same key
decoded_message_binary = "".join([str(int(a) ^ int(b)) for a, b in zip(encoded_message, key_padded)])

# Convert binary back to text
decoded_message = "".join(chr(int(binary_chunk, 2)) for binary_chunk in [decoded_message_binary[i:i+8] for i in range(0, len(decoded_message_binary), 8)])

print("Decoded message:", decoded_message)
