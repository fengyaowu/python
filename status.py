
import os
import subprocess

def test1():
   
    fnull = open(os.devnull, 'w')
    return1 = subprocess.call('ping baidu.com -c 4', shell = True, stdout = fnull, stderr = fnull)
    if return1:
        execfile('/etc/init.d/connect.py')
    else:
        print 'ping ok'
    fnull.close()
 
if __name__=='__main__':
    test1()
