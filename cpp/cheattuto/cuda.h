# include cuda_runtime.h 
# include cuda_runtime_api.h




__global__ void vecAdd(float * A, float * B, float * C)
{
    int i = threadIdx.x;
    C[i] = A[i] + B[i];
}

int main()
{
    // utilisation du kernel
	int N=2 ;
	int A[]= [1,2] ;
	int B[]= [1,2] ;
	int C[2] ;
	
    vecAdd<<<1, N>>>(A, B, C);
        //     |-> vecteurs additionnés une seule fois
        //        |-> nombre de composante des vecteurs
