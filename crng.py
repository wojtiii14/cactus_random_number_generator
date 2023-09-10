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

img = Image.open('cactus.jpg')
pix = img.load()

values = []

for x in range(img.size[0]):
    for y in range(img.size[1]):
        [r, g, b] = img.getpixel((x, y))

        values.append(r)
        values.append(g)
        values.append(b)

x = int(input("How many numbers should be combined in random string: "))

result = ""

for i in range(0, x):

    number = int(values[random.randint(0, len(values) - 1)])

    result = result + str(number)

print(result)
        
# print(values)

# ent = entropy(values)
# print(f"Entropia wynosi: {ent}")
