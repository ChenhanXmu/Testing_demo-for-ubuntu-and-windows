import numpy as np
import matplotlib.pyplot as plt
import os.path
import json
import scipy
import argparse
import math
import pylab
from sklearn.preprocessing import normalize
from mpl_toolkits.mplot3d import Axes3D

# Make sure that caffe is on the python path:
caffe_root = ''  # Change to your directory to caffe
import sys
sys.path.insert(0, caffe_root + 'python')
import caffe

# Import arguments
parser = argparse.ArgumentParser()
MODEL_FILE = '/home/hjb/posenet/posenet/models/test_jiannandalitang.prototxt'
WEIGHTS = '/home/hjb/posenet/xmu_final_models/jiannandalitang/jiannandalitang_iter_32500.caffemodel'

#args = parser.parse_args()

caffe.set_mode_gpu()

net = caffe.Net(MODEL_FILE,
                WEIGHTS,
                caffe.TEST)
net.forward()


predicted_q = net.blobs['cls3_fc_wpqr'].data 
predicted_x = net.blobs['cls3_fc_xyz'].data  

 

predicted_q = np.squeeze(predicted_q)
predicted_x = np.squeeze(predicted_x)

result=np.append(predicted_x,predicted_q,axis=0)
#predicted_q = np.squeeze(predicted_q)
#predicted_x = np.squeeze(predicted_x)
print 'xyz,wpqr',result
result=np.ndarray.tolist(result)
 
result[0]= float('%0.6f'%result[0])
result[1]= float('%0.6f'%result[1])
result[2]= float('%0.6f'%result[2])
result[3]= float('%0.6f'%result[3])
result[4]= float('%0.6f'%result[4])
result[5]= float('%0.6f'%result[5])
result[6]= float('%0.6f'%result[6])
#for x in 1:len(result):

np.savetxt('result.txt', result, delimiter=' ')
print 'Success!'

