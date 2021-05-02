import string
import random

f = open("genTest.txt", "w+")
letters = string.ascii_letters

qtdExamples = random.randint(10, 100)
maxVolume = random.randint(1000, 10000)
f.write(str(maxVolume)+'\n')
for i in range(qtdExamples):
    f.write("1\n")
    a = ''.join(random.choice(letters) for i in range(10))
    f.write(a+'\n')
    volume = random.randint(1, 200)
    f.write(str(volume)+'\n')
    valor = random.randint(1, 500)
    f.write(str(valor)+'\n')
f.write("2\n")
f.write("3\n")
f.close()
