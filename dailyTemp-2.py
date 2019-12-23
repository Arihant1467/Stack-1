class Solution {
    public int[] dailyTemperatures(int[] T) {
        
        int len = T.length-1;
        int i=0;
        int[] nextWarmerDays = new int[T.length];
        
        
        Stack<Integer> st = new Stack<>();
        while(i<=len) {
            
            while(!st.isEmpty() && T[i] > T[st.peek()]) {
                int j = st.pop();
                nextWarmerDays[j] = (i-j);
            }
            
            st.push(i);
            i+=1;
    }
        
        return nextWarmerDays;
    }
}
