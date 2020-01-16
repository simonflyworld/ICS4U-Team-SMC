# -*- coding: utf-8 -*-
"""
Created on Mon Jan  6 10:21:42 2020

@author: Simon
"""
from typing import List
import numpy as np

class UserHabitLearn:
    """
    This class is a user habit learning class.
    This class use essential machine learning to learn user habit.
    It is also an API that helps data science people to sort and clean the data.
    It even able to train the Vision class CNN network by its self.
    """
    database = {}
    def __init__(self, name: str):
        """
         Initialize userhabitlearn class
        
        arg:
            name: name of the data for this time
            x_contents:The x value read out from data base
            y_contents:The y value read out from data base
            database: This is a dictionary that storge data from the database
        """
        self.name = name
        with open("x_data(for_training).txt", "r") as f:
           #self.x_contents = f.read()      
           database = {"x":list(map(int, f.read().split(",")))}
           #print(database)
        
        with open("y_data(for_training).txt", "r") as f:
           #self.y_contents = f.read()
           database["y"] = f.read().split(",")
        self.database = database
        print(self.database)
    
    def merge_sort(numbers: List[int]) -> List[int]:
        """
        This is the merge sort function that use to sort the data
        It uses merge sort which useing recursion
        
        arg:
            
        """
        # base case
        if len(numbers) == 1:
            return numbers
    
        midpoint = len(numbers)//2
    
        # two recursive steps
        # mergesort left
        left_side = UserHabitLearn.merge_sort(numbers[:midpoint])
        # mergesort right
        right_side = UserHabitLearn.merge_sort(numbers[midpoint:])
        # merge the two together
        sorted_list = []
    
        # loop through both lists with two markers
        left_marker = 0
        right_marker = 0
        while left_marker < len(left_side) and right_marker < len(right_side):
            # if right value less than left value, add right value to sorted, increase right marker
            if left_side[left_marker] < right_side[right_marker]:
                sorted_list.append(left_side[left_marker])
                left_marker += 1
            # if left value less than right value, add left value to sorted, increase left marker
            else:
                sorted_list.append(right_side[right_marker])
                right_marker += 1
        
        # create a while loop to gather the rest of the values from either list
        while right_marker < len(right_side):
            sorted_list.append(right_side[right_marker])
            right_marker += 1
        
        while left_marker < len(left_side):
            sorted_list.append(left_side[left_marker])
            left_marker += 1
        
        # return the sorted list
        return sorted_list
    
    def sort(self):
        print(type(self))
        x_value_list = self.database['x']
        self.database.pop("x")
        y_value_list = self.database["y"]
        self.database.pop("y")
        sorted_x = UserHabitLearn.merge_sort(x_value_list)
        sorted_y = UserHabitLearn.merge_sort(y_value_list)
        self.database = {"x":sorted_x}
        self.database["y"] = sorted_y
    
    
    
    def find_x_mode(self):
        print(self.database)
        x_value_list = self.database['x']
        maximum = x_value_list.index(min(x_value_list))
        minimum = x_value_list.index(max(x_value_list))
        x_value_list.pop(maximum-1)
        x_value_list.pop(minimum-1)
        counts = np.bincount(x_value_list)
        #返回众数
        x_mode = np.argmax(counts)
        
        return x_mode

    def find_y_mode(self):
        y_value_list = self.database["y"]
        maximum = y_value_list.index(min(y_value_list))
        minimum = y_value_list.index(max(y_value_list))
        y_value_list.pop(maximum-1)
        y_value_list.pop(minimum-1)
        counts = np.bincount(y_value_list)
        #返回众数
        y_mode = np.argmax(counts)
        
        return y_mode
class Calc:
    # 初始化
    def __init__(self, a, b):
        self.a = a
        self.b = b
  
    # 重置值
    def set_a_b(self, a, b):
        self.a = a
        self.b = b
    
    # 加法
    def __add(self):
        '''
        :return:self.a + self.b
        '''
        return self.a + self.b

    # 减法
    def __sub(self):

        return self.a - self.b

    # 乘法
    def _mul(self):
        return self.a * self.b

    # 除法
    def _div(self):
        # a / b 2和3版本的除法有稍许变化
        if self.b != 0:
            return self.a // self.b
        else:
            raise ('除数为0，无法计算！')

    # 加法
    def get_adds(self):
        return self.__add()

    # 减法
    def get_subs(self):
        return self.__sub()

    def get_muls(self):
        return self._mul()
    
    def get_divs(self):
        return self._div()
    
    """
    math API package
    Feel free to use if you needed
    01/15/2020 Simon Li
    Here is how you use it
    eg = Calc(2, 6)
    print(eg.get_adds())
    print(eg.get_subs())
    eg.set_a_b(9, 6)
    print(eg.get_divs())
    print(eg.get_muls())
    user_habit_learn.ellipse_detect()
    """




if __name__ == "__main__":
    user_habit_learn = UserHabitLearn("你妈逼的")
    user_habit_learn.sort()
    print(user_habit_learn.find_x_mode())
    print(user_habit_learn.find_y_mode())