#include <iostream>
#include <vector>

using namespace std;

class A
{
private:
	int _a;
public:
	A(int a):_a(a){}

	int getA()
	{
		return this->_a;
	}

	void setA(int a)
	{
		this->_a = a;
	}

	~A()
	{
		cout << "deconstruct invoked " << this->_a << endl;
	}
};

int main(void)
{
	vector< A* > as, bs, deletedAs, addedAs;
	as.push_back(new A(1));
	as.push_back(new A(3));
	as.push_back(new A(5));
	as.push_back(new A(6));
	as.push_back(new A(7));

	bs.push_back(new A(1));
	bs.push_back(new A(2));
	bs.push_back(new A(4));
	bs.push_back(new A(6));
	bs.push_back(new A(7));
	
	vector< A* >::iterator ite, ite2, p;

	for(ite = as.begin(); ite != as.end(); ite++)
	{
		for(ite2 = bs.begin(); ite2 != bs.end(); ite2++)
		{
			if((*ite)->getA() == (*ite2)->getA())
				break;
			else
			{
				deletedAs.push_back(*ite);
			}
		}
	}	


	for(ite = bs.begin(); ite != bs.end(); ite++)
	{
		for(ite2 = as.begin(); ite2 != as.end(); ite2++)
		{
			if((*ite)->getA() == (*ite2)->getA())
			{
				delete *ite;
				*ite = 0;
			}
			else
			{
				addedAs.push_back(*ite);
			}
		}
	}	

	for(ite = as.begin(); ite != as.end(); ite++)
	{
		for(ite2 = deletedAs.begin(); ite2 != deletedAs.end(); ite2++)
		{
			if((*ite)->getA() == (*ite2)->getA())
			{
				delete *ite;
				*ite = 0;
				break;
			}
		}
	}
	p = as.begin();
	for(ite2 = as.begin(); ite2 != as.end();ite2++)
	{
		if(*ite2 != 0)
		{
			*p = *ite2;
			p++;	
		}
	}

	for(ite = addedAs.begin(); ite != addedAs.end(); ite++)
	{
		as.insert(++p, *ite);
	}

	as.erase(p, as.end());

	cout << "result :" << endl;

	for(ite = as.begin(); ite != as.end(); ite++)
	{
		cout << (*ite)->getA() << endl;
	}
	return 0;
}
