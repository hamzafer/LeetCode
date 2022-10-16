class Solution
{
    public:
        int missingNumber(vector<int> &nums)
        {
            int sum = 0;
            int arraySum = 0;
            for (int i = 0; i <= nums.size(); i++)
            {
                sum += i;
                if (i != nums.size())
                {
                    arraySum += nums[i];
                }
            }
            return sum - arraySum;
        }
};