#!/usr/bin/env python
from mpi4py import MPI
from mpiclass import MPIClass
import tarfile
import os, sys
from stat import *
import shutil
from write_rand_data import *
from collections import deque



################################################################################
class Workthief(MPIClass):

    #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    def __init__(self):

        MPIClass.__init__(self,initdirs=False)

        self.instruct = None;
        self.queue = deque()
        self.dirs = []
        self.files = []

        if self.i_am_root:
            self.recurse("testtree", maxdepth=1)
            sep="-"*80
            print("{}\ndir queue, {} items=\n{}".format(sep, len(self.queue), self.queue))
            print("{}\ndirs found {} items=\n{}".format(sep, len(self.dirs),  self.dirs))
            print("{}\nfiles found {} items=\n{}".format(sep,len(self.files), self.files))
        return



    #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    def recurse(self, top, maxdepth=sys.maxint, depth=0):

        for f in os.listdir(top):
            pathname = os.path.join(top, f)
            statinfo = os.stat(pathname)
            if S_ISDIR(statinfo.st_mode):
                if (depth < maxdepth):
                    self.dirs.append(pathname)
                    self.recurse(pathname, maxdepth, depth=depth+1)
                else:
                    self.queue.append(pathname)
            else:
                #print(statinfo)
                self.files.append(pathname)
        return



    #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    def run_serial_task(self):
        return



    #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    def run(self):
        return




################################################################################
if __name__ == "__main__":
    wt = Workthief()
    wt.run()