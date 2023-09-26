#Never use import * since there is a name clash with Exception class in python
from mpi4py import MPI

comm = MPI.COMM_WORLD #Returns an object containing all the information passed to the processor while running the script. 
size = comm.Get_size() #Gives the total number of processors being used
rank = comm.Get_rank() #The unique processor id of each processor

print("Processor {} says Hello World".format(rank))