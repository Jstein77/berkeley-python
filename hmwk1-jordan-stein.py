#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jun  9 17:45:20 2018

@author: jordanstein
1.  Include a sec4on with your name
2.  Create matrix A with size (3,5) containing random numbers A = np.random.random(15)
3.  Find the size and length of matrix A
4.  Resize (crop/slice) matrix A to size (3,4)
5.  Find the transpose of matrix A and assign it to B
6.  Find the minimum value in column 1 of matrix B (check the proper4es of a matrix – ‘B.min()’)
7.  Find the minimum and maximum values for the en4re matrix A
8.  Create vector X (an array) with 4 random numbers
9.  Create a func4on and pass vector X and matrix A in it
10.  In the new func4on mul4ply vector X with matrix A and assign the result to D
(note: you may get an error! ... think why and fix it. Recall matric manipula4on in class!)
11.  Create a complex number Z with absolute and real parts != 0
12.  Show its real and imaginary parts as well as it’s absolute value
13.  Mul4ply result D with the absolute value of Z and record it to C
14.  Convert matrix B from a matrix to a string and overwrite B
15.  Display a text on the screen: ‘Your Name is done with HW2‘
16.  Organize your code: use each line from this assignment as a comment line before each step
17.  Save all steps as a script in a .py file
18.  Email your Github link to me including your .py file + screenshots of your running code no later than midnight on Saturday Jun.09.
"""
import numpy as np

class _file_operations():
    def write_my_file(A):
        file = open('my_array','w')
        file.writelines('%s' %str(A))
        file.close()
    def read_my_file():
        file = open('my_array','r')
        B = file.read()
        file.close()
        return B

#create a (3,5) matrix of random numbers
A = np.random.random(15)
A = A.reshape(3,5)
A = np.matrix(A)

##find the size and length of the matrix
size = A.size #size of array
length = A.shape[1] #lenfth of array, which is 5 elements per row


#resize Matrix A to 3:4
A = A[0:4,0:4]
A

#Find the transpose of matrix A and assign it to B
B=A.T
B

#Find The minimum value in Column 1
B.min(1) # minimum value in each row in column 1
min_col_1 = B.min(1)
min_col_1.min() # minimum value in column 1

#Find the minimum and maximum value for the entire matrix
A.min()
A.max()

# Create vector X (an array) with 4 random numbers
X = np.random.rand(1,4)

# Create a functon and pass vector X and matrix A in it
def matrix_multiplication(vector,matrix):
    #Because X is shape(1,4) and A is Shape (3,4) multiplication will not work
    #Need to invert matrix to shape (4,3) usings SVD to invert matrix
    U,s,V = np.linalg.svd(A, full_matrices = False)
    S = np.diag(s)
    S[0,0], S[1,1], S[2,2] = 1/np.diag(S[0:3,0:3])
    X = np.dot(U, np.dot(S,V))
    X = X.T
    result = vector * X
    return result

D = matrix_multiplication(X,A)

# Create a complex number Z with absolute and real parts != 0
#show real and imaginary parts and absolute value
Z= 1 + 2j
Z.real
Z.imag
np.absolute(Z)

# Mul4ply result D with the absolute value of Z and record it to C
D * np.absolute(Z)

#Convert matrix B from a matrix to a string and overwrite B
B.tofile('my_array',sep=',', format='%s')
B = _file_operations.read_my_file()
B

print('Jordan is done with HW 2')