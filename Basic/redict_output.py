from io import StringIO
import sys
 

tmp = sys.stdout
my_result = StringIO()
sys.stdout = my_result

help(abs)
sys.stdout = tmp
print(my_result.getvalue())