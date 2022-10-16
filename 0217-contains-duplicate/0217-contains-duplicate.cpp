class Solution
{
    public:
        set<int> convertToSet(vector<int> v)
        {
            set<int> s;
            for (int x: v)
            {
                s.insert(x);
            }
            return s;
        }

    bool containsDuplicate(vector<int> &nums)
    {
        if (convertToSet(nums).size() == nums.size())
            return false;

        return true;
    }
};