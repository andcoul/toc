from pip._vendor.distlib.compat import raw_input

from turing.check import check_language

if __name__ == "__main__":
    word = raw_input(
        "Usage:\n" + "python test.py word\n" + "where word is the word to be tested as a validate string\n")

    print("Testing: %s" % word)
    check_language(word)

#aaaa+aaaa=aaaaaaaa
