#include <vector>

using namespace std;

class Solution {
public:
	int expressiveWords(string S, std::vector<string>& words) {
		int num = 0;
		for (int i = 0; i < words.size(); ++i)
		{
			if (expressiveWord(S, words[i]))
				num++;
		}
		return num;
	}

	bool expressiveWord(string s, string t)
	{
		int s_i = 0;
		int t_i = 0;

		while (s_i < s.length() && t_i < t.length())
		{
			if (s[s_i] != t[t_i])
				return false;

			int s_flag = 0;
			while (s[s_i] == t[t_i])
			{
				s_i++;
				s_flag++;
			}

			int t_flag = 0;
			while (s[s_i - 1] == t[t_i])
			{
				t_flag++;
				t_i++;
			}

			if (t_flag == s_flag  || (s_flag >= 3 && t_flag <= s_flag))
				continue;

			return false;
		}
		return s_i == s.length() && t_i == t.length();
	}
};
