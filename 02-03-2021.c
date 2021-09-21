#include<stdio.h>
#include<stdlib.h>
int main() 
{

int n,ans=21,i=0;
scanf("%d",&n);
for(i=1;i<=n;i++)
{
    printf("%d ",ans);
    ans=(ans*2)-(7*i);
}
}

int i=0,n,a=4;
scanf("%d",&n);
for(i=0;i<n;i++)
{
    printf("%d ",a);
    if(i%2==0)
    {a=(a*2)+3;}
    else
    {a=(a*2)-3;}
}
int n,ans=7,i;
scanf("%d",&n);
for(i=2;i<=n;i++)
{
    printf("%d ",ans);
    ans=ans+(i*(i+1));
}


}