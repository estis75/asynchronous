import os, time

while(not os.path.isdir("data")):
  print("mkdata: data not found")
while(not os.path.isdir("state")):
  print("mkdata: state not found")

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