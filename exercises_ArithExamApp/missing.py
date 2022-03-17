#How do you close a file? Add the 3rd line.

file = open('test_file.txt', 'w')
file.write('This line will be in the file!')
file.close()