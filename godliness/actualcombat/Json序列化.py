import psutil
import os

for pid in psutil.pids():
    try:
        proc = psutil.Process(pid)
        exeFile = os.path.basename(proc.exe())
        threads = psutil._psutil_windows.proc_threads(pid)
        times = 0
        for thread in threads:
            for timeUsed in thread[1:]:
                times += timeUsed
        print('='*40)
        print('Exe file:', os.path.basename(proc.exe()))
        print('Number of threads:', len(threads))
        print('Time used:', times)
    except:
        pass

