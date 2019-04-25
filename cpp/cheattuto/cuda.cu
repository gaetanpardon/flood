# include <cuda_runtime.h >
# include <cuda_runtime_api.h>
#include <fstream>
#include <iostream>
using namespace std;




__global__ void vecAdd(int * A, int * B, int * C)
{
    int i = threadIdx.x;
    C[i] = A[i] + B[i];
}

int main()
{
    // utilisation du kernel
	int N=19 ;
	int A[]= {1,2,3,4,5,6,7,8,8,0,1,2,3,4,5,6,7,8,8} ;
	int B[]= {1,2,3,4,5,6,7,8,8,0,1,2,3,4,5,6,7,8,8} ;
	int C[19] ;
	
    vecAdd<<<1, N>>>(A, B, C);
        //     |-> vecteurs additionnés une seule fois
        //        |-> nombre de composante des vecteurs
		
	cout(C[1]) ;
}