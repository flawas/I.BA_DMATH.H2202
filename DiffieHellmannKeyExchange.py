import random
p = int(input("p:"))
g = int(input("g:"))


class Person:
  def __init__(self, name):
    self.name = name
    self.priv_key = random.randint(500, 4000)
  
  def computeOffer(pers, g, p):
    return (g ** pers.priv_key) % p
  
  def computeKey(pers, offer, p):
    K = (offer ** pers.priv_key) % p
    pers.cKey = K
    return K
  
annie = Person("Alice")
billy = Person("Bob")
print("Private Keys: ")
print(annie.priv_key)
print(billy.priv_key)

A = annie.computeOffer(g, p)
B = billy.computeOffer(g, p)

print("Offers in the Insecure Channel: ")
print(A)
print(B)


print("Cryptographic Keys:")
print(annie.computeKey(B, p))
print(billy.computeKey(A, p))