from PIL import Image
import math
from collections import Counter
import random

def entropy(data):
    counts = Counter(data)
    
    total = len(data)
    
    entropy = 0.0
    
    for count in counts.values():

        probability = count / total
        
        entropy -= probability * math.log2(probability)
    
    return entropy

with open('sbox_08x08_20130110_011319_02.SBX', 'rb') as  file:
    sbox = file.read()
    
    counter = 0
    all_bytes = []
    
    for byte in sbox:
        if counter % 2 == 0:
            all_bytes.append(byte)
        counter += 1

img = Image.open('cactus.jpg')
pix = img.load()

values = []

counter = 0

for x in range(img.size[0]):
    for y in range(img.size[1]):

        [r, g, b] = img.getpixel((x, y))

        if(counter == 255):
            counter = 0
        else:
            counter = counter + 1

            values.append(r ^ all_bytes[counter])
            values.append(g ^ all_bytes[counter])
            values.append(b ^ all_bytes[counter])

# x = int(input("How many numbers should be combined in random string: "))

result = ""

for i in range(0, x):

    number = int(values[random.randint(0, len(values) - 1)])

    result = result + str(number)

number = int(values[random.randint(0, len(values) - 1)])

# print(result)

print(number)
        
# print(values)

# ent = entropy(values)
# print(f"Entropy equals: {ent}")
