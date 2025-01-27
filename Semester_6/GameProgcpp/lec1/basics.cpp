#include<iostream>
using namespace std;

/*int gcd(int a,int b){
 if(b==0){
 
 return a;
}
 return gcd(b,a%b);
 
}
int lcm(int a,int b){
return (a*b)/gcd(a,b);
}
*/
struct str{
 int roll;
 char name[30];
 float cgpa;
};
int main(){
/*
int a,b;
std::cout<<"hello world\n";

cout<<"enter the number";
cin>>a;
cin>>b;
cout <<a<<" + "<<b<<" = "<<a+b<<endl;

char name[30];
cout<<"enter the name ";

//cint>>name;
cin.getline(name,30);
cout<<"Welcome " << name << "! "<<endl;
*/


struct str s[5];
for(int i=0;i<5;i++){
cout << "Enter roll std "<<i+1<<" : ";
cin >>s[i].roll;
cout <<"Enter  name std"<<i+1<<" : ";
cin.ignore();
cin.getline(s[i].name,30);
cout <<"Enter cgpa std "<<i+1<<" : ";
cin >>s[i].cgpa;
}
cout<< "details"<<endl;
for(int i=0;i<5;i++){
cout<<"roll"<<s[i].roll<<endl;
cout<<"name"<<s[i].name<<endl;
cout<<"cgpa"<<s[i].cgpa<<endl;

}


return(0);
}