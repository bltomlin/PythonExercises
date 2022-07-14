"""
There's a function blackbox(lst) that takes a list, does some magic, and returns a list. You don't know if it is the same list or creates a completely different one. Find this out and print "same" if the function saves the same list or "new" if the returned list is not connected to the initial one.

Remember to define your list. Content is not important.
"""
lst = ['i', 'k', 'laz']
if id(lst) == id(blackbox(lst)):
    print("same")
else:
    print("new")
