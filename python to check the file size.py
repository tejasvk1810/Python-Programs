# to check file size
#in this ex,you will learn to check the file size
#using the os module
#the o/p size you will get be in Byte:

import os
sharad=os.stat('python to add two matrices.py')
print(sharad.st_size)

#using the pathlib module
from pathlib import Path
sharad=os.stat('python to add two matrices.py')
print(sharad.st_size)

#
from pathlib import Path
sharad=Path('python to add two matrices.py')
print(sharad.stat().st_size)

 