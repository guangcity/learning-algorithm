int min(int a,int b)
{
    if(a>b)
        return b;
    else
        return a;
}


int maximalSquare(char** matrix, int matrixRowSize, int matrixColSize) {
    int row,col;
    int max=0;
    int m[1000][1000];
    
    for(row=0;row<matrixRowSize;row++)
    {
        for(col=0;col<matrixColSize;col++)
        {
            if(matrix[row][col]=='1')
                m[row+1][col+1]=1;
            else
                m[row+1][col+1]=0;
        }
    }
    for(row=0;row<=matrixRowSize;row++)
    {
        for(col=0;col<=matrixColSize;col++)
        {
            if(m[row][col]==1)
            {
                m[row][col] = min(min(m[row][col-1],m[row-1][col]),m[row-1][col-1])+1;
            }
            if(m[row][col]>max)
                max=m[row][col];
        }
    }
    return max*max;
}
