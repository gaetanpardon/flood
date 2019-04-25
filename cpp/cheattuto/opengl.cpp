

#include "GL/gl.h"
#include "GL/glu.h"


bool initialize()
{
	glEnable(GL_DEPTH_TEST);
	resize(WINDOW_WIDTH,WINDOW_HEIGHT) ;
	return true ;
}

void resize(int w,int h )
{
	if(h<=0)
	{h=1 ;}
	glViewport(0,0,(GLsizei)w ,(Glsizei)h) ;
	glMatrixMode(GL_PROJECTION);
	glLoadfIdentity();
	gluPerspective(60.0f,float(w)/float(h),1.0f,1000.0f);
	
	glMatrixMode(GL_MODELVIEW);
	glLoadfIdentity() ;
	
}

int main ()
{

	initialize() ;
	
	
}