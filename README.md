# perceptual_hashing
Contains two scripts: 

1. phfGenerate takes a folder containing images (JPG or PNG, but this can be altered), and produces a text file containing their PHF hashes for
   two different PHF functions, dhash and phash from the imagehash Python module.

2. phfCompare recieves such a text file (database) and compares the digests with a given image. The script will then notify you of either an exact match or close similarity.
   The sensitivity of close matches can be adjusted under "hamming_threshold"
