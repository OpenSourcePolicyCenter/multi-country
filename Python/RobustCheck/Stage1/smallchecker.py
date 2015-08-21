#import numpy as np
import Main as mn
import sys
import time
from mpi4py import MPI
from mpi4py.MPI import ANY_SOURCE

comm=MPI.COMM_WORLD
rank=comm.Get_rank()

if rank==0:
    start=time.time()
    mn.TheWholeSmack(80,10,6)
    timer=time.time()-start

    print "This process took", timer, "seconds"
