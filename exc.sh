#!/bin/bash

for i in `ls state`;do
  rm state/$i
done

python3 mkdata.py &
python3 kernel.py &
python3 processing.py &
