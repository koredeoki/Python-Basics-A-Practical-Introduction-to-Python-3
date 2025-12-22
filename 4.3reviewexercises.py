# convert to lowercase
# "Animals", "Badger", "Honey Bee", "Honeybadger"
print("Animals".lower())
print("Badger".lower())
print("Honey Bee".lower())
print("Honeybadger".lower())
# convert to uppercase
# "Animals", "Badger", "Honey Bee", "Honeybadger"
print("Animals".upper())
print("Badger".upper())
print("Honey Bee".upper())
print("Honeybadger".upper())
# remove whitespace
string1 = "    Filet Mignon"
string1 = string1.lstrip()
string2 = "Brisket    "
string2 = string2.rstrip()
string3 = " Cheeseburger "
string3 = string3.strip()
print(string1)
print(string2)
print(string3)

string1 = "Becomes"
string2 = "becomes"
string3 = "BEAR"
string4 = " bEautiful"

print(string1.startswith("be"))
print(string2.startswith("be"))
print(string3.startswith("be"))
print(string4.startswith("be"))

string1 = "Becomes"
string2 = "becomes"
string3 = "BEAR"
string4 = " bEautiful"

string1 = string1.lower()
string2 = string2.lower()
string3 = string3.lower()
string4 = string4.strip().lower()

print(string1.startswith("be"))
print(string2.startswith("be"))
print(string3.startswith("be"))
print(string4.startswith("be"))
