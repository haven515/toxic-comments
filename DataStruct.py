# -*- coding: utf-8 -*-
"""
Created on Wed Feb 14 15:24:29 2018

@author: Andy
"""

'''
A class meant to containg the training data for the project.
Pass an array of length M of 8-tuples to DataStruct(data) to initialize.
This class supports indexing into the ith data point
    and accessing specific columns of data.
    # ds = DataStruct(data)
    # ds[99]       <- returns the 100th data point from the data as an 8-tuple
    # ds.text      <- returns a list of all the text of the data points
    # ds.text[5]   <- returns the text of the 6th datapoint
    # ds.c4[7]     <- returns classification of class 4 on 8th datapoint
'''

class DataStruct():
    
    def __init__(self, data):
        '''
        Input:
            data: a list containing 8-tuples (essentially a Mx8 matrix)
        Output:
            No output
        '''
        id = []
        text = []
        class1 = []
        class2 = []
        class3 = []
        class4 = []
        class5 = []
        class6 = []
        length = 0
        
        for row in data:
            id.append(row[0])
            text.append(row[1])
            class1.append(row[2])
            class2.append(row[3])
            class3.append(row[4])
            class4.append(row[5])
            class5.append(row[6])
            class6.append(row[7])
            length += 1
        
        self.id = id
        self.text = text
        self.c1 = class1
        self.c2 = class2
        self.c3 = class3
        self.c4 = class4
        self.c5 = class5
        self.c6 = class6
        self.length = length
        
    def id(self):
        '''
        Output:
            Returns self.id, a list containing a 16 character string
        '''
        return self.id
    
    def text(self):
        '''
        Output:
            Returns self.text, a list containing strings
        '''
        return self.text
    
    '''
    The following methods return self.cX.
    The output is a list of strings.
        The string are either '0' or '1'.
    '''
    def c1(self):
        return self.c1
    def c2(self):
        return self.c2
    def c3(self):
        return self.c3
    def c4(self):
        return self.c4
    def c5(self):
        return self.c5
    def c6(self):
        return self.c6
    
    def __getitem__(self, index):
        '''
        Overloading the indexing [] operator
        Output:
            Returns an 8-tuple formed with the ith string of each attribute
        '''
        return (self.id[index], self.text[index], self.c1[index],
                self.c2[index], self.c3[index], self.c4[index], self.c5[index],
                self.c6[index])
    
    def __len__(self):
        '''
        Overloads the len() operator. Allows len(DataStruct_object) to work.
        Returns an integer containing the length of the attributes
        '''
        return self.length
    
    