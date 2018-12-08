#include<string.h>
char* longestPalindrome(char* s) {
    int len = strlen(s);
    int n = 2*len-1;
    int i;
    int max=0;
    int left = 0;
    int right = 0;
    int L=0,R=0;
    for(i=0;i<n;i++)
    {
        if(i%2==0)
        {
            int index = i/2;
            L=index-1;
            R=index+1;
            while(L>=0&&R<len&&s[L]==s[R])
            {
                L--;
                R++;
            }
            L++;
            R--;
            if(R-L>max)
            {
                max=R-L;
                right=R;
                left=L;
            }
        }
        else if(i%2==1)
        {
            L=(i-1)/2;
            R=(i+1)/2;
            while(L>=0&&R<len&&s[L]==s[R])
            {
                L--;
                R++;
            }
            L++;
            R--;
            if(R-L>max)
            {
                max=R-L;
                right=R;
                left=L;
            }
        }
    }
    char *p=malloc(1000*sizeof('x'));
    int k=0;
    for(i=left;i<=right;i++)
    {
        //printf("%c",s[i]);
        p[k++]=s[i];
    }
    p[k]='\0';
    return p;
}