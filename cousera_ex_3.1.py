def computepay(fh, fr):
    if fh > 40:
        reg = fh * fr
        opt = (fh-40) * (fr*0.5)
        return reg + opt
    else:
        return fh *fr

hours = input('Enter hours: ')
rate = input('Enter rate: ')
fh = float(hours)
fr = float(rate)

print('Pay',computepay(fh, fr))