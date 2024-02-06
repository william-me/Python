import os
if os.path.exists("demofile.txt"):
    os.remove("demofile.txt")
else:
    print("The file doesnt exists")