#include<bits/stdc++.h>

class Solution {
public:
    int count_digits(int n){
        string s = to_string(n);
        return s.size();
    }
    
    int findNumbers(vector<int>& nums) {
        int count = 0;
        for (auto i : nums){
            if(count_digits(i)%2){
                count++;
            }
        }
        return nums.size() - count;
    }
};
