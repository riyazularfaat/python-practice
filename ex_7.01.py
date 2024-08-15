fname = input('Enter file name: ')
try:
    fhandle = open(fname)
except ValueError:
    print('Invalid file name')
    quit()

for line in fhandle:
    line.rstrip()
    to_upper = line.upper()
    print(to_upper)