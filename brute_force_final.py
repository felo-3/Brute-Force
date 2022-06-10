#import hashlib
#from datetime import datetime
#from itertools import permutations
#import string

#start timer 
start = datetime.now()
# open file with password hashes
file = open("hashes.txt")
#find number of passwords
num_pass = len(file.readlines())
#number of cracked passwords 
num_cracked = 0
#creating a set from hashed passwords
hash_set = set(open('hashes.txt').read().split())
#iterating variable 
x = 1
file.close()
#creating string of all printable characters except for whitespace 
char = string.digits + string.ascii_letters + string.punctuation

#while not all passwords have been cracked 
while num_cracked < num_pass:
    poss_guesses = permutations(char, x)    #create permutations of size x
    for i in (poss_guesses): #iterate through permutations
        stri = ("".join(i))
        hash_guess = hashlib.md5(stri.encode())
        if hash_guess.hexdigest() in hash_set:  #compare guess and real password
            print(f"{stri}\t{(datetime.now()-start).seconds}")
            num_cracked += 1
    x += 1

