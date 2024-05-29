# -*- coding: utf-8 -*-
"""
Created on Fri May  3 15:10:54 2024

@author: jpila
"""

import CameraCalibration as CC
import SizeEstimations as SE
import cv2 as cv
import numpy as np
from findHomgraphyLines import dlt_with_lines

# objL = np.float32([#[-2.42, 1.0, -51.98],[-1.7134, 1.0, 0.0],[0.87, 1.0, -89.141],[1.96, 1.0, -97.984],
#                    [0,-1,0], [1,0,0], [1,0,-73.6], [0,1,-117.4]
# ])

# imgL = np.float32([#[9.93, 1.0, -4300.0],[1.736, 1.0, -660.92],[-0.348, 1.0, -61.16],[-0.698, 1.0, 94.521],
#                    [0.1276,1,75.7],[-1.84, 1.0, 643.83],[64.64, 1.0, -7978.954],[0.191, 1.0, -438.2371]
# ])

objL = np.float32([[0.0472, -0.01925, 1.0],[-0.01, -0.01123, 1.0],[-0.02, -0.01022, 1.0],
                   [-0.0136, 0.0, 1.0]
])

imgL = np.float32([[-0.0023, -0.00023, 1.0],[0.0057, -0.0164, 1.0],[-0.0074, 0.0106, 1.0],
                   [-0.008, -0.000126, 1.0]
])


# objL = np.array([[2.5,-1, 51.95],[1.71,-1,0.22],[-1.15,-1,89.38],[-10.2,-1,449.12],
#                    [0,-1,0], [1,0,0], [73.6,0,0], [0,-117.4,0]
# ])

# imgL = np.array([[-9.8,-1,4245],[-1.73,-1,662.6],[0.35,-1,61.2],[2.34,-1,-470],
#                    [-0.13,-1,76.99],[1.8,-1,-646.3],[-44.3,-1,5510.5],[-0.19,-1,439.06]
# ])

def getT1(Lines):

    t1, t2, t3 = np.sum(Lines, axis=0)
  
    T1 = np.array([
        [1,0,-t1/t3],
        [0,1,-t2/t3],
        [0,0,1]
        ])
    
    print(f"T1 = {T1}")
    
    return T1

def getLPrime(T, Lines):
     
    Lprimes = []
    for i in range(0, Lines.shape[0]):
        Lprimes.append( T @ Lines[i, :].reshape((3,1)) )
        #Lprimes.append( T @ objL[i, :] ) #, :].reshape((3,1)) )
        
    return np.array(Lprimes)

def getL2Prime(T, Lines):
     
    Lprimes = []
    for i in range(0, Lines.shape[0]):
        Lprimes.append( T @ Lines[i, :] )
        #Lprimes.append( T @ objL[i, :] ) #, :].reshape((3,1)) )
        
    return np.array(Lprimes)
          
def getT2(LinesPrime):

    num = denom = 0
    for i in range(0, LinesPrime.shape[0]):
        print(i, LinesPrime[i], LinesPrime[i].shape, LinesPrime[i, 0, 0], LinesPrime[i, 1, 0], LinesPrime[i, 2, 0])
        #print(i, LinesPrime[i, 0, 0], LinesPrime[i, 1, 0])
        #num   += LinesPrime[i, 0, 0]**2 + LinesPrime[i, 1, 0]**2
        #denom += LinesPrime[i, 2, 0]**2
        #a, b, c = LinesPrime[i]
        #LinesPrime = LinesPrime**2
        a, b, c = np.sum(LinesPrime, axis=0).reshape((3, ))
        # a = np.sum(LinesPrime[:,0])
        # b = np.sum(LinesPrime[:,1])
        # c = np.sum(LinesPrime[:,2])
        # a = LinesPrime[i, 0, 0]
        # b =  LinesPrime[i, 1, 0]
        # c = LinesPrime[i, 2, 0]
        
        # num   += a**2 + b**2
        # denom += c**2

    #s = num / (2 * denom)
    #s = np.sqrt(s)
    LinesPrime = LinesPrime**2
    A, B, C = np.sum(LinesPrime, axis=0).reshape((3, ))
    s = np.sqrt( (A + B) / (2*C) )

    T2 = np.array([[1, 0, 0],
                   [0,1,0],
                   [0,0, s]
                ])
    return T2
          
# def getL2Prime(LinesPrime):
#     s = getT2(LinesPrime)
    
#     T2 = np.float32([[1,0,0],
#           [0,1,0],
#           [0,0,s]])
    
#     print('T2 = ',T2)
#     print('')
    
#     L1 = np.dot(T2, LinesPrime[0].reshape((3,1)))
#     R = np.float32([L1])


#     for i in range(1,LinesPrime.shape[0]):
#         Li = np.dot(T2, LinesPrime[i].reshape((3,1)))
        
#         R = np.concatenate((R,np.array([Li])))
              
#     print('R = ', R)
#     print('')
#     return (R,T2)

def normalize(Lines):

    normalizeLines = []

    for i in range(Lines.shape[0]):
        norm  = np.linalg.norm(Lines[i, :])
        normalizeLines.append(Lines[i, :]/norm)

    normalizeLines = np.array(normalizeLines) 
     
    return normalizeLines

def getA(nobjLPP, nimgLPP):

    A_matrix = []
    for i in range (nobjLPP.shape[0]):
        print(nobjLPP[i].T[0], nobjLPP[i].T[0].shape, nobjLPP[i], "==================================")
        x, y, z = nobjLPP[i].reshape((3, )) #.T[0]
        u, v, w = nimgLPP[i].reshape((3, )) #.T[0]
        #x, y = x, y
        #u, v = v, v
        #x = nobjLPP[i][0]
        #y = nobjLPP[i][1]
        #u = nimgLPP[i][0]
        #v = nimgLPP[i][1]

        #A_matrix.append([-u, 0, u*x, -v, 0, v*x, -1, 0, x])
        #A_matrix.append([0, -u, u*y, 0, -v, v*y, 0, -1, y])

        A_matrix.append([0, 0, 0, -w*x, -w*y, -w*z, v*x, v*y, v*z])
        A_matrix.append([w*x, w*y, w*z, 0, 0, 0, -u*x, -u*y, -u*z])

        #A_matrix.append([-x, 0, u*x, -y, 0, v*x, -1, 0, u])
        #A_matrix.append([0, -x, u*y, 0, -y, v*y, 0, -1, v])

    A_matrix = np.array(A_matrix)
            
    return A_matrix

# From source image    
T1Obj = getT1(objL)
LObjPrime = getLPrime(T1Obj, objL)  
print(f"LObjPrime = {LObjPrime}")  
T2Obj = getT2(LObjPrime) 
l2Prime = getL2Prime(T2Obj, LObjPrime)
print(f"T2Obj = {T2Obj}") 
print(f"LObj2Prime = {l2Prime}")  
nObjL2Prime = normalize(l2Prime)

print('nObjLPrime = ',nObjL2Prime, nObjL2Prime.dtype, nObjL2Prime.shape, nObjL2Prime.T.shape, nObjL2Prime.T)
print('')

# from image
T1Img = getT1(imgL)
LImgPrime = getLPrime(T1Img, imgL)    
T2Img = getT2(LImgPrime)
LImg2Prime = getL2Prime(T2Img, LImgPrime)
nImgL2Prime = normalize(LImg2Prime)

print('nImgLPrime = ',LImg2Prime)
print('')    

A = getA(nObjL2Prime, nImgL2Prime)

#A = getA(objL,imgL)
print('')
print('A shape = ', A.shape)
print('')
# #with A , Compute the homography matrix

U,S,V = np.linalg.svd(A)
print('S = ', S)
print('V = ', V)
print('V shape = ', type(V))

h = V[-1] #/V[-1, -1]
print('h = ', h)
print('h shape = ', h.shape)

HPrime = h.reshape((3,3)).T
#HPrime = HPrime /HPrime[2,2]


print('')
print('H Prime = ', HPrime)
print('')
print('H shape', HPrime.shape)

#Denormalization
T1Objt = np.transpose(T1Obj)
T2Objt = np.transpose(T2Obj)

T1ImgInv = np.linalg.inv(T1Img)
T2ImgInv = np.linalg.inv(T2Img)
T1ImgInvt = np.transpose(T1ImgInv)
T2ImgInvt = np.transpose(T2ImgInv)

#H = np.dot(T1Objt,T2Objt)
#H = np.dot(H,HPrime)
#H = np.dot(H,T1ImgInvt)
#H = np.dot(H,T2ImgInvt)
#H = T2Objt @ T1Objt @ H @ T2ImgInvt @ T1ImgInvt
H = (T2Objt @ T1Objt) @ HPrime @ (T1ImgInvt @ T2ImgInvt)
#H = T2ImgInvt @ T1ImgInvt @ HPrime @ T1Objt @ T2Objt 

H_dlt = dlt_with_lines(objL, imgL)
#H = np.linalg.inv(H)
#Hinv = np.transpose(H_dlt)

# ######Results
img1 = cv.imread('Test.jpg')

#HPrimeInv = np.linalg.inv(HPrime)
tImg = cv.warpPerspective(img1, H, (img1.shape[1],img1.shape[0]))
#tImg = cv.warpPerspective(img1, H, (img1.shape[1],img1.shape[0]))

cv.imshow('Case Study', img1)
cv.waitKey(0)
cv.destroyAllWindows()

cv.imshow('Transformation', tImg)
cv.waitKey(0)
cv.destroyAllWindows()
cv.imwrite('analysis.jpg', tImg)

toShow = np.concatenate((img1, tImg), axis=1) 
cv.imshow('Comparation', toShow)
cv.waitKey(0)
cv.destroyAllWindows()