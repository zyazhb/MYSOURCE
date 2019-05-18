#include <stdio.h>
#include <stdlib.h>
struct stu
{
    int xh;
    char name[21];
    double w;
}p[150],tmp;
int main()
{
    int n,i,j;
    for(;scanf("%d",&n)!=EOF;)
    {
        for(i=0;i<n;i++)
        {
            scanf("%d%s%lf",&p[i].xh,p[i].name,&p[i].w);
        }
        for(i=0;i<n;i++)
        {
            for(j=i+1;j<n;j++)
            {
                if(p[i].w<p[j].w)
                {
                    tmp=p[i];
                    p[i]=p[j];
                    p[j]=tmp;
                }
            }
        }
        for(i=0;i<=2;i++)
        {
            printf("%d %s\n",p[i].xh,p[i].name);
        }
    }
    return 0;
}
