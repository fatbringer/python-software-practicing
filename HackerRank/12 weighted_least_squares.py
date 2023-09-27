```
Udemy - data fusion with linear kalman filter
PRACTICE for Weighted Least Squares

Weighted Least Squares
Weighted Least Squares Estimation
Using the code template given, fill out the indicated areas to solve the following problems.
Write a function that calculates the weighted least squares solution x and P for a problem given the measurement vector y, measurement uncertainty covariance matrix R and model matrix H. (i.e. estimate the vector x for a given H matrix, R matrix and y vector). (Hint: When using numpy arrays use the np.matmul(A,B) function to perform matrix multiplication, np.transpose(A) function to transpose a matrix and the np.linalg.inv(A) to calculate the matrix inverse)
Use your function to calculate the line of best fit (of linear form: y_i = x_1 * r_i + x_2) that describes the temperature (y_i) to RPM (r_i) relationship given noisy temperature measurements at different RPMs with different measurement uncertainties (sigma_i). The dataset input into the function is a list of measurements { [y_1, r_1, sigma_1], [y_2, r_2,sigma_2], ..., [y_n, r_n,sigma_n]}. For example Dataset = [[65,1,1], [65,2,2], ... , [97,5,1]].

Notable libaries 
numy as np
np.transpose
np.linalg.inv
np.matmul only works on 2 matrices at 1 go
usin the @ operator lets you do multiple matrix multiplcations in 1 line in that specified order

```

import numpy as np

def CalculateWeightedLeastSquaresSolution(Hmatrix, Rmatrix, Ymatrix):
  # Enter Your Code Here to calculate the least Squares Solution
  Xmatrix = []
  Pmatrix = []
  H_trans = np.transpose(Hmatrix)
  R_inv = np.linalg.inv(Rmatrix)
  
  #Pmatrix = np.linalg.inv( np.matmul(np.matmul(H_trans, R_inv), Hmatrix)) 
  Pmatrix = np.linalg.inv( H_trans @ R_inv @ Hmatrix)
  #matmul can only do between 2 matrices each time, so you need to chain them
  # you can use the @ operator to do the matrix multiplication too, but must be in correct order
  Amat = np.matmul(np.matmul(Pmatrix, H_trans), R_inv)
  Xmatrix = np.matmul(Amat, Ymatrix)
  
  
  return Xmatrix, Pmatrix;
  
def CalculateLineOfBestFitSolution(Dataset):
    # Generate the H, R and Y matrices for the Measurement Dataset
    Hmatrix = []
    Rmatrix = []
    Ymatrix = []
    
    for reading in Dataset:
        Ymatrix.append(reading[0]) #all the measurement values y1 y2 y3 ... yn 
        Hmatrix.append((reading[1], 1)) #all the rpm values r1 r2 r3 .... rn 
        Rmatrix.append(reading[2]**2) #all the sigma values, rmb to square them
        
    Rmatrix = np.diag(Rmatrix)
        
    LineParam, LineParamCov = CalculateWeightedLeastSquaresSolution(Hmatrix, Rmatrix, Ymatrix)
    return LineParam
