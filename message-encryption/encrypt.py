'''
DESCRIPTION :

This is an simple encryption program that gets input message as string value and enodes using matrix 
inversion method and produce a encrypted code starting with '#'.
The encrypted code is again decrypted and produced as output.
You can also print the encrypted code.



---------------------------------------------
Created on Sun Aug 21 2022
purpose : Encrytion using matrix in python
@author : Santhosh
--------------------------------------------
'''


import random
import numpy as np


# functions for basic math operation

def multiply(mat1,mat2):
    result = [[]]
    for i in range(len(mat1[0])):
        result[0].append(0)
    
    for i in range(len(mat1)):
 
        for j in range(len(mat2[0])):
                
            for k in range(len(mat2)):
                result[i][j] += mat1[i][k] * mat2[k][j]
 
    return result



def determination(mat):
    val = np.array(mat) 
    det = np.linalg.det(val)
    return det


def matrixInversion(mat):
    rough_inversion=np.linalg.inv(mat)
    iMatrix=[]
    for i in rough_inversion:
        val=[]
        for j in i:
            val.append(float(j))
        iMatrix.append(val)
    return iMatrix

#function to randomly generate key value

def generateKeyMatrix(len):
    keyMatrix=[]
    for i in range(len):
        val=[]
        for j in range(len):
            r=random.randint(0,9)
            val.append(r)
        keyMatrix.append(val)
    if determination(keyMatrix)!=0:
        return keyMatrix
    else:
        generateKeyMatrix(len(keyMatrix))


#functions to convert text to ascii and vice versa

def strToMatrix(str):
    eMatrix=[[]]
    for i in str:
        if i==" ":
            eMatrix[0].append(226)
        else:
            eMatrix[0].append(ord(i))
    return eMatrix



def matrixToStr(mat):
    message=""
    for i in mat:
        for j in i:
            if j==226:
                message+=" "
            else:
                message+=chr(j)

    return message







#input section

input_message=str(input("Enter Your message : "))

"--------ENCODING---------"

#encoding text to ascii value

ascci_matrix=strToMatrix(input_message)



#key matrix generation and it is completely randomized

key_matrix=generateKeyMatrix(len(input_message))


#chiper matrix generated as encrypted code 


chiper_matrix=multiply(ascci_matrix,key_matrix)


encode_value="#"
for i in chiper_matrix:
    for j in i:
        encode_value+=":"
        encode_value+=str(j)

#the 'encode_value' is the encrypted value of input

print("Encrypted value : "+encode_value)       


"---------DECODING------------"

#matrix inversion

imatrix=matrixInversion(key_matrix)

#decrypting chipper to ascii 

decrypt_matrix=multiply(chiper_matrix,imatrix)


for i in decrypt_matrix:
    c=0
    for j in i:
        decrypt_matrix[0][c]=round(j)
        c+=1

#decoding matrix from ascii value to text

message=matrixToStr(decrypt_matrix)

print(message)


'''End of program !!!'''



'''This is an completely randomized program that chiper value will differ for same input at every time !!!'''