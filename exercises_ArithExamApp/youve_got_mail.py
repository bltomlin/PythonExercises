#You are working with a database of email addresses from an imaginary email service yougotmail.com. Create a program that would separate the local-part that precedes the @ sign from the rest of the address.

email = input()
email = email.split('@')
print(email[0])