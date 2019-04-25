#include <fstream>
#include <iostream>
using namespace std;

int main () 
{
	ofstream Writfile;
	Writfile.open("banum.num") ;
	float a = 7.654874;
	float b = 12.6547 ;
	cout << a<< endl << endl ;
	Writfile.write((char*) &a,sizeof(float)) ;/* <<(char*) &b ; */
	Writfile.write((char*) &b,sizeof(float)) ;
	Writfile.close() ;
	
	char v[1];
	cin.getline(v, 1) ;
	
	ifstream Readfile ;
	Readfile.open("banum.num") ;
	float c ;
	float d ;
	Readfile.read((char*) &c, sizeof(float)); /* >> (char*) &d; */
	Readfile.read((char*) &d, sizeof(float));
	cout << c <<endl << c - a << endl<< d ;
	Readfile.close() ;
	
	return 0 ;
}