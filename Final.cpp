#include <iostream>
#include <fstream>
using namespace std;



void solve_equation_leapfrog(float t_init, float t_end, float delta_t, string filename);

int main(){  

 
  solve_equation_leapfrog(0.0, 10.0, 0.1, "datos.dat");
 
  return 0;
}


void solve_equation_leapfrog(float t_init, float t_end, float delta_t, string filename){
    
  float t=t_init;
  float y=0;
  float z=0;
  float x=1;
  float m= 7294.29;
 
  float q = 2.0;
  float f = 0.3*q;
    
  ofstream outfile;
  outfile.open(filename);
  
    while(t<t_end){
      
    outfile << t << " " << x <<" " << y << endl;
  
        
    z = z + delta_t*y*f*0.5;    
    y = y + delta_t*z;
    z = z + y*f*delta_t*0.5;
       
    t = t + delta_t;
    
        
  
  }
  outfile.close();
 
    
}