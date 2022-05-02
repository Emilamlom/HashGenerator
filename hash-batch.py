import sys

#pipe output to file
sys.stdout = open('wordlist-cust.txt', 'w')

#read files
nouns = open("nouns.txt", "r").readlines()
adjs = open("adjs2.txt", "r").readlines()

#Initialize Vairables
word = ''

#with open("nouns.txt") as nouns, open("adj.txt") as adjs:
for noun in nouns:
    for adj in adjs:
        for x in range(100):
            word = adj.strip() + noun.strip() + '{:02d}'.format(x)
            print(word)


#while x < 10000:
#    word = prefix + str('{:04d}'.format(x))
#    print(word, end=': ')
#    word = hashlib.md5(word.encode())
#    print(word.hexdigest())
#    x += 1

