class Solution {

    public String largestTimeFromDigits(int[] A) {
        int res = -1;
        for(int i = 0; i < 4; i ++){
            for(int j = 0; j < 4; j ++){
                if(i == j){
                    continue;
                }
                int hour = A[i] * 10 + A[j];
                if(hour > 23){
                    continue;
                }
                for(int m = 0; m < 4; m ++){
                    if(m == i || m == j){
                        continue;
                    }
                    for(int n = 0; n < 4; n ++){
                        if(n == i || n == j || n ==m){
                            continue;
                        }
                        int minute = A[m] * 10 + A[n];
                        if(minute > 59){
                            continue;
                        }
                        res = Math.max(res, hour * 100 + minute);
                    }
                }
            }
        }
        return res == -1 ? "": (res/100 < 10 ? "0" + res/100: res/100) + ":" + (res % 100 < 10 ? "0" + res%100: res%100);
    }
}