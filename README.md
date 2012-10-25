== Description ==
For this project I implemented the find_max algorithm for use on clusters. 
The program creates a random array of n numbers, distributes the array across all the nodes of the cluster and then finds the max.
The program also calculates the processing time, communication time and overall time to find the max. It outputs the results in either a human readable form, or in a tab separated output.
 
 == Source code ==
 You can download the source code of the application here:
 https://github.com/mvictoras/MPImaxFinder
 <syntaxhighlight lang="bash">
 git clone https://github.com/mvictoras/MPImaxFinder
 </syntaxhighlight>

 == Installation ==
 I have included a Makefile to compile the project.
 <syntaxhighlight lang="bash">make</syntaxhighlight>

 == Running ==
 The project was run on [http://accc.uic.edu/service/argo-cluster ARGO], that is a [http://www.uic.edu/ University of Illinois at Chicago] cluster available for students and staff.
 If you are on ARGO (or any cluster that processes are submitted using [http://www.adaptivecomputing.com/products/open-source/torque/ TORQUE]), you need to run:
 <syntaxhighlight lang="bash">
 ./submit.sh 
 -n <# of numbers> 
 -p <# of physical processors> 
 -k <# of logical processors per node> 
 -t <topology: ring, 2dmesh, hypercube, tree> 
 -a <find_max algorithm: ring_shift, gather, reduction>
 </syntaxhighlight>

 If your cluster allows you to run directly programs (without process queues, then you run:
 <syntaxhighlight lang="bash">
 mpirun -np <num_of_nodes> unified 
 -n <# of numbers> 
 -p <# of physical processors> 
 -k <# of logical processors> 
 -t <topology: ring, 2dmesh, hypercube, tree> 
 -a <find_max algorithm: ring_shift, gather, reduction> 
 [-c]
 </syntaxhighlight>
 All the arguments are mandatory. The -c option is optional. By default the program prints the results into a human readable format, -c outputs in a tab separated format, so that the data can be easily read and processed by other processes.
