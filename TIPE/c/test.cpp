/*#include <iostream>*/
#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include <new.h>
/*comante */
const float pi =3.141592654 ;

int fft(float* V ,int lV ,float*R,int *lR ) ;


int main() {
	float a = 0 ;
	int i = 0 ;
	printf("%f\n",a);
	a=cos(0) ;
	printf("%f\n",a);
	int t = 25 ;
	t=t/2 ;
	printf("%d",t) ;
	FILE* f = NULL ;
	char liste[200]="";
	int cara = 0 ;
	f = fopen("..\\MCC.csv","r");
	if (f != NULL )
	{
		fgets(liste,100,f);
		printf("%s",liste) ;
		float mod =0 ;
		float tension = 0;
		float temf = 0 ;
		cara = fgetc(f);
		int signe = 0 ;
		while ( cara!= EOF )
		{
			
			/*printf("%c",cara) ;*/
			mod = 0 ;
			tension = 0 ;
			signe = 0 ;
			if (cara == 45 )
			{
				signe = 1 ;
				cara=fgetc(f);
				
			}
			while ((cara!=10) && (cara!=EOF)) 
			{
				
				if (mod == 0) 
				{
					/*printf("%c",cara) ;*/
					if (cara == 46)
					{
						mod = 1 ;
					}
					else 
					{
						tension = ( tension * 10 ) + (cara - 48 );
						/*printf("%c",cara) ;*/
						/*printf("a  %f \n ",tension) ;*/
					}
				}
				else 
				{
					mod = mod * 10 ;
					temf = cara-48 ;
					tension += (temf)/(mod) ;
					/*printf("b %f \n ",tension) ;
					printf("c %d  %f \n",cara,mod ) ;*/
				}
				cara = fgetc(f);
			}
			if (signe == 1 )
			{
				tension = -tension ;
			}
			printf("%f \n",tension) ;
			cara = fgetc(f);
		}
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
	float cn = 0 ;
	float pa = 0 ;
	if ((R!=NULL ) || (V==NULL )|| (lR=NULL ) || (lV<1 ))
	{
		return(-1) ;
	}
	R = new float [*lR];
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
		cn= sqrt(an*an + bn*bn ) ;
		
	}
	
	
	
	return (0);
}

int fft(float V[200] ,float R [100] ) {
	int i = 0 ;
	int ar = 1 ;
	float an = 0 ;
	float bn = 0 ;
	float cn = 0 ;
	float pa = 0 ;
	for (ar=1 ;ar<201 ; ar++)
	{
		an=0;
		bn=0;
		pa = (ar*(pi*2))/101 ;
		for (i=0 ;i<101;i++)
		{
			an+= *(V+i) * cos(pa*i);
			bn+= *(V+i) * sin(pa*i);
		}
		cn= sqrt(an*an + bn*bn );
		R[ar-1]=cn;
	}
	
	
	
	return (0);
}

int harl (float *L ,int lL,int*R,int *lR)
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
	R = new int [*lR] ;
	if (R==NULL)
		{
			return(-2) ;
		}
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


int readf(const char* nom ,float * R ,int *lR) 
{
	FILE* f = NULL ;
	char liste[200]="";
	f = fopen(nom,"r");
	if (f != NULL )
	{
		fgets(liste,100,f);
		printf("%s",liste) ;
		int i =0 ;
		int cara = 0 ;
		for (i=0 ;i<20 ; i++)
		{
			cara = fgetc(f);
			printf("%c",cara) ;
		}
		fclose(f);
	}
	else
	{
		printf("erreur");
	}
	return(0) ;
}

int rendwav(const char* nom ,char * R ,int *lR)
{
	
	FILE* f = NULL ;
	f = fopen(nom,"rb");
	if (f != NULL )
	{
		int i =0 ;
		int vb[44] ;
		for (i=0 ;i<44 ; i++)
		{
			fread(vb,1,44,f);
			
		}
		fclose(f);
	}
	else
	{
		printf("erreur");
	}
	return(0) ;
}

/*delete [] R */
