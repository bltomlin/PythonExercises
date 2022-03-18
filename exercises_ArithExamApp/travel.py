#There's a file countries.txt that contains a list of the countries Kate has been to. For example:

#France
#China
#Brazil

#During her last trip, she has visited Turkey for the first time. Add Turkey to the countries.txt file.

#Kate will not give up traveling, so it would be reasonable to add a newline character at the end.

#Don't forget to close the file!

new_file = open('countries.txt', 'a', encoding='utf-8')
new_file.write('Turkey\n')
new_file.close()