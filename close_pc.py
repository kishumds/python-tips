import os

# Shutdown PC within 30 seconds
os.system(("shutdown /s"))

#Shutdown PC in given time (here immediately because time is 0 second)
os.system("shutdown /s /t 0")

#Restart PC within 30 seconds
os.system("shutdown /r")

#Restart PC in given time (here immediately because time is 0 second)
os.system("shutdown /r /t 0")