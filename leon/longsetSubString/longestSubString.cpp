#include <string>
#include <typeinfo>
#include <vector>
#include <algorithm>
// #include<unordered_set>
#include <iostream>
using namespace std;
class Solution
{
  public:
    int lengthOfLongestSubstring(string s)
    {
        int max = 0;
        int record = 0;
        auto size = s.size();
        // const char *p = s.data();
        vector<char> myvector;

        for (decltype(size) i = 0; i < size; i++)
        {
            char temp = s[i];

            if (find(myvector.begin(), myvector.end(), temp) != myvector.end())
            {
                while (find(myvector.begin(), myvector.end(), temp) != myvector.end())
                {
                    // cout << *(myvector.end());
                    cout << string("delete:") + *(myvector.begin()) << endl;
                    myvector.erase(myvector.begin());
                }
                myvector.push_back(temp);
                cout << string("insert:") + temp << endl;
                record = myvector.size();
                if (record > max)
                {
                    max = record;
                }
                for (auto i : myvector)
                {
                    cout << i << endl;
                }
            }
            else
            {
                record++;
                if (record > max)
                {
                    max = record;
                }
                cout << string("insert:") + temp << endl;
                myvector.push_back(temp);
                for (auto i : myvector)
                {
                    cout << i << endl;
                }
            }
        }
        // p = NULL;
        // free((void *)p);

        return max;
    }
};
int main()
{
    string a = "bbbb";
    Solution s;
    int max = s.lengthOfLongestSubstring(a);
    // cout << a;
    cout << a << endl;
    cout << max << endl;
    // string a_2 = "ynyo";
    // Solution s_2;
    // int max_2 = s_2.lengthOfLongestSubstring(a_2);
    // // cout << a;
    // cout << a_2 << endl;
    // cout << max_2;
    // if (typeid(char).name() == typeid(decltype(a[0])).name())
    //     cout << "true" << endl;

    return 0;
}
