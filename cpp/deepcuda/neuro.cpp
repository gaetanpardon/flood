

struct Sneuro{
	unsigned int ne;// nombre d entre
	float* Lp ; // liste des paramettre du nerone bias en fin
	float ** Le ; //liste de pointeur vers des sorti de neurone : les entre 
	float etself ; // detection de potentiel duplissité du neurone 
	float* Lete ; // valeur jouant un role dans la detection d'entree inutile 
	unsigned int ns ; // valeur du neuro if <1 destroy
	float* s; //sorti
	
} ;

struct Scouche {
	unsigned int ns ;
	Sneuro * Ls;
};
struct Stopo {
	unsigned int nc ;
	Scouche * Lc;
};



void Fneurosol(float* Lc , float** Lv , int e; float* is){
	
	float s=*(Lc[e]) ;
	for(i=0 ;i<e ;i++ ) {
		s+=*(Lc[i]) * (**(Lv[i])) ;
	}
	*is =s
	
}

void Ftoposol (Stopo topos){
	
	
	unsigned int nc= topos.nc ;
	unsigned int ns ;
	Scouche * pcouche
	for(ii=0 ; ii<nc ; ii++ ){
		pcouche = topos.Lc[ii]
		ns = pcouche*.ns 
		for (iii=0 ; iii<ns ; iii++ ) {
			
			
		}
	}
		
	
	
}