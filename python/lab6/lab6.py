#!/usr/bin/env python3.7
import numpy as np
import matplotlib
matplotlib.use('ps')
import matplotlib.pyplot as plt

def zad1(n, plik = None):
    filename = 'zad1_test.txt' if not plik else plik
    info = lambda x,opis,s: '{} - {}: {}'.format(x,opis,s)
    with open(filename) as f1:
        lines = f1.readlines()
        n_all = n if n <= len(lines) else len(lines)
        for i in range(n_all):
            print(info(i,'FIRST LINES',lines[i]))
            print(info(i,'LAST LINES',lines[-(i+1)]))
            print(info(i,'EACH N LINE',lines[i])) if i%n else None
            print(info(i,'N LETTER',lines[i][n])) if len(lines[i]) > n else print(lines[i][-1])
            slowa = lines[i].split(' ')
            print(info(i,'N WORD',slowa[n])) if len(slowa) > n else print(info(i,'N WORD',slowa[-1]))
        f1.close()

def zad2(plik = None):
    filename = 'wyniki_zad2.out' if not plik else plik
    files = [f'pliki/plik{i}.in' for i in range(6)]
    files = [open(f).readlines() for f in files]
    Xs = [line.split(' ')[0] for line in files[0]]
    Ys = [[] for _ in range(len(Xs))]
    for i in range(len(Ys)):
        temp = [float(lines[i].split(' ')[1]) for lines in files]
        Ys[i].extend(temp)
    Y_data = [(np.average(y),np.std(y)) for y in Ys]
    with open(filename,'w') as out:
        for i in range(len(Y_data)):
            out.writelines([Xs[i], ' ', str(Y_data[i][0]), ' ', str(Y_data[i][1]),'\n'])
        out.close()


def zad3(filename = None):
    filename = 'wyniki_zad2.out' if not filename else filename
    with open(filename) as f:
        lines = f.readlines()
        columns = len(lines[0].split(' ')) - 1
        Xs = [float(line.split(' ')[0]) for line in lines]
        Ys = [[] for _ in range(columns)]
        for i in range(columns):
            Ys[i] = [float(line.split(' ')[i+1]) for line in lines]
        plt.plot(Xs,*Ys, 'bo')
        plt.savefig('output.pdf')
        f.close()

def zad4(plik):
    s_alf = ['a','b','q','w','e','r','t','y','u','i','o','p','s','d','f','g','h','j','k','l','z','x','c','v','b','n','m']
    s_alf.sort()
    data = {l:0 for l in s_alf}
    with open(plik) as f:
        words = f.read().split(' ')
        for word in words:
            if word:
                if word[0].isalpha():
                    data[word[0].lower()] += 1
        real_data = [data[k] for k in data]
        plt.hist(real_data, label=s_alf)
        plt.savefig('output2.pdf')
        f.close()


if __name__ == '__main__':
    # zad3('pliki/plik0.in')
    # zad3()
    zad4('zad4B.in')

