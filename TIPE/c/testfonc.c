/*#include <iostream>*/
#include <stdio.h>
#include <stdlib.h>
#include <math.h>
/*comante */

const float pi =3.141592654 ;

int fft(float* V ,int lV ,float*R,int *lR ) ;

int main() {
	float a = 0 ;
	int i = 0 ;
	printf("%f\n",a);
	a=cos(0) ;
	printf("%f\n",a);
	FILE* f = NULL ;
	char liste[200]="";
	f = fopen("..\\MCC.csv","r");
	if (f != NULL )
	{
		for (i=0 ;i<20 ; i++)
		{
			fgets(liste,100,f);
			printf("%s ",liste) ;
		}
		fgets(liste,100,f);
		printf("%s",liste) ;
		fclose(f);
	}
	else
	{
		printf("erreur");
	}
	return 0 ;
	
}

int fft(float* V ,int lV ,float*R,int *lR ) {
	*lR=lV/2+1;
	int i = 0 ;
	int ar = 1 ;
	float an = 0 ;
	float bn = 0 ;
	float pa = 0 ;
	if ((R!=NULL ) || (V==NULL )|| (lR=NULL ) || (lV<1 ))
	{
		return(-1) ;
	}
	R = malloc((*lR )*sizeof(float)) ;
	for (ar=1 ;ar<*lR ; ar++)
	{
		an=0;
		bn=0;
		pa = (ar*(pi*2))/lV ;
		for (i=0 ;i<lV;i++)
		{
			an+= *(V+i) * cos(pa*i);
			bn+= *(V+i) * sin(pa*i);
		}
	}
	
	
	
	return (0);
}

int harl (float *L ,int lL,float*R,int *lR)
{
	if ((R!=NULL ) || (L==NULL )|| (lR=NULL ) || (lL<5 ))
	{
		return(-1) ;
	}
	
	
	*lR = 0 ;
	int ar= 0 ;
	int i = 3 ;
	for (i=3 ; i <lL ; i++ )
	{	
		if ( (*(L+i)>*(L+i-1)) && (*(L+i)>*(L+i-2)) && (*(L+i)>*(L+i-3)) )
		{
			if ((ar+5)<i)
			{
				(*lR)++ ;
			}
			if (*(L+i)> *(L+ar))
			{
				ar=i ; 
			}
		}
	}
	
	
	ar= 0 ;
	i = 3 ;
	int j = 0 ;
	R = malloc((*lR )*sizeof(int)) ;
	for (i=3 ; i <lL ; i++ )
	{	
		if ( (*(L+i)>*(L+i-1)) && (*(L+i)>*(L+i-2)) && (*(L+i)>*(L+i-3)) )
		{
			if ((ar+5)<i)
			{
				*(R+j) = i ;
				j++ ;
			}
			if (*(L+i)> *(L+ar))
			{
				ar=i ;
			}
		}
	}
	return(0) ;
	
}
