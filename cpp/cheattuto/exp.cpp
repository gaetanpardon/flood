#include <stdio.h>
#include <cuda_runtime.h> 
# include <fstream>
// Cuda supports printf in kernels for 
// hardware with compute compatibility >= 2.0

__global__ void helloworld(){  
// CUDA runtime uses device overloading  
// for printf in kernels  
printf("Hello world!\n");
}

int main(void)
{  
	helloworld<<<1,1>>>();
	cudaDeviceSynchronize();
	return 0 ;

}