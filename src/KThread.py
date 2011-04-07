#This code module allows you to kill threads. The
#class KThread is a drop-in replacement for
#threading.Thread. It adds the kill() method, which
#should stop most threads in their tracks.

#
#---------------------------------------------------------------------
# KThread.py: A killable Thread implementation.
#
#---------------------------------------------------------------------

import sys
import trace
import threading

class KThread(threading.Thread):
    """A subclass of threading.Thread, with a kill() method."""
    
    def __init__(self, *args, **keywords):
        threading.Thread.__init__(self, *args, **keywords)
        self.killed = False
        pass
    pass
    
    def start(self):
        """Start the thread."""
        self.__run_backup = self.run
        self.run = self.__run # Force the Thread to install our trace.
        threading.Thread.start(self)
        pass
    pass
    
    def __run(self):
        """Hacked run function, which installs the trace."""
        sys.settrace(self.globaltrace)
        self.__run_backup()
        self.run = self.__run_backup
        pass
    pass
    
    def globaltrace(self, frame, why, arg):
        if why == 'call':
            return self.localtrace
        else:
            return None
        pass
    pass
    
    def localtrace(self, frame, why, arg):
        if self.killed:
            if why == 'line':
                raise SystemExit()
            return self.localtrace
        pass
    pass
    
    def kill(self):
        self.killed = True
        pass
    pass