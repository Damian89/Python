# a script to get the current local time

import time

localtime = time.asctime( time.localtime(time.time()) )
print("Local current time :", localtime)