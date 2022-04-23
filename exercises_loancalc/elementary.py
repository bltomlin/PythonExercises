"""
write a program that takes a file as an argument, reads it, decodes it, and prints the decoded text. Even though the
provided piece of code above contains the phrase "Decoded text: " and quotes, please output only the decoded text
itself.
"""

import argparse

def decode_caesar_cipher(s, n):
    alpha = " ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz',.?!"
    s = s.strip()
    text = ''
    for c in s:
        text += alpha[(alpha.index(c) + n) % len(alpha)]
    print('Decoded text: "' + text + '"')


parser = argparse.ArgumentParser(description="This program decodes a Caesar cipher")
parser.add_argument("--file")
args = parser.parse_args()

filename = args.file
opened_file = open(filename)
encoded_text = opened_file.read()
opened_file.close()

decode_caesar_cipher(encoded_text, -13)
