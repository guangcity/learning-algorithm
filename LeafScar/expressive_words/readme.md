# LeetCode 809——情感丰富的文字
### 题目
&emsp;&emsp;有时候人们会用额外的字母来表示额外的情感，比如 "hello" -> "heeellooo", "hi" -> "hiii"。我们将连续的相同的字母分组，并且相邻组的字母都不相同。我们将一个拥有三个或以上字母的组定义为扩张状态（extended），如第一个例子中的 "e" 和" o" 以及第二个例子中的 "i"。 此外，"abbcccaaaa" 将有分组 "a" , "bb" , "ccc" , "dddd"；其中 "ccc" 和 "aaaa" 处于扩张状态。

&emsp;&emsp;对于一个给定的字符串 S ，如果另一个单词能够通过将一些字母组扩张从而使其和 S 相同，我们将这个单词定义为可扩张的（stretchy）。我们允许选择一个字母组（如包含字母 c ），然后往其中添加相同的字母 c 使其长度达到 3 或以上。注意，我们不能将一个只包含一个字母的字母组，如 "h"，扩张到一个包含两个字母的组，如 "hh"；所有的扩张必须使该字母组变成扩张状态（至少包含三个字母）。

&emsp;&emsp;输入一组单词，输出其中可扩张的单词数量。

**示例：**  
**输入：**  
```
S = "heeellooo"
words = ["hello", "hi", "helo"]
```
**输出：** 
```
1
```
**解释：**  
我们能通过扩张"hello"的"e"和"o"来得到"heeellooo"。
我们不能通过扩张"helo"来得到"heeellooo"因为"ll"不处于扩张状态。


**说明：**
* 0 <= len(S) <= 100。
* 0 <= len(words) <= 100。
* 0 <= len(words[i]) <= 100。
* S 和所有在 words 中的单词都只由小写字母组成。

### 思路

**对题目的理解：**
* 不扩充状态：原单词的单个字母连续出现次数与扩充后单词对应处连续出现次数相等
* 扩充状态：原单词的单个字母连续出现次数与扩充后单词对应字母处比较，扩充后单词对应字母连续出现次数大于原单词的单个字母连续出现次数，且必须大于3次

**实现想法：**

原单词与扩充后单词顺序扫描，记录单个字母连续出现次数，分别记为t_flag与s_flag；
![File](file.png)
1. 如果顺序扫描时，出现扩充字母与原单词字母不同，直接返回false；
2. t_flag等于s_flag 或者 （s_flag大于等于3 且 s_flag的值大于t_flag的值）才进行下一种字母的判断；
3. 直到其中一个单词扫描完结束，另一个单词还未扫描完，那一定是false;

**代码实现：**
```
bool expressiveWord(string s, string t)
{
	int s_i = 0;    // 扩充单词扫描到的下标
	int t_i = 0;    // 原单词扫描到的下标

	while (s_i < s.length() && t_i < t.length())
	{
		if (s[s_i] != t[t_i])
			return false;

		int s_flag = 0;
		while (s[s_i] == t[t_i])    // 记录扩充单词字母连续用出现次数
		{
			s_i++;
			s_flag++;
		}

		int t_flag = 0;
		while (s[s_i - 1] == t[t_i])    // 记录原单词字母连续用出现次数
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

// 接下去就是遍历整组单词，记录满足符合给定扩充单词的原单词的数量
int expressiveWords(string S, std::vector<string>& words) {
	int num = 0;
	for (int i = 0; i < words.size(); ++i)
	{
		if (expressiveWord(S, words[i]))
			num++;
	}
	return num;
}
```





