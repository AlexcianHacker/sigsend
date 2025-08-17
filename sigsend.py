import os; import sys; 
def sigsend(pid: int, signum: int = 11) -> int: 
    try: os.kill(pid,signum); 
    except: print("Shit Went Wrong Bruv "); return -1; 
    return 0; 
if __name__=="__main__": 
    if len(sys.argv)> 2: sigsend(-1, sys.argv[2]); 
    else: sigsend(-1, 11); 