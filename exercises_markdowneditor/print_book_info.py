"""
Your task is to write a function print_book_info(title, author=None, year=None) that prints information about a book. Arguments author and year are optional, so be ready that they might equal None.

You don't have to read the input. The information about a book will be passed to your function, and it should output it in the right format.

See the samples below to understand the output format.
"""

def print_book_info(title, author=None, year=None):
    if year is None and author is None:
        print('"' + title + '"')
    elif year is None:
        print('"' + title + '"' + " was written by " + author)
    elif author is None:
        print('"' + title + '"' + " was written in " + year)
    else:
        print('"' + title + '"' + " was written by " + author + " in", year)
    pass
