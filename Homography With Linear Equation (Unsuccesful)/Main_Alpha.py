# -*- coding: utf-8 -*-
"""
Created on Fri May  3 15:10:54 2024

@author: jpila
"""
import cv2 as cv
import numpy as np

################### Code For trying to Implement Homography With Lines correspondance

def findabc(pointA,pointB):
    # Input 2 points
    # Calculate a straight line equation a b c that passes throught these points
    # Output a b c normalize by c
    
    deltaX = pointB[0] - pointA[0]
    
    if(deltaX == 0):
        a = 1
        c = -pointA[0]
        b = 0
    else:
       a = (pointB[1] - pointA[1])/(deltaX)
    
       c = pointB[1] - a*pointB[0]
       
       b = -1
    
    print( 'y = ',a,'*x + ',c)
    
   
    return (a/c,b/c,c/c)


    
def pAppartient(point,a,c):
    #function  pour verifier si un point apartien bien  a une droite
    
    
    verY = a*point[0] + c
    print('verY = ',verY)
    if(abs(point[1] - verY) < 1):
        print('le Point appartient')
    else:
        print("Le Point n'appartient pas")



####First test of functions

# #L1
# print('L1')
# print('Obj')
# a1Obj, b1Obj, c1Obj = findabc([0,0],[0,117.4])
# print('Img')
# a1Img, b1Img, c1Img = findabc([365,29],[533,337])
# print('')

# #L2
# print('L2')
# print('Obj')
# a2Obj, b2Obj, c2Obj = findabc([0,0],[73.6,0])
# print('Img')
# a2Img, b2Img, c2Img = findabc([365,29],[123,60])
# print('')

# #L3
# print('L3')
# print('Obj')
# a3Obj, b3Obj, c3Obj = findabc([0,0],[73.6,117.4])
# print('Img')
# a3Img, b3Img, c3Img = findabc([365,29],[116,415])
# print('')

# #L4
# print('L4')
# print('Obj')
# a4Obj, b4Obj, c4Obj = findabc([0,117.4],[73.6,0])
# print('Img')
# a4Img, b4Img, c4Img = findabc([533,337],[123,60])
# print('')

# #L5
# print('L5')
# print('Obj')
# a5Obj, b5Obj, c5Obj = findabc([0,117.4],[73.6,117.4])
# print('Img')

# a5Img, b5Img, c5Img = findabc([533,337],[116,415])
# print('')

# #L6
# print('L6')
# print('Obj')
# a6Obj, b6Obj, c6Obj = findabc([73.6,0],[73.6,117.4])
# print('Img')
# a6Img, b6Img, c6Img = findabc([123,60],[116,415])
# print('')


# objPoints = np.float32([ [[26.5,6],[26.4,87.6]], [[8,40],[72.4,65.6]], [[52,0],[64.2,110]],[[1.2,88],[68.2,92]],
#                         [[7,14.4],[72.4,26]] , [[7.6,57.4],[47,106]], [[59,3.8],[35.4,45.4]], [[34.2,39],[44.4,112.8]] ])

objPoints = np.float32([ [[0,0],[0, 225]],[[70,373],[210,373]], [[0, 373],[280, 373]],[[210,225],[210,495]],
                        [[140, 225],[140, 373]], [[280, 225],[210, 373]], [[70, 373],[210, 495]], [[280, 0],[70, 495]],
                        [[70,225],[70,495]] ])

#better view 
objPoints = objPoints * 4


############## Line equations estimation of sets of 2 points

#L10
print('L10')
print('Obj')
#points 1 and 2-13
a10Obj, b10Obj, c10Obj = findabc(objPoints[0][0],objPoints[0][1])
print('Img')
a10Img, b10Img, c10Img = findabc([282,46],[352,244])
print('')

#L11
print('L11')
print('Obj')
#points 2 and 2-25
a11Obj, b11Obj, c11Obj = findabc(objPoints[1][0],objPoints[1][1])
print('Img')
a11Img, b11Img, c11Img = findabc([376,100],[123,205])
print('')

#L12
print('L12')
print('Obj')
#points 1-18 and 2-27
a12Obj, b12Obj, c12Obj = findabc(objPoints[2][0],objPoints[2][1])
print('Img')
a12Img, b12Img, c12Img = findabc([194,48],[167,371])
print('')

#L13
print('L13')
print('Obj')
#points 7 and 2-26
a13Obj, b13Obj, c13Obj = findabc(objPoints[3][0],objPoints[3][1])
print('Img')
a13Img, b13Img, c13Img = findabc([468,225],[145,293])
print('')


# #L14
# print('L14')
# print('Obj')
# #points 1-9 and 2-23
# a14Obj, b14Obj, c14Obj = findabc(objPoints[4][0],objPoints[4][1])
# print('Img')
# a14Img, b14Img, c14Img = findabc([355,54],[125,106])
# print('')

# #L15
# print('L15')
# print('Obj')
# #points 2-10 and 2-22
# a15Obj, b15Obj, c15Obj = findabc(objPoints[5][0],objPoints[5][1])
# print('Img')
# a15Img, b15Img, c15Img = findabc([397,139],[264,335])
# print('')

# #L16
# print('L16')
# print('Obj')
# #points 2-18 and 1-16
# a16Obj, b16Obj, c16Obj = findabc(objPoints[6][0],objPoints[6][1])
# print('Img')
# a16Img, b16Img, c16Img = findabc([170,59],[254,140])
# print('')

# #L17
# print('L17')
# print('Obj')
# #points 2-12 and 1-22
# a17Obj, b17Obj, c17Obj = findabc(objPoints[7][0],objPoints[7][1])
# print('Img')
# a17Img, b17Img, c17Img = findabc([275,110],[287,366])
# print('')

#L110
print('L110')
print('Obj')

a110Obj, b110Obj, c110Obj = findabc(objPoints[0][0],objPoints[0][1])
print('Img')
a110Img, b110Img, c110Img = findabc([154, 420],[171, 489])
print('')

#L111
print('L111')
print('Obj')

a111Obj, b111Obj, c111Obj = findabc(objPoints[1][0],objPoints[1][1])
print('Img')
a111Img, b111Img, c111Img = findabc([171,488], [501, 491])
print('')

#L112
print('L112')
print('Obj')

a112Obj, b112Obj, c112Obj = findabc(objPoints[2][0],objPoints[2][1])
print('Img')
a112Img, b112Img, c112Img = findabc([194, 583], [675, 583])
print('')

#L113
print('L113')
print('Obj')

a113Obj, b113Obj, c113Obj = findabc(objPoints[3][0],objPoints[3][1])
print('Img')
a113Img, b113Img, c113Img = findabc([254, 797], [1081, 797])
print('')
########

#L114
print('L114')
print('Obj')

a114Obj, b114Obj, c114Obj = findabc(objPoints[4][0],objPoints[4][1])
print('Img')
a114Img, b114Img, c114Img = findabc([338,492],[438,582])
print('')

#L115
print('L115')
print('Obj')

a115Obj, b115Obj, c115Obj = findabc(objPoints[5][0],objPoints[5][1])
print('Img')
a115Img, b115Img, c115Img = findabc([501,491], [563, 583])
print('')

#L116
print('L116')
print('Obj')

a116Obj, b116Obj, c116Obj = findabc(objPoints[6][0],objPoints[6][1])
print('Img')
a116Img, b116Img, c116Img = findabc([308,583], [904, 798])
print('')

#L117
print('L117')
print('Obj')

a117Obj, b117Obj, c117Obj = findabc(objPoints[7][0],objPoints[7][1])
print('Img')
a117Img, b117Img, c117Img = findabc([367, 421], [433, 797])
print('')

#L118
print('L118')
print('Obj')

a118Obj, b118Obj, c118Obj = findabc(objPoints[8][0],objPoints[8][1])
print('Img')
a118Img, b118Img, c118Img = findabc([241, 489], [433, 797])
print('')


# objL = np.float32([[a1Obj, b1Obj, c1Obj],[a2Obj,b2Obj, c2Obj],
#                     # [a3Obj, b3Obj, c3Obj],
#                     [a4Obj, b4Obj, c4Obj],
#                     [a5Obj, b5Obj, c5Obj],[a6Obj,b6Obj, c6Obj]])
#                     # [a7Obj, b7Obj, c7Obj], [a8Obj, b8Obj, c8Obj]])

# objL = np.float32([[a10Obj, b10Obj, c10Obj],[a11Obj,b11Obj, c11Obj],[a12Obj, b12Obj, c12Obj], [a13Obj, b13Obj, c13Obj]])
#                     # [a14Obj, b14Obj, c14Obj],[a15Obj,b15Obj, c15Obj],[a16Obj, b16Obj, c16Obj], [a17Obj, b17Obj, c17Obj]])

# imgL = np.float32([[a10Img, b10Img, c10Img],[a11Img,b11Img, c11Img],[a12Img, b12Img, c12Img],[a13Img, b13Img, c13Img]])
#                     # [a14Img, b14Img, c14Img],[a15Img,b15Img, c15Img],[a16Img, b16Img, c16Img],[a17Img, b17Img, c17Img]])
          

# imgL = np.float32([[a1Img, b1Img, c1Img],[a2Img,b2Img, c2Img],
#                     # [a3Img, b3Img, c3Img],
#                     [a4Img, b4Img, c4Img],
#                     [a5Img, b5Img, c5Img],[a6Img,b6Img, c6Img]])
#                     # [a7Img, b7Img, c7Img], [a8Img, b8Img, c8Img]])
                    
         


#######  Points to use with openCV function  (to compare results at the end)
objPt = np.float32([[0,0,0],[73.6,0,0],[0,117.4,0],[73.6,117.4,0]]) #1- 9
#better view 
objPt = objPt * 3
imgPt = np.float32([[366,29,0],[123,61,0],[533,337,0],[116,416,0]])#1- 9
#######                   



##### Different test with different points

# objL = np.float32([[0.222, -0.432, 100],[0.49, -0.544, 100],[-2.222, 0.585, 100],[0.108, -0.275, 100]])
# imgL = np.float32([[0, 1, 0],[0, 1, -2.8],[0, 1, -5.6], [8.4, -1, 0]])

# objL = np.float32([[0,0],[280, 0],[0, 225],[280, 225], [0, 373],[280,373],[0,495],[280, 495]])
# imgL = np.float32([[154, 420],[365, 419],[171,488], [501, 491], [194, 583], [675, 583], [254, 797], [1081, 797]])

# objL = np.float32([[a110Obj, b110Obj, c110Obj],[a111Obj, b111Obj, c111Obj],[a112Obj, b112Obj, c112Obj], [a113Obj, b113Obj, c113Obj]])
# imgL = np.float32([[a110Img, b110Img, c110Img],[a111Img,b111Img, c111Img],[a112Img, b112Img, c112Img],[a113Img, b113Img, c113Img]])


# objL = np.float32([[a110Obj, b110Obj, c110Obj],[a111Obj, b111Obj, c111Obj],[a112Obj, b112Obj, c112Obj], [a113Obj, b113Obj, c113Obj],
#                    [a114Obj, b114Obj, c114Obj],[a115Obj,b115Obj, c115Obj],[a116Obj, b116Obj, c116Obj], [a117Obj, b117Obj, c117Obj]])

# imgL = np.float32([[a110Img, b110Img, c110Img],[a111Img,b111Img, c111Img],[a112Img, b112Img, c112Img],[a113Img, b113Img, c113Img],
#                    [a114Img, b114Img, c114Img],[a115Img,b115Img, c115Img],[a116Img, b116Img, c116Img],[a117Img, b117Img, c117Img]])



####Final test
objL = np.float32([[a111Obj, b111Obj, c111Obj],[a113Obj, b113Obj, c113Obj],
                    [a114Obj, b114Obj, c114Obj],[a118Obj,b118Obj, c118Obj]])

imgL = np.float32([[a111Img,b111Img, c111Img],[a113Img, b113Img, c113Img],
                    [a114Img, b114Img, c114Img],[a118Img, b118Img, c118Img]])


print('objl = ', objL)
print('imgla = ', imgL)

def getT1(Lines):
    #Get matrix T1
    
    #Get the sum of all a, b and c
    t1, t2, t3 = np.sum(Lines, axis=0)
  
    #Construct the T1 Matrix
    T1 = np.array([
        [1,0,-t1/t3],
        [0,1,-t2/t3],
        [0,0,1]
        ])
    
    print('')
    print('T1 = ',T1)
    print('')
    
    return T1

def getLPrime(T, Lines):
    #Pour toute les lignes appliquer (produit matriciel avec ) la matrice T
    Lprimes = []
    
    
    for i in range(0, Lines.shape[0]):
        Lprimes.append( T @ Lines[i, :].reshape((3,1)) )
    
    return np.array(Lprimes)
          
def getT2(LinesPrime):
    #Get matrix T2
    
    num = denom = 0
    
    #T2 is equals to the square root of sum of the numerator divided by the denominator
    for i in range(0, LinesPrime.shape[0]):
        print("i a' b' =",i, LinesPrime[i, 0, 0], LinesPrime[i, 1, 0])
        
        #Get numerator that is the sum of  = ai^2 + bi^2 
        num   += LinesPrime[i, 0, 0]**2 + LinesPrime[i, 1, 0]**2
        
        #Get denominator that is the sum of = ci^2
        denom += LinesPrime[i, 2, 0]**2

    s = num / (2 * denom)
    s = np.sqrt(s)

    #Construct the T2 Matrix
    T2 = np.array([[1,0,0],
                [0,1,0],
                [0,0,s]
                ])
    
    print('')
    print('T2 = ',T2)
    print('')
    
    return T2
          


def normalize(Lines):
    # function to normalize every line
    normalizeLines = []

    for i in range(Lines.shape[0]):
        norm  = np.linalg.norm(Lines[i, :])
        normalizeLines.append(Lines[i, :]/norm)

    normalizeLines = np.float32(normalizeLines) 
     
    return normalizeLines


def getA(objLPP, imgLPP):
    # Get Known matrix A of our homography  Linear equation  calculus A.h = 0
    # We tested different structures of A to see wich one could work
    A_matrix = []
    for i in range (objLPP.shape[0]):
        # a = objLPP[i][0][0] 
        # b = objLPP[i][1][0] 
        # c = objLPP[i][2][0]
        # a_p = imgLPP[i][0][0] 
        # b_p = imgLPP[i][1][0] 
        # c_p = imgLPP[i][2][0] 
        
        # A_matrix.append([0, 0, 0, -c_p*a, -c_p*b, -c_p*c, b_p*a, b_p*b, b_p*c])
        # A_matrix.append([c_p*a, c_p*b, c_p*c, 0, 0, 0, -a_p*a, -a_p*b, -a_p*c])
        
        
        x = objLPP[i][0][0] 
        y = objLPP[i][1][0] 
        z = objLPP[i][2][0]
        u = imgLPP[i][0][0] 
        v = imgLPP[i][1][0] 
        w = imgLPP[i][2][0] 

        # A_matrix.append([0, 0, 0, -z*u, -z*v, -z*w, y*u, y*v, y*w])
        # A_matrix.append([z*u, z*v, z*w, 0, 0, 0, -x*u, -x*v, -x*w])
        
        A_matrix.append([0, -z*u, y*u, 0, -z*v, -y*v, 0, -z*w, y*w])
        A_matrix.append([z*u, 0, -x*u, z*v, 0, -x*v, z*w, 0, -x*w])
    
   # print('A_Matrix = ', A_matrix)
    A_matrix = np.float32(A_matrix)
            
    return A_matrix



#### From source image    
T1Obj = getT1(objL)
LObjPrime = getLPrime(T1Obj, objL)   
print('ObjectL Prime = ',LObjPrime)
print('')

T2Obj = getT2(LObjPrime)
L2ObjPrime = getLPrime(T2Obj, LObjPrime)
print('ObjectL Prime Prime = ',L2ObjPrime)
print('')


nObjL2Prime = normalize(L2ObjPrime)

print('nObjL2Prime = ',nObjL2Prime)
print('')
####

#### from image
T1Img = getT1(imgL)
LImgPrime = getLPrime(T1Img, imgL)
print('Image L Prime = ',LImgPrime)
print('')


T2Img = getT2(LImgPrime)
L2ImgPrime = getLPrime(T2Img, LImgPrime)
print('Image L Prime = ',L2ImgPrime)
print('')

nImgL2Prime = normalize(L2ImgPrime)


print('nImgL2Prime = ',nImgL2Prime, 'Shape =', nImgL2Prime.shape)
print('')    
####


A = getA(nObjL2Prime, nImgL2Prime)


# print('')
# print('A shape = ', A.shape)
# print('')
# #with A , Compute the homography matrix

U,S,V = np.linalg.svd(A)

# print('S = ', S)
# print('V = ', V)
# print('V shape = ', type(V))

h = V[-1]

# print('h = ', h)
# print('h shape = ', h.shape)

HPrime = h.reshape((3,3))

# HPrime = HPrime/HPrime[-1,-1]


print('')
print('H Prime = ', HPrime)
print('')
print('H shape', HPrime.shape)

###############Denormalization
T1Objt = np.transpose(T1Obj)
T2Objt = np.transpose(T2Obj)

T1ImgInv = np.linalg.inv(T1Img)
T2ImgInv = np.linalg.inv(T2Img)
T1ImgInvt = np.transpose(T1ImgInv)
T2ImgInvt = np.transpose(T2ImgInv)

H = np.dot(T1Objt,T2Objt)
H = np.dot(H,HPrime)
H = np.dot(H,T1ImgInvt)
H = np.dot(H,T2ImgInvt)
# print('H =', H)
################

## Test of inversing the H matrix
# Hinv = np.linalg.inv(H)
# hHinv = np.linalg.inv(HPrime)

## OpenCV way of computing homography with points correspondance
cvH, _ = cv.findHomography(imgL,objL)


# ######Results
img1 = cv.imread('image_hold3.jpg')


cvtImg = cv.warpPerspective(img1, cvH, (img1.shape[1],img1.shape[0]))
tImg = cv.warpPerspective(img1, H, (img1.shape[1],img1.shape[0]))

cv.imshow('Case Study', img1)
cv.waitKey(0)
cv.destroyAllWindows()

cv.imshow('Transformation', tImg)
cv.waitKey(0)
cv.destroyAllWindows()
cv.imwrite('analysis.jpg', tImg)

# cv.imshow('Transformation OpenCV', cvtImg)
# cv.waitKey(0)
# cv.destroyAllWindows()
# # cv.imwrite('analysis.jpg', tImg)

toShow = np.concatenate((img1, tImg), axis=1) 
# toShow = np.concatenate((toShow, cvtImg), axis=1) 
cv.imshow('Comparation', toShow)
cv.waitKey(0)
cv.destroyAllWindows()