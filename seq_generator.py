#description     :This script will randomly generate sequences containg all XPyPyY sites.
#author          :Chen Lu


import itertools
import random

N = int(raw_input("How many iterations you want?\n"))
bases = ['A','C','T','G']
purines = ['A','G']
cpds = ['TT','TC','CC','CT']
pyrimidines = ['C','T']
ends = [['TA','CG'],['CA','TG']]


def is_max_4pys(s):
    if len(s) <= 4:
        return True
    count = 0
    for i in range(len(s)):
        if s[i] in pyrimidines:
            count += 1
        else:
            count = 0
        if count > 4:
            return False
    return True

def get_site_freqs(s):
    site_freqs = {}
    blocks = [''.join(t) for t in  itertools.product(bases, cpds, bases)]
    for block in blocks:
        site_freqs[block] = s.count(block)
    return site_freqs

def contains_all_sites(s):
    site_freqs = get_site_freqs(s)
    flag = True
    for k, v in site_freqs.items():
        flag = flag and v >= 1
    return flag

def get_blocks():
    threemer_blocks = [''.join(t) for t in  itertools.product(pyrimidines, pyrimidines, pyrimidines)]
    A_5mer = []
    G_5mer = []
    for threemer in threemer_blocks:
        end = random.choice(ends)
        A_5mer.append(end[0][0] + threemer + end[0][1])
        G_5mer.append(end[1][0] + threemer + end[1][1])

    twomer_blocks = [''.join(t) for t in  itertools.product(pyrimidines, pyrimidines)]
    A_3mer = 2 * [ x + 'A' for x in twomer_blocks ]
    G_3mer = 2 * [ x + 'G' for x in twomer_blocks ]

    #print  A_5mer + G_5mer + A_3mer + G_3mer
    return A_5mer + G_5mer + A_3mer + G_3mer

def generate_seq(blocks):
    random.shuffle(blocks)
    seq = ''.join(blocks)
    seq = random.choice(purines) + seq
    if contains_all_sites(seq) and is_max_4pys(seq):
        return seq
    else:
        return ""

def repeat(n):
    seqs = []
    blocks = get_blocks()
    for i in range(n):
        s = generate_seq(blocks)
        if( s!= ""):
            seqs.append(s)
    return seqs

f = open('output.txt','w')
seqs = repeat(N)
count = 1
for seq in seqs:
    f.write('seq ' + str(count )+' :\n')
    f.write(seq + '\n')
    count += 1
f.close()
