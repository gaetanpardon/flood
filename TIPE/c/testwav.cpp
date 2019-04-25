#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include <new.h>
/*comante */
const float pi =3.141592654 ;

int main() 
{
	FILE* f = NULL ;
	f = fopen("..\\soll.wav","r");
	if (f != NULL )
	{
		int i =0 ;
		int j = 0 ;
		int oct = 0 ;
		int octb = 0 ;/*oct bloc*/
		int octc = 0 ;/*N caneau*/
		int octd = 0 ;/*oct data*/
		int test = 0 ;
		unsigned char vb[44] ;
		unsigned char vbf[4] ;
		float vf =0 ;
		fread(vb,1,44,f);
		test=printf("%c %c %c %c \n",vb[0] ,vb[1] ,vb[2],vb[3]) ;
		/*printf("%d %d %d %d",vb[4] ,vb[5] ,vb[6],vb[7]) ;*/
		oct = vb[4] +256* (vb[5] + 256*(vb[6] + 256*vb[7])) ;
		printf("%d  \n" , oct );
		printf("%c %c %c %c \n",vb[8] ,vb[9] ,vb[10],vb[11]) ;
		printf("%c %c %c %c \n",vb[12] ,vb[13] ,vb[14],vb[15]) ;
		oct = vb[16] +256* (vb[17] + 256*(vb[18] + 256*vb[19])) ;
		printf("%d  \n" , oct );
		oct = vb[20] + 256*vb[21]; 
		printf("%d  \n" , oct );
		octc = vb[22] + 256*vb[23]; /*N caneau*/
		printf("c: %d  \n" , oct );
		oct = vb[24] +256* (vb[25] + 256*(vb[26] + 256*vb[27])) ;
		printf("%d  \n" , oct );
		oct = vb[28] +256* (vb[29] + 256*(vb[30] + 256*vb[31])) ;
		printf("%d  \n" , oct );
		octb = vb[32] +256* vb[33] ;/*oct bloc*/
		printf("b: %d  \n" , octb );
		/*oct = vb[32] +256* (vb[33] + 256*(vb[34] + 256*vb[35])) ;*/
		oct = vb[34] + 256*vb[35] ;/**/
		printf("%d  \n" , oct );
		printf("%c %c %c %c \n",vb[36] ,vb[37] ,vb[38],vb[39]) ;
		octd = vb[40] +256* (vb[41] + 256*(vb[42] + 256*vb[43])) ;
		printf("%d  \n" , octd );/*oct data*/
		
		printf("t : %d \n", test ) ;
		test=fread(vb,1,octb,f);
		printf("%d %d %d %d \n",vb[0] ,vb[1] ,vb[2] ,vb[3] ) ;
		printf("t : %d \n", test ) ;
		
		if (octb%octc==0)
		{
			
			for (i=0 ;i<(octd/octb) ; i++) /*(octd/octb)*/
			{
			
				test=fread(vb ,1,octb,f);
				/*printf("1  %d %d %d %d \n",vb[0] ,vb[1] , vb[2] ,vb[3]) ;
				/*vbf[0]=vb[3] ;
				vbf[1]=vb[2];
				vbf[2]=vb[1] ;
				vbf[3]=vb[0] ;
				vf = *reinterpret_cast<float*>(vbf);
				printf("%f \n",vf) ;*/
				/*
				if ((vb[0]!=73 ) || (vb[1]!=0)|| (vb[2]!=48)|| (vb[3]!=0)  )
				{
					printf("2  %d %d %d %d \n",vb[0] ,vb[1] ,vb[2] ,vb[3] ) ;
					printf("t : %c \n", test ) ;
				} */
				if ((test!=0)  )
				{
					printf("2  %d %d %d %d \n",vb[0] ,vb[1] ,vb[2] ,vb[3] ) ;
					printf("t : %d \n", test ) ;
				} 
			}
		/*printf("%c %c %c %c",vb[1] ,vb[2] ,vb[3],vb[4]) ;*/
		}
		fclose(f);
	}
	else
	{
		printf("erreur");
	}
	return(0) ;
} 
