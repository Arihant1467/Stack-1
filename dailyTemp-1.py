class Solution {
    public int[] dailyTemperatures(int[] T) {
        
        int len = T.length-1;
        int i=0;
        int[] nextWarmerDays = new int[T.length];
        for(i=0;i<=len;++i){
            int j=i+1;
            while(j<=len){
                if(T[i]<T[j]){
                    nextWarmerDays[i]=(j-i);
                    break;
                }
                j+=1;
            }
        }
        
        return nextWarmerDays;
    }
}
