import random
import sys
print(sys.argv)

print("hi")
print("hi")
print("hi")
print("blat")

i = 0

while i < 10 :
    s = random.choice('Chewbacca') + str(random.randint(1, 100))
    print (s)
    i = i + 1
