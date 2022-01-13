
def flippingBits(n):
    binary = '{:032b}'.format(n)
    bdict = {'0': '1', '1': '0'}
    inverse_s = ''
    for i in binary:
        inverse_s += bdict[i]
    return int(inverse_s, 2)
