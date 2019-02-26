公粮. 

[题目在这](https://leetcode-cn.com/problems/ipo/description/)

说: 假设 LeetCode 即将开始其 IPO。为了以更高的价格将股票卖给风险投资公司，LeetCode希望在 IPO 之前开展一些项目以增加其资本。 由于资源有限，它只能在 IPO 之前完成最多 k 个不同的项目。帮助 LeetCode 设计完成最多 k 个不同项目后得到最大总资本的方式。

给定若干个项目。对于每个项目 i，它都有一个纯利润 Pi，并且需要最小的资本 Ci 来启动相应的项目。最初，你有 W 资本。当你完成一个项目时，你将获得纯利润，且利润将被添加到你的总资本中。

总而言之，从给定项目中选择最多 k 个不同项目的列表，以最大化最终资本，并输出最终可获得的最多资本。

举了个例子: 

> 输入: k=2, W=0, Profits=[1,2,3], Capital=[0,1,1].
>
> 输出: 4
>
> 解释:
> 由于你的初始资本为 0，你尽可以从 0 号项目开始。
> 在完成后，你将获得 1 的利润，你的总资本将变为 1。
> 此时你可以选择开始 1 号或 2 号项目。
> 由于你最多可以选择两个项目，所以你需要完成 2 号项目以获得最大的资本。
> 因此，输出最后最大化的资本，为 0 + 1 + 3 = 4。

题目看上去很简单, 贪心就好嘛. 将两个数组排序, 按照 Capital 从小到大 Profits 从大到小排序, 然后循环贪心选择 k 次就好啦. 

然后你就发现你超时了... 

所以这里需要一些小技巧, 优先队列. 

代码如下: 

```
class Solution {
    typedef pair<int, int> PC;
    
public:
    static bool cmp(PC x, PC y) { return x.second < y.second || (x.second == y.second && x.first > y.first); }
    
    int findMaximizedCapital(int k, int w, vector<int>& P, vector<int>& C) {
        vector<PC> vec;
        for (int i = 0; i < P.size(); i++) vec.push_back(make_pair(P[i], C[i]));
        sort(vec.begin(), vec.end(), cmp);
        //for (int i = 0; i < vec.size(); i++) cout<<vec[i].first<<"\t"<<vec[i].second<<endl;
        //vector<bool> chosen(vec.size(), false);

        int res = w, pos = 0;
        priority_queue<int> pq;

        while (k--) {
            int index = -1, curr = INT_MIN;
            for ( ; pos < vec.size() && vec[pos].second <= res; pos++) {
                pq.push(vec[pos].first);
            }
            if (pq.empty()) {
                break;
            } else {
                res += pq.top(); pq.pop();
            }
        }
        return res;
    }
};
```
