#include<bits/stdc++.h>
#include<string.h>
#include <windows.h>
#include<fstream>
using namespace std;
class morsecode
{
private:
	char string[1000];
	int l;
	char c;
public:
	void getstring()
	{
		cout << "Enter the string to parse: ";
    	gets(string);
	}
	void aplhanum()
	{
		l=strlen(string);
    	ofstream out("output.txt");
    	ifstream in;
    	for(int i=0; i<l; i++)
    	{
        	switch(string[i])
        	{
            	case 'a' :
            	case 'A' :
                	{
                    	out << ".- ";
                    	break;
                	}
            	case 'b' :
            	case 'B' :
                	{
                    	out << "-... ";
                    	break;
                	}
            	case 'c' :
            	case 'C' :
                	{
                    	out << "-.-. ";
                    	break;
                	}
            	case 'd' :
            	case 'D' :
                	{
                    	out << "-.. ";
                    	break;
                	}
            	case 'e' :
            	case 'E' :
                	{
                    	out << ". ";
                    	break;
                	}
            	case 'f' :
            	case 'F' :
                	{
                    	out << "..-. ";
                    	break;
                	}
            	case 'g' :
            	case 'G' :
                	{
                    	out << "--. ";
                    	break;
                	}
            	case 'h' :
            	case 'H' :
                	{
                    	out << ".... ";
                    	break;
                	}
            	case 'i' :
            	case 'I' :
                	{
                   		out << ".. ";
                    	break;
                	}
            	case 'j' :
            	case 'J' :
                	{
                    	out << ".--- ";
                    	break;
                	}
            	case 'k' :
            	case 'K' :
                	{
                    	out << "-.- ";
                    	break;
                	}
            	case 'l' :
            	case 'L' :
                	{
                    	out << ".-.. ";
                    	break;
                	}
            	case 'm' :
            	case 'M' :
                	{
                    	out << "-- ";
                    	break;
                	}
            	case 'n' :
            	case 'N' :
                	{
                    	out << "-. ";
                    	break;
                	}
            	case 'o' :
            	case 'O' :
                	{
                    	out << "--- ";
                    	break;
                	}
            	case 'p' :
            	case 'P' :
                	{
                    	out << ".--. ";
                    break;
                	}
            	case 'q' :
            	case 'Q' :
                	{
                    	out << "--.- ";
                    	break;
                	}
            	case 'r' :
            	case 'R' :
                	{
                    	out << ".-. ";
                    	break;
                	}
            	case 's' :
            	case 'S' :
                	{
                    	out << "... ";
                    	break;
                	}
            	case 't' :
            	case 'T' :
                	{
                    	out << "- ";
                    	break;
                	}
            	case 'u' :
            	case 'U' :
                	{
                    	out << "..- ";
                    	break;
                	}
            	case 'v' :
            	case 'V' :
                	{
                    	out << "...- ";
                    	break;
                	}
            	case 'w' :
            	case 'W' :
                	{
                    	out << ".-- ";
                    	break;
                	}
            	case 'x' :
            	case 'X' :
                	{
                    	out << "-..- ";
                    	break;
                	}
            	case 'y' :
            	case 'Y' :
                	{
                    	out << "-.-- ";
                    	break;
                	}
            	case 'z' :
            	case 'Z' :
                	{
                    	out << "--.. ";
                    	break;
                	}
            	case ' ' :
                	{
                    	out << " /  ";
                    	break;
                	}
            	case '0' :
                	{
                    	out << "----- ";
                    	break;
                	}
            	case '1' :
                	{
                    	out << ".---- ";
                    	break;
                	}
            	case '2' :
                	{
                    	out << "..--- ";
                    	break;
                	}
            	case '3' :
                	{
                    	out << "...-- ";
                    	break;
                	}
            	case '4' :
                	{
                    	out << "....- ";
                    	break;
                	}
            	case '5' :
                	{
                    	out << "..... ";
                    	break;
                	}
            	case '6' :
                	{
                    	out << "-.... ";
                    	break;
                	}
            	case '7' :
                	{
                    	out << "--... ";
                    	break;
                	}
            	case '8' :
                	{
                    	out << "---.. ";
                    	break;
                	}
            	case '9' :
                	{
                	    out << "----. ";
                    	break;
                	}
			}
		}
	}
	void characters()
	{
		ofstream out;
		out.close();
        ifstream in;
		in.open("output.txt");
        while(!in.eof())
        {
            in>>c;
            if(c =='.')
            {
                Beep(523,200);
            }
            else if(c =='-')
            {
                Beep(523,700);
            }
            else if(c ==' ')
            {
                Beep(0,100);
            }
            else if(c == '/')
            {
                Beep(0,400);
            }
        }
        in.close();
	}
};
main()
{
	morsecode t;
	t.getstring();
	cout<<"The respective Morse Code..";
	t.aplhanum();
	t.characters();
}
