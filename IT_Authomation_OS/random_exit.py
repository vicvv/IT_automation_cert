# run it with retry.sh

#!/Users/vicky/anaconda3/envs/py39/bin/python
import sys
import random

val = random.randint(0,3)
print("Returning: " + str(val))
sys.exit(val)
