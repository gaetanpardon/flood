#include <fstream>
#include <iostream>
#include <limits>



void vider_buffer()
{
    std::cin.clear();
    std::cin.seekg(0, std::ios::end);

    if(!std::cin.fail())
    {
        std::cin.ignore(std::numeric_limits<std::streamsize>::max());
    }

    else
    {
        std::cin.clear(); // Le flux est dasn un état invalide donc on le remet en état valide
    }
}

/* int main (){
	return 0 ;
} */