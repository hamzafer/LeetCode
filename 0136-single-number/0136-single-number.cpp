class Solution
{
    public:
        int singleNumber(vector<int> &nums)
        {
            unordered_map<int, int> map;

            for (auto x: nums)
                map[x]++;

            for (auto z: map)
                if (z.second == 1)
                    return z.first;

            return -1;
        }
};