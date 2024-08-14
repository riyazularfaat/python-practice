fname = input("Enter file name: ")
fh = open(fname)
count = 0
total = 0
for line in fh:
    line = line.rstrip()
    if not line.startswith("X-DSPAM-Confidence:"):
        continue
    count += 1
    fvalues = float(line[20:29])
    total += fvalues
average = total / count
print('Average spam confidence:',average)
