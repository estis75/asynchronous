import os, time

for i in range(10): # make 10 files 
  addr="data/" + str(i)

  print("mkdata: datus is made")
  f = open("state/file.catch", 'w')
  f.write(addr)
  f.close()

  # check the exsistance of file while kernel find the data
  while(os.path.exists("state/file.catch")):
    print("yet")
    time.sleep(0.3)

f = open("state/mkdata_finished", 'w')
f.close

print("mkdata: finished")