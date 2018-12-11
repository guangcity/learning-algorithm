### Problem

Given a string, find the length of the longest substring without repeating characters.

Example 1:

```c++
Input: "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.
```

Example 2:

```c++
Input: "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.
```

Example 3:

```c++
Input: "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
             Note that the answer must be a substring, "pwke" is a subsequence and not a substring.
```

### Answer

```c++
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
                    // cout << string("delete:") + *(myvector.begin()) << endl;
                    myvector.erase(myvector.begin());
                }
                myvector.push_back(temp);
                // cout << string("insert:") + temp << endl;
                record = myvector.size();
                if (record > max)
                {
                    max = record;
                }
                // for (auto i : myvector)
                // {
                //     cout << i << endl;
                // }
            }
            else
            {
                record++;
                if (record > max)
                {
                    max = record;
                }
                // cout << string("insert:") + temp << endl;
                myvector.push_back(temp);
                // for (auto i : myvector)
                // {
                //     cout << i << endl;
                // }
            }
        }
        // p = NULL;
        // free((void *)p);

        return max;
    }
};
```

#### Using vector

when I first saw the question,my opinion is to get the character of the string one by one.and use a data structure to store substring that meeting the requirements that adjacent element is different.Meanwhile,caculate the length of the storage.And assign the maximum value to the variable "max" .Finally,return max.

#### Bug encountered

1. the select of data structure.(I use vector,but I tried to use set which is completed by the red blacktrees.When using set,I met a bug that my substring will be sorted automatically so I change to vector.)
2. Use FIFO(first in first out),so need push_back and erase(vec.begin());
3. Finally,in the leetcode we can't cout too many contents;