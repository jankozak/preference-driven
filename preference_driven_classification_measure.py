#!/usr/bin/python3
# -*- coding: utf-8 -*-

def count_cm(matrix, i):
    tp = fp = fn = 0
    i-=1
    tp = matrix[i][i]
    fp = sum([x[i] for x in matrix])-tp
    fn = sum(matrix[i])-tp
    return tp,fp,fn


def rec_avg(matrix):
    sum_rec = 0
    for i in range(n):
        tp,fp,fn = count_cm(matrix, i+1)
        sum_rec += tp/(tp+fn) if tp+fn>0 else 0
    return sum_rec/n

def prec_avg(matrix):
    sum_prec = 0
    for i in range(n):
        tp,fp,fn = count_cm(matrix, i+1)
        sum_prec += tp/(tp+fp) if tp+fp>0 else 0
    return sum_prec/n
    
def pref(matrix,kappa):
    sum_pref = 0
    for i in range(n):
        tp,fp,fn = count_cm(matrix, i+1)
        prec = tp/(tp+fp) if tp+fp>0 else 0
        rec = tp/(tp+fn) if tp+fn>0 else 0

        sum_pref += kappa[i]*prec + (1-kappa[i])*rec
        #sum_prec += prec
        #sum_rec += rec

        #print(f"For {i+1:3} | TP: {tp:3} | FP: {fp:3} | FN: {fn:3} || Prec: {prec:.2f} | rec: {rec:.2f}")

    return sum_pref/n


for n_test in range(0,1):
    lines = open("test"+str(n_test)+".txt").read().replace("[","").replace("]","").split("\n")
    matrix = [list(map(int,line.strip().split())) for line in lines if len(line)>0]
    n = len(matrix)


    #kappa = [0,1]

    #####
    # Test dla różnych kappa
    test = [0]
    distance = 0.1
    while test[-1]<1:
        test.append(round(test[-1]+distance,5)) # testowe wartości kappy

    kappa_list = []
    for _ in range(n-1):
        for i in test:
            for j in test:
                kappa_list.append([i,j])
                #for k in test:
                #    kappa_list.append([i,j,k])
    #print(kappa_list)

    output = open("results"+str(n_test),"w")
    for kappa in kappa_list:
        #print(kappa[0],kappa[1],pref(matrix,kappa))
        output.write(f"{kappa[0]} {kappa[1]} {pref(matrix,kappa)}\n")
    output.close()
    print("----------")
    print(rec_avg(matrix), "avg recall, to wszystkie kappa = 0")
    print(prec_avg(matrix), "avg precision, to wszystkie kappa = 1")
