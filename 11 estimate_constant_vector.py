'''
Udemy - Data fusion with linear kalman filter 

PRACTICE for estimation of a constant vector


Estimation of a Constant Vector
Least Squares Estimation
Using the code template given, fill out the indicated areas to solve the following problems.
Write a function that calculates the general least squares solution x for a problem given the measurement vector y and model matrix H. (i.e. estimate the vector x for a given H matrix and y vector). (Hint: When using numpy arrays use the np.matmul(A,B) function to perform matrix multiplication, np.transpose(A) function to transpose a matrix and the np.linalg.inv(A) to calculate the matrix inverse)
Use your function to calculate the line of best fit (of linear form: y_i = x_1 * r_i + x_2) that describes the temperature (y_i) to RPM (r_i) relationship given noisy temperature measurements at different RPMs. The dataset input into the function is a list of measurements { [y_1, r_1], [y_2, r_2], ..., [y_n, r_n]}.


Notable libraries
numpy
np.transpose 
np.matmul --> to do matrix multiplication on 2 matrices (max is 2 for this function)
np.array --> to convert a list into an array 
np.linalg.inv --> to calculate the inverse of a matrix
'''

import numpy as np
import logging

def CalculateLeastSquaresSolution(Hmatrix,Ymatrix):
  # Enter Your Code Here to calculate the least Squares Solution
  H_transpose = np.transpose(Hmatrix)
  HTH_matrix = np.matmul(H_transpose,Hmatrix)
  HTH_and_Hinverse_matrix = np.matmul( np.linalg.inv(HTH_matrix), H_transpose)
  Xmatrix = np.matmul(HTH_and_Hinverse_matrix, Ymatrix)
  return Xmatrix;
  
def CalculateLineOfBestFitSolution(Dataset):
    # Generate the H and Y matrices for the Measurement Dataset
    # take note that Dataset is a list, not a numpy array
    Ymatrix = []
    Hmatrix = []
    for readings in Dataset:
        Ymatrix.append(readings[0])  #all the measurement values y1 y2 y3 .... yn 
        Hmatrix.append((readings[1], 1))  #all the rpm values, so r1 r2 r3 .... rn, and all the ones
    
    #optional    
    #Ymatrix_np =  np.array(Ymatrix)
    #Hmatrix_np = np.array(Hmatrix)
    
    LineParam = CalculateLeastSquaresSolution(Hmatrix, Ymatrix)
    return LineParam
