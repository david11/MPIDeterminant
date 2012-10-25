CC=mpicc

all: determinant

determinant: determinant.c
			$(CC) -lm -o determinant determinant.c

clean:
	    rm -rf determinant
