# -*- coding: utf-8 -*-
"""
Created on Wed Feb  7 00:41:08 2018

@author: Andy
"""

'''
Inputs
    datafile: a .csv format file with n columns

Outputs
    
'''

import codecs
import csv
import pickle
import numpy as np
from DataStruct import DataStruct


def read_csv_file(datafile, trainfile, testfile):
    '''
    Input:
        datafile:   .csv file
        trainfile:  name of file to write formatted training data
        testfile:   name of file to write formatted test data
    Output:
        No return value
    
    Opens the given file. Assumes the data inside is in csv format.
    Reads all rows of the csv file into a list.
    Uses pickle to dump the list into the output files.
        100,000 datapoints in training data
        remaining datapoints go to test data (around 50,000)
    '''
    
    # read the input
    csvfile = codecs.open(datafile, 'r', encoding='utf8')
    reader = csv.DictReader(csvfile)

    # add to the list    
    outputdata = []
    for row in reader:
        outputdata.append( [row['id'], row['comment_text'], row['toxic'], row['severe_toxic'],
                            row['obscene'], row['threat'], row['insult'], row['identity_hate']] )
    csvfile.close()
    
    # shuffle the data; randomization
    np.random.shuffle(outputdata)
    
    # pickle training data to output file; 100000 data points for training
    with open(trainfile, 'wb') as fp:
        pickle.dump(outputdata[0:100000], fp)
    fp.close()
    
    # pickle test data to output file; remaining data points (around 50000) for testing
    with open(testfile, 'wb') as fp:
        pickle.dump(outputdata[100000:], fp)
    fp.close()
    
    return

def read_data(datafile):
    '''
    Input:
        datafile:  Input file to read data
    Ouput:
        Returns a DataStruct object initialized on the data from datafile
    '''
    file = open(datafile, 'rb')
    data = pickle.load(file)
    file.close()
    
    return DataStruct(data)


if __name__ == '__main__':
    read_csv_file('train.csv', 'traindata.data', 'testdata.data') # pickle the data
    trainds = read_data('traindata.data')             # read training data into data struct
    print(trainds[0])                            # some testing to make sure it works