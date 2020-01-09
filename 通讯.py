# -*- coding: utf-8 -*-
"""
Created on Tue Jan  7 11:31:36 2020

@author: Simon
"""

x = 121
x_data = str(x)

y = 121
y_data = str(x)

"""
冗余算法通讯
"""
#通道A
with open("x.txt", "w") as f:
    f.write(x_data)
    
with open("x.txt", 'r') as f:
    contents = f.read()
    print(contents)


#通道B（冗余通道）
with open("xb.txt", "w") as f:
    f.write(x_data)
    
with open("xb.txt", 'r') as f:
    contents = f.read()
    print(contents)



#通道A
with open("y.txt", "w") as f:
    f.write(y_data)
    
with open("y.txt", 'r') as f:
    contents = f.read()
    print(contents)


#通道B（冗余通道）
with open("yb.txt", "w") as f:
    f.write(y_data)
    
with open("yb.txt", 'r') as f:
    contents = f.read()
    print(contents)


try :
    with open("y.txt", 'r') as f:
        y_contents = f.read()
        print(y_contents)
        
    

except:
    with open("yb.txt", 'r') as f:
        y_contents = f.read()
        print(y_contents)