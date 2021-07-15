import string


def main_string():
    print("String processing")
    string_proc()


def string_proc():
    s = 'The quick brown fox jumped over the lazy dog.'
    print(s)
    print(string.capwords(s))
