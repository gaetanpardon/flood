#include <fstream>
#include <iostream>
#include "toolbox.h"


int main(){
	char name[20];
	std::cout<<"[chois pseudo]" ;
	std::cin.getline(name,19) ;
	std::cout<<"debug1"<<name;
	vider_buffer() ;
	std::cout<<"debug2";
	std::cin.read(name,20) ;
	
	
	
	
	
	
	return 0 ;
}