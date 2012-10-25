#!/bin/bash

if ( ! getopts ":n:p:t:k:" opt); then
  echo "Usage: `basename $0` -n <number of numbers> -p <number of physical processors> -t <ring, mesh> -k <processors per node>"
  exit 1
fi
while getopts ":n:p:t:k:" opt; do
    case $opt in
    n)
      n=$OPTARG
      ;;
    p)
      p=$OPTARG
      ;;
    t)
      t=$OPTARG
      ;;
    k)
      k=$OPTARG
      ;;
    \?)
      echo "Invalid option: -$OPTARG" >&2
      exit 1
      ;;
    :)
      echo "Option -$OPTARG requires an argument." >&2
      exit 1
      ;;
  esac
done

echo "Creating $n random numbers and using $p physical processorswith $k processors per node"
qsub -V -l nodes=$p:ppn=$k -q student_long -v n=$n,p=$p,t=$t,k=$k process.sh 
