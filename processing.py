import os, time

while(not os.path.isdir("data")):
  print("processing: data not found")
while(not os.path.isdir("state")):
  print("processing: state not found")

while (not os.path.exists("state/kernel_finished")):
  if(not os.path.exists("state/file.path")):
    print("processing: no data")
  else:
    print("processing: start a new job")
    f = open("state/busy", 'w')
    f.close()
    f = open("state/file.path", 'r')
    path = f.read()
    f.close()
    os.remove("state/file.path")
    # processing
    print("processing: processing")
    f2 = open("data/pathes", 'a')
    f2.write(path + "\n")
    f2.close()
    os.remove("state/busy")
  time.sleep(1)
else:
  if(not os.path.exists("state/file.path")):
    print("processing: no data")
  else:
    print("processing: start a new job")
    f = open("state/busy", 'w')
    f.close()
    f = open("state/file.path", 'r')
    path = f.read()
    f.close()
    os.remove("state/file.path")
    # processing
    print("processing: processing")
    f2 = open("data/pathes", 'a')
    f2.write(path + "\n")
    f2.close()
    os.remove("state/busy")

f = open("state/processing_finished", 'w')
f.close
print("processing: finished")