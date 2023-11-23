import cv2
import os
# Read the image
img = cv2.imread("windows.jpg")
# Get the secret message and password
msg = input("Enter secret message: ")
password = input("Enter password: ")
# Create dictionaries for character to integer and integer to character conversion
char_to_int = {chr(i): i for i in range(255)}
int_to_char = {i: chr(i) for i in range(255)}
# Encrypt the message into the image
for idx, char in enumerate(msg):
    x, y, z = idx // img.shape[1], idx % img.shape[1], (idx // 3) % 3
    img[x, y, z] = char_to_int[char]
# Save the image with the encrypted message
cv2.imwrite("Encryptedmsg.jpg", img)
# Open the image
os.system("start Encryptedmsg.jpg")
# Decrypt the message from the image
decrypted_msg = ""
pas = input("Enter passcode for Decryption: ")
if password == pas:
    for idx in range(len(msg)):
        x, y, z = idx // img.shape[1], idx % img.shape[1], (idx // 3) % 3
        decrypted_msg += int_to_char[img[x, y, z]]
    print("Decrypted message:", decrypted_msg)
else:
    print("Not valid key")
