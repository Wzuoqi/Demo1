# 创建时间：2021/2/24 14:07
# hmmer_selecting.py

from sys import argv

hmmerlist = list(set([((x.rstrip()).spilt())[2] for x in open(argv.[1]).readlines()]))
sequencelist = [x.rstrip() for x in open(argv[2]).readlines()]
seq_dict = {}
for x in sequencelist:
    if x.startwith('>'):
        dict_id = x[1:]
        seq_dict[dict_id] = ''
    else:
        seq_dict[dict_id] += x

for x in tlbastnlist:
    for y in seq_dict.keys():
        if x == y:
            print(">"+x+"\n"+seq_dict[y])


