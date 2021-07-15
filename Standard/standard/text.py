import string
import textwrap



def main_string():
    print("String processing")
    string_proc()
    template_proc()
    fill_proc()


def string_proc():
    s = 'The quick brown fox jumped over the lazy dog.'
    print(s)
    print(string.capwords(s))


def fill_proc():
    sample_text = '''
    The textwrap module can be used to format text for output in
    situations where pretty-printing is desired. It offers
    programmatic functionality similar to the paragraph wrapping
    or filling features found in many text editors.
    '''
    print(textwrap.fill(sample_text, width=50))
    detended_text = textwrap.dedent(sample_text)
    print(detended_text)


def template_proc():
    values = {'var': 'foo'}
    t = string.Template("""
    Variable : $var
    Escape : $$
    Variable in text: ${var}iable
    """)
    print('TEMPLATE:', t.substitute(values))
    s = """
    Variable : %(var)s
    Escape : %%
    Variable in text: %(var)siable
    """
    print('INTERPOLATION:', s % values)
    s = """
    Variable : {var}
    Escape : {{}}
    Variable in text: {var}iable
    """
    print('FORMAT:', s.format(**values))