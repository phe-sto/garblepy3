# -*- coding: utf-8 -*-

import gzip
import sys

import unidecode
from slimit import minify


def garble(inputPath, outputPath, compress):
    # letters / numbers
    symbols = {
        'a': '((!!+[]+"")[+!![]])',
        'b': '((({})+"")[(+!![])+(+!![])])',
        'c': '((({})+"")[(+!![])+(+!![])+(+!![])+(+!![])+(+!![])])',
        'd': '((({})[""]+"")[(+!![])+(+!![])])',
        'e': '((!!+[]+"")[(+!![])+(+!![])+(+!![])+(+!![])])',
        'f': '((!!+[]+"")[+[]])',
        'g': '"\\x67"',
        'h': '"\\x68"',
        'i': '((+!![]/+[]+"")[(+!![])+(+!![])+(+!![])])',
        'j': '((({})+"")[(+!![])+(+!![])+(+!![])])',
        'k': '"\\x6B"',
        'l': '((!!+[]+"")[(+!![])+(+!![])])',
        'm': '"\\x6D"',
        'n': '((+!![]/+[]+"")[+!![]])',
        'o': '((({})+"")[+!![]])',
        'p': '"\\x70"',
        'q': '"\\x71"',
        'r': '((!+[]+"")[+!![]])',
        's': '((!!+[]+"")[(+!![])+(+!![])+(+!![])])',
        't': '((!+[]+"")[+[]])',
        'u': '((!+[]+"")[(+!![])+(+!![])])',
        'v': '"\\x76"',
        'w': '"\\x77"',
        'x': "'x'",
        'y': '((+!![]/+[]+"")[(+!![])+(+!![])+(+!![])+(+!![])+(+!![])+(+!![])+(+!![])])',
        'z': '"\\x7A"',
        'A': '"\\x41"',
        'B': '"\\x42"',
        'C': '"\\x43"',
        'D': '"\\x44"',
        'E': '"\\x45"',
        'F': '"\\x46"',
        'G': '"\\x47"',
        'H': '"\\x48"',
        'I': '((+!![]/+[]+"")[+[]])',
        'J': '"\\x4A"',
        'K': '"\\x4B"',
        'L': '"\\x4C"',
        'M': '"\\x4D"',
        'N': '((+[]/+[]+"")[+[]])',
        'O': '((({})+"")[(+!![])+(+!![])+(+!![])+(+!![])+(+!![])+(+!![])+(+!![])+(+!![])])',
        'P': '"\\x50"',
        'Q': '"\\x51"',
        'R': '"\\x52"',
        'S': '"\\x53"',
        'T': '"\\x54"',
        'U': '"\\x55"',
        'V': '"\\x56"',
        'W': '"\\x57"',
        'X': '"\\x58"',
        'Y': '"\\x59"',
        'Z': '"\\x5A"',
        "(": "'('",
        ")": "')'",
        "{": "'{'",
        "}": "'}'",
        "[": "'['",
        "]": "']'",
        ".": "'.'",
        ";": "';'",
        "@": "'@'",
        "*": "'*'",
        '"': "'\"'",
        "/": "'/'",
        ":": "':'",
        ",": "','",
        "'": '"\'"',
        "=": "'='",
        ">": "'>'",
        "<": "'<'",
        "!": "'!'",
        "$": "'$'",
        "_": "'_'",
        "#": "'#'",
        "+": "'+'",
        "-": "'-'",
        "%": "'%'",
        " ": "' '",
        "?": "'?'",
        "|": "'|'",
        "^": "'^'",
        "&": "'&'",
        "~": "'~'",
        "\\": "'\\\\'",
        "0": "(+[])",
        "1": "(+!![])",
        "2": "((+!![])+(+!![]))",
        "3": "((+!![])+(+!![])+(+!![]))",
        "4": "((+!![])+(+!![])+(+!![])+(+!![]))",
        "5": "((+!![])+(+!![])+(+!![])+(+!![])+(+!![]))",
        "6": "((+!![])+(+!![])+(+!![])+(+!![])+(+!![])+(+!![]))",
        "7": "((+!![])+(+!![])+(+!![])+(+!![])+(+!![])+(+!![])+(+!![]))",
        "8": "((+!![])+(+!![])+(+!![])+(+!![])+(+!![])+(+!![])+(+!![])+(+!![]))",
        "9": "((+!![])+(+!![])+(+!![])+(+!![])+(+!![])+(+!![])+(+!![])+(+!![])+(+!![]))"
    }

    fileContents = open(inputPath, 'r').read()

    fileContentsUnicoded = str(fileContents)
    fileContentsUnunicoded = unidecode.unidecode(fileContentsUnicoded)

    replacedReserved1 = fileContentsUnunicoded.replace(".deleteExpando", ".replaceLaterExpando");
    replacedReserved2 = replacedReserved1.replace(".delete", "['delete']");
    replacedReserved3 = replacedReserved2.replace(".replaceLaterExpando", ".deleteExpando");
    replacedReserved4 = replacedReserved3.replace(".catch", "['catch']");

    minified = minify(replacedReserved4, mangle=False, mangle_toplevel=False)

    transformed = []
    outputFile = open(outputPath, 'w+')
    outputFile.write(
        "[][(![]+[])[+[]]+([![]]+[][[]])[+!+[]+[+[]]]+(![]+[])[!+[]+!+[]]+(!![]+[])[+[]]+(!![]+[])[!+[]+!+[]+!+[]]+(!![]+[])[+!+[]]][([][(![]+[])[+[]]+([![]]+[][[]])[+!+[]+[+[]]]+(![]+[])[!+[]+!+[]]+(!![]+[])[+[]]+(!![]+[])[!+[]+!+[]+!+[]]+(!![]+[])[+!+[]]]+[])[!+[]+!+[]+!+[]]+(!![]+[][(![]+[])[+[]]+([![]]+[][[]])[+!+[]+[+[]]]+(![]+[])[!+[]+!+[]]+(!![]+[])[+[]]+(!![]+[])[!+[]+!+[]+!+[]]+(!![]+[])[+!+[]]])[+!+[]+[+[]]]+([][[]]+[])[+!+[]]+(![]+[])[!+[]+!+[]+!+[]]+(!![]+[])[+[]]+(!![]+[])[+!+[]]+([][[]]+[])[+[]]+([][(![]+[])[+[]]+([![]]+[][[]])[+!+[]+[+[]]]+(![]+[])[!+[]+!+[]]+(!![]+[])[+[]]+(!![]+[])[!+[]+!+[]+!+[]]+(!![]+[])[+!+[]]]+[])[!+[]+!+[]+!+[]]+(!![]+[])[+[]]+(!![]+[][(![]+[])[+[]]+([![]]+[][[]])[+!+[]+[+[]]]+(![]+[])[!+[]+!+[]]+(!![]+[])[+[]]+(!![]+[])[!+[]+!+[]+!+[]]+(!![]+[])[+!+[]]])[+!+[]+[+[]]]+(!![]+[])[+!+[]]](")

    for i in range(len(minified)):
        if i == 0:
            transformed.append(symbols[minified[i]] + "+")
        elif i == len(minified) - 1:
            transformed.append(symbols[minified[i]])
        else:
            transformed.append(symbols[minified[i]] + "+")
    outputFile.write("".join(transformed))
    outputFile.write(")()")
    outputFile.close()

    if compress.lower() == "yes":
        f_in = open(outputPath, 'rb')
        f_out = gzip.open(outputPath + ".gz", 'wb')
        f_out.writelines(f_in)
        f_out.close()
        f_in.close()


if __name__ == "__main__":
    # execute only if run as a script
    if len(sys.argv) < 3:
        print("please specify an input and output and if you would like to use compression.")
        quit()
    inputPath = sys.argv[1]
    outputPath = sys.argv[2]
    compress = sys.argv[3]
    garble(inputPath, outputPath, compress)
