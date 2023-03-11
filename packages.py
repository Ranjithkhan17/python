#write a script to get disk usage

import os
import shutil
print(os.getcwd())
total, usage, free =(shutil.disk_usage("/"))
print(f"Total space is",total // (2**30),"GB")
print("Total usage space is",usage // 2**30) 
print("Free space",free // 2**30)