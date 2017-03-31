# coding: utf-8
import numpy as np
hight = float(input('what is your hight(m)?\t'))
weight = float(input('what is your weight(kg)?\t'))
bmi = weight/np.power(hight,2)
print('your bmi is %.2f' %(bmi))
if bmi < 18.5:
    print('you are too thin!!')
elif bmi < 24 and bmi >= 18.5:
    print('Congratulation!! you are fit!!')
else:
    print('maybe you are overweight!!')
