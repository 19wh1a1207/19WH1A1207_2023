class Solution {
public:
    int removeDuplicates(vector<int>& nums) {
        set <int> s;
        int count = 0;
        for(auto itr = nums.begin(); itr != nums.end(); itr++){
            if(s.find(*itr) == s.end())
                s.insert(*itr);
            else{
                *itr = INT_MAX;
                count++;
            }
        }
        sort(nums.begin(), nums.end());
        return nums.size() - count;
    }
};
