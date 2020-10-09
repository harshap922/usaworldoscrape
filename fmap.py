f=open("buf.txt","r")
f2=open("toast.ps1","w")
lines=f.readlines()
print("New-BurntToastNotification -Text \"USA Total\", \'{}\' ".format(lines[2].strip()))
f2.write("New-BurntToastNotification -Text \"USA Total\", \'{}\' ".format(lines[2].strip()))

f.close()
f2.close()