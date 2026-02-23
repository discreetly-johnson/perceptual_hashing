import glob
from PIL import Image
import imagehash
import hashlib

phash_file = input("Please provide text filepath containing PHF hashes: : ")

im = input("Please provide filepath for chosen image: ")
#image is read and hashed using two different PHF functions
image = Image.open(im)
image_phash = imagehash.phash(image)
image_dhash = imagehash.dhash(image)

#strings for comparing exact matches
phash_str = str(image_phash)
dhash_str = str(image_dhash)

print("This image has phash: " + phash_str)
print("This image has dhash: " + dhash_str)

#defining Hamming Distance for similarity checking 

hamming_threshold = 5 #mid-strength value found through manual testing

def hamming_distance(hash1, hash2):
    return bin(hash1 ^ hash2).count("1")

with open(phash_file) as file:
    match = False
    for line in file:
        
        split = line.split()
        hash = split[1]
        
        if hash == phash_str or hash == dhash_str:
            print("This image has an exact match. " + line)
            match = True
            
        #Hash and strings are converted into integers so that they are same data types
        #Integers put through the Hamming Distance function
        elif hamming_distance(int(phash_str, 16), int(hash, 16)) < hamming_threshold:
            print("This image has a close match. " + line)
            match = True
        elif hamming_distance(int(dhash_str, 16), int(hash, 16)) < hamming_threshold:
            print("This image has a close match. " + line)
            match = True
    if match == False:
        print("No close matches were found.")
    
