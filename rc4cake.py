from Crypto.Cipher import ARC4
from sys import stdin, stdout


filename = "keys.txt"
with open(filename, 'r') as myfile:
    data=myfile.read().replace('\n', '')

key = "there is no cake"
ci=ARC4.new(key)
c=ci.decrypt(data)
print(c)
