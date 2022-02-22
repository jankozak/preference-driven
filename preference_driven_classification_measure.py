#!/usr/bin/python3
# -*- coding: utf-8 -*-

def count_cm(matrix, i):
    tp = fp = fn = 0
    i-=1
    tp = matrix[i][i]
    fp = sum([x[i] for x in matrix])-tp
    fn = sum(matrix[i])-tp
    return tp,fp,fn
    
def preference_driven(matrix,kappa=[]):
    if len(kappa)==0:
        class_sum = [sum(row) for row in matrix]
        kappa = list(map(lambda x: x/sum(class_sum),class_sum))
    sum_pref = 0
    
    for i in range(len(matrix)):
        tp,fp,fn = count_cm(matrix, i+1)
        prec = tp/(tp+fp) if tp+fp>0 else 0
        rec = tp/(tp+fn) if tp+fn>0 else 0
        sum_pref += kappa[i]*prec + (1-kappa[i])*rec
    return sum_pref/len(matrix)


matrix = [[100, 10, 10],
          [ 10, 80, 30],
          [  1, 10, 30]]
kappa = [0.3,0.1,0.9]
pd = preference_driven(matrix,kappa)

print(pd)
