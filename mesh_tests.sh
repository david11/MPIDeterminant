#!/bin/bash

# n = 2520
./submit.sh -n 2520 -p 1 -k 1 -t mesh
./submit.sh -n 2520 -p 4 -k 1 -t mesh

# n = 5040
./submit.sh -n 5040 -p 1 -k 1 -t mesh
./submit.sh -n 5040 -p 4 -k 1 -t mesh

# n = 10080
./submit.sh -n 10080 -p 1 -k 1 -t mesh
./submit.sh -n 10080 -p 4 -k 1 -t mesh

# n = 5040
./submit.sh -n 5040 -p 3 -k 3 -t mesh
./submit.sh -n 5040 -p 4 -k 4 -t mesh

# n = 10080
./submit.sh -n 10080 -p 3 -k 3 -t mesh
./submit.sh -n 10080 -p 4 -k 4 -t mesh
