int reverse(int x) {
    long res=0;
    while(x!=0){
        res=res*10+x%10;
        x/=10;
    }
    int flog1=0x7fffffff;
    int flog2=0x80000000;
    if(res<flog2||res>flog1){
        return 0;
    }
   return (int)res; 
    
}
