class Solution {
public:
    bool wordBreak(string s, vector<string>& wordDict) {
        vector<bool> state(s.length()+1, false);
        state[0] = true;
        for (int i = 1; i <= s.length(); i++) {
			//for (int j = 0; j <=i ; j++)
            for (int j = i-1; j >=0 ; j--) {
                if (state[j] && find(wordDict.begin(), wordDict.end(), s.substr(j, i-j)) != wordDict.end()) {
                    state[i] = true;
                }
            }
        }        
        return state[s.length()];
    }
};