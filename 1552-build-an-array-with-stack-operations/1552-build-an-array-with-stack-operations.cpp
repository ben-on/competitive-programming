class Solution {
public:
    vector<string> buildArray(vector<int>& target, int n) {
       vector<int> s;
        vector<string> res;
        unordered_set<int> set(target.begin(), target.end());
        for (int i = 1; i <= n; i++) {
            s.push_back(i);
            res.push_back("Push");
            if (set.find(s.back()) == set.end()) {
                s.pop_back();
                res.push_back("Pop");
            }
            if (target == s) {
                return res;
            }
        }
        return res; 
        }
};