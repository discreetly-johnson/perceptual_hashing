#imports
from PIL import Image
import imagehash
import glob
import os 

folder = input("Please provide image directory for hashing: ")

#Returns the location of this program
script_path = os.path.dirname(os.path.realpath(__file__))

#File extensions that will be noticed by Glob utility. This can be altered to cater for alternative image file extensions
ext = ["/*.jpg", "/*.png"]

#iterates through each file of the required extensions, applying to PHF functions
#writes the PHF digests to a text file
for ex in ext:
    for image in glob.glob(folder + ex): 
            img = Image.open(image)
                        
            phash = imagehash.phash(img)
            dhash = imagehash.dhash(img)

            phash_txt = "Phash: " + str(phash) + "\n" 
            dhash_txt = "Dhash: " + str(dhash) + "\n"
            with open(os.path.join(script_path, "phf_hashes.txt"), "a") as f:
                f.write(phash_txt)
                f.write(dhash_txt)

