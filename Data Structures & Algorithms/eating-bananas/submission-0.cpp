class Solution {
public:
    int minEatingSpeed(vector<int>& piles, int h) {
        //Minimum speed to eat the bananas is 1 per hour.
        //Maximum speed to finish the piles is the maximum number in the 
        // piles array.

        int upper_bound=INT_MIN;
        for(int i=0;i<piles.size();i++)
        {
            upper_bound=max(upper_bound,piles[i]);
        }

        int lower_bound=1;
        int minimum_hours_taken=INT_MAX;
        int result;

        while(lower_bound<=upper_bound)
        {
            int mid=(lower_bound+upper_bound)/2;
            int hours_taken=0;
            for(int i=0;i<piles.size();i++)
            {
                int dividend = piles[i]/mid;
                int remainder=piles[i]%mid;
                hours_taken+= dividend;
                if(remainder !=0) hours_taken+=1;
            }
            if(hours_taken>h)
            {
                 lower_bound=mid+1;
            }
            else
            {
                upper_bound=mid-1;
                result=mid;
            }
        }
        return result;
    }
};
