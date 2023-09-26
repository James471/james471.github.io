from mpi4py import MPI

comm = MPI.COMM_WORLD #Returns an object containing all the information passed to the processor while running the script. 
size = comm.Get_size() #Gives the total number of processors being used
rank = comm.Get_rank() #The unique processor id of each processor

if rank!=0:
    # Each processor except processor 0 sends it's rank to processor 0. 
    # You can send any object you want by passing it as data parameter. 
    # The tag is meant to identify the data.
    comm.send(rank, 0, tag=0)   
    print("Sent {} to processor {}".format(rank,0))
else:
    sum = rank
    for i in range(1, size):
        # Processor 0 receives the data with tag=0 from each processor. 
        # Source is the processor rank of the processor sending the data.
        num = comm.recv(source = i, tag=0)  
        print("{} received from processor {}".format(num,i))
        sum += num
    print(sum)