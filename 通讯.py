# -*- coding: utf-8 -*-
"""
Created on Tue Jan  7 11:31:36 2020

@author: Simon
"""

import multiprocessing
#import os
def send(x,y,conn):  #conn管道类型
    conn.send(x,y)  #发送的数据
    conn.close()  #关闭
 
def reciver(conn):
    print(conn.recv())
 
if  __name__=="__main__":
    conn_a,conn_b=multiprocessing.Pipe() #创建一个管道，两个口
    """
    接口x,y
    """
    sender=multiprocessing.Process(target=send,args=(x,y,conn_a,))
    sender.start()
    reciver(conn_b)
    sender.join()
