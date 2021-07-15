import re


def main_re():
    #simple()
    test_patterns('abbaaabbbbaaaaa',
                  [('ab', "'a' followed by 'b'"),
                   ])
    test_patterns(
        'abbaabbba',
        [('ab*', 'a followed by zero or more b'),
         ('ab+', 'a followed by one or more b'),
         ('ab?', 'a followed by zero or one b'),
         ('ab{3}', 'a followed by three b'),
         ('ab{2,3}', 'a followed by two to three b')],
    )


def simple():
    pattern = 'this'
    text = 'Does this text match the pattern?'
    match = re.search(pattern, text)
    s = match.start()
    e = match.end()
    print('Found "{}"\nin "{}"\nfrom {} to {} ("{}")'.format(
        match.re.pattern, match.string, s, e, text[s:e]))
    print(f'from {match.start()} to {match.end()} ("{match.re.pattern}")')


def test_patterns(text, patterns):
    """Given source text and a list of patterns, look for
    matches for each pattern within the text and print
    them to stdout.
    """
    # Look for each pattern in the text and print the results.
    for pattern, desc in patterns:
        print("'{}' ({})\n".format(pattern, desc))
        print(" '{}'".format(text))
        for match in re.finditer(pattern, text):
            s = match.start()
            e = match.end()
            substr = text[s:e]
            n_backslashes = text[:s].count('\\')
            prefix = '.' * (s + n_backslashes)
            print(" {}'{}'".format(prefix, substr))
        print()
    return
