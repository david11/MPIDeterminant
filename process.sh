#!/bin/bash

#PBS -m be
#PBS -e ${t}.${n}n.${p}.${k}.error
#PBS -o ${t}.${n}n.${p}.${k}.output
#PBS -N determinant

num_nodes=$[$p*$k]
mpiexec -np $num_nodes ${HOME}/proj2/determinant -n $n -t $t -c
