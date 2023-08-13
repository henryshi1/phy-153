# Henry Shi
# L4ex5.py

zlist = [];                         # initialize empty zlist
xlist_idx = [0,1,2];                # list of indices corresp. to xlist
xlist = [11,21,31];                 # xlist

for i in xlist_idx:                 # for every index i in xlist_idx
    zlist.append(xlist[i]*0.5+15);  # Calculate the corresp. value of z as: x*0.5 + 15

print(xlist);                       # Print xlist. Should yield [11,21,31]
print(zlist);                       # Print zlist. Should yield [20.5,25.5,30.5]
