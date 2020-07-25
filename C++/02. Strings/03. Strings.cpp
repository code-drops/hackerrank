'''
You are given two strings,a  and b, separated by a new line. Each string will consist of lower case Latin characters ('a'-'z').
In the first line print two space-separated integers, representing the length of a and b respectively.
In the second line print the string produced by concatenating a and b.
In the third line print two strings separated by a space,a'  and b' . a' and b' are the same as a and b, respectively, except that their first characters are swapped.
'''

#include <iostream>
#include <string>
using namespace std;

int main() {
	// Complete the program
    string a,b;
    cin >> a;
    cin >> b;
    cout << a.length() << " " << b.length() << endl;
    cout << a+b << endl;
    string a1,a2;
    a1 = b[0];
    for(int i=1;i<a.length();i++)
        a1 = a1 + a[i];
    a2 = a[0];
    for(int i=1;i<b.length();i++)
        a2 = a2 + b[i];
    cout << a1 <<" "<<a2;
    return 0;
}
