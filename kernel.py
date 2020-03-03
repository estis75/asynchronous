import math as ms
import random
import string 
import os
import time

print(os.getcwd())
try: # initialize file to manage flags
  os.mkdir("state")
except FileExistsError:
  os.chdir("state")
  for i in os.listdir():
    os.remove(i)
  os.chdir("..")

try: # initialize file to save data
  os.mkdir("data")
except FileExistsError:
  os.chdir("data")
  for i in os.listdir():
    os.remove(i)
  os.chdir("..")

data=[]

while (not (os.path.exists("state/mkdata_finished") and len(data)==0)) :
  # check the state of processing unit
  if(os.path.exists("state/busy") or len(data)==0):
    print("kernel: busy or no data")
  else:
    print("kernel: start a new job")
    f = open("state/file.path", 'w')
    f.write(data[0])
    data.pop()
    f.close()
    while(os.path.exists("state/busy")):
      time.sleep(1)

  # check the exsistance of a new data path
  if(not os.path.exists("state/file.catch")):
    print("kernel: no data")
  else:
    f = open("state/file.catch", 'r')
    data.append(f.read())
    f.close()

    print("kernel: ", data)

    os.remove("state/file.catch")
  time.sleep(0.5)

f = open("state/kernel_finished", 'w')
f.close
print("kernel: finished")