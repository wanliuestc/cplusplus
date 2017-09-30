#include <stdio.h>
#include <string.h>
#include <ctype.h>

#define MAXTOKEN 100

enum { NAME, PARENS, BRACKETS };

void dcl(void);
void dirdcl(void);

int gettoken(void);
int tokentype;
char token[MAXTOKEN];
char name[MAXTOKEN];


void dcl(void)
{
    int ns;
    for(ns = 0; gettoken() == '*';)
        ns++;
        dirdcl();
    while(ns-- > 0)
        strcat(out, " pointer to ");
}

void dirdcl(void)
{
    int type;
    if(tokentype =='(')
    {
        dcl();
        if(tokentype != ')')
            printf("error: missing )\n")
    }
    else if(tokentype == NAME)
        sttcpy(name, token);
    else
        printf("error: expected name or (dcl)\");
    while((type = gettoken()) ==  PARENS || type == BRACKETS)
        if(type == PARENS)
            strcat(out, " function returning");
        else
        {
            strcat(out, " array");
            strcat(out, token);
            strcat(out, " of");
        }
}
