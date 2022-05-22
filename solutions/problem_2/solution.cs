public class Solution {
    public int MaximumBags(int[] capacity, int[] rocks, int additionalRocks) {
        int n = rocks.Length;
        int i = 0;
        int count = 0;
        int[] diff = new int[n];
        for(i = 0; i < n; i++)
        {
            diff[i] = capacity[i] - rocks[i];
        }
        Array.Sort(diff);
        for(i = 0; i < n; i++)
        {
            if(diff[i] == 0)
                count++;
            else if(additionalRocks >= diff[i])
            {
                additionalRocks -= diff[i];
                count++;
            }
            else
                break;
        }
        return count;
    }
}