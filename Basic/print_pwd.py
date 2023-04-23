import os
pwd = os.popen("pwd").read()
contain = os.popen(f"ls {pwd}").read().split()
print(f"{pwd} : {contain}")
