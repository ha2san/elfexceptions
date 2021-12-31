#include <iostream>
using namespace std;

int main (int argc, char** argv) {
  try
  {
    if(argc > 1) throw 20;
  }
  catch (int e)
  {
    cout << "An exception occurred. Exception Nr. " << e << '\n';
  }
  cout << "End of the program\n";
  return 0;
}
