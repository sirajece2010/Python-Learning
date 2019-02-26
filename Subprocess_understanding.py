import subprocess


#subprocess.call('ls -l | grep calc', shell=True)

#print(my)
my2 = subprocess.Popen(['ls -l', 'grep', 'calc'], stdout=subprocess.PIPE, shell=True)
print(my2.communicate()[0])