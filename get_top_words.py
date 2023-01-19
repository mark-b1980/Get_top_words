#!/usr/bin/env python3
import sys

# Check if programm started with all arguments
if len(sys.argv) < 3 or "-h" in sys.argv:
    print("USAGE: get_top_words.py INPUTFILE MIN-LENGTH [TOP-X default=20] [EXCLUDE-WORD1] [EXCLUDE-WORD2] [EXCLUDE-WORD2] ...\n")
    quit()

# Check if 2nd argument is an integer
try:
    sys.argv[2] = int(sys.argv[2])
    if len(sys.argv) == 3:
        sys.argv.append(20)
    else:
        sys.argv[3] = int(sys.argv[3])
except ValueError:
    print("MIN-LENGTH and TOP-X must be a integer!")
    quit()

# Read file and parse data
words = {}
try:
    with open(sys.argv[1], "r") as f:
        for line in f:
            line = line.lower().replace("\n", " ")
            line = line.replace(".", " ").replace("!", " ").replace("?", " ")
            line = line.replace(",", " ").replace(";", " ").replace("-", " ")
            line = line.replace("@", " ").replace("#", " ").replace(":", " ")
            line = line.replace("’", " ").replace("'", " ")

            for word in line.split(" "):
                if len(word) >= sys.argv[2]:
                    if not words.get(word, False):
                        words[word] = 1
                    else:
                        words[word] += 1
except:
    print("Can't read INPUTFILE!")
    quit()

# Set exclude words
if len(sys.argv) > 4:
    exclude_words = sys.argv[4:]
    for word in exclude_words:
        try:
            del(words[word])
        except KeyError:
            print(f"WARNING: {word} was not found in text")

# Output words with top 20 count 
for i in sorted(set(sorted(words.values(), reverse=True)[0:sys.argv[3]]), reverse=True):
    print(f"{i:>4}: ", end="")
    for word, count in words.items():
        if count == i:
            print(f"{word} ", end="")
    print()

