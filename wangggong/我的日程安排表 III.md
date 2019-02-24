公粮. 

这次与其说是一个算法题, 不如说是把算法放在 OO 的框子下的一个东西. 

题目是这样的:

> 实现一个 `MyCalendar` 类来存放你的日程安排，你可以一直添加新的日程安排。
>
> `MyCalendar` 有一个 `book(int start, int end)` 方法。它意味着在start到end时间内增加一个日程安排，注意，这里的时间是半开区间，即 `[start, end)`, 实数 `x` 的范围为，  `start <= x < end`。
>
> 当 __K__ 个日程安排有一些时间上的交叉时（例如K个日程安排都在同一时间内），就会产生 __K__ 次预订。
>
> 每次调用 `MyCalendar.book`方法时，返回一个整数 __K__ ，表示最大的 __K__ 次预订。
>
> 请按照以下步骤调用MyCalendar 类: `MyCalendar cal = new MyCalendar(); MyCalendar.book(start, end)`

还举了个例子: 

> MyCalendarThree();
> MyCalendarThree.book(10, 20); // returns 1
> MyCalendarThree.book(50, 60); // returns 1
> MyCalendarThree.book(10, 40); // returns 2
> MyCalendarThree.book(5, 15); // returns 3
> MyCalendarThree.book(5, 10); // returns 3
> MyCalendarThree.book(25, 55); // returns 3

题目本身说的意思可以理解为一个数轴上有若干个线段, 问哪个区域的覆盖的线段数目最多. 

直接看答案, 答案通过讨论每个边界位置的覆盖线段数目来计算最大的预订数, 具体实现是通过维护一个哈希表实现. 具体代码如下: 

```
class MyCalendarThree {
    map<int, int> M;
    
public:
    MyCalendarThree() {
        // Do nothing... 
    }
    
    int book(int start, int end) {
        M[start] = (M.count(start) ? M[start] : 0) + 1;
        M[end]   = (M.count(end) ? M[end] : 0) - 1;
        
        int res = 0;
        int cur = 0;
        for (auto it = M.begin(); it != M.end(); ++it) {
            cur += it->second;
            res = max(res, cur);
        }
        
        return res;
    }
};
```

引申的有通过二叉搜索树进行模拟的解法, 本质区别不大, 但写的时候就会难受得多: 

```
class MyCalendarThree {
    class Node {
        int pos, val;
        Node* left;
        Node* right;
        
        friend Node* insert(Node* node, int pos, int val);
        friend void count(Node* node, int& maxCnt, int& curr);

    public:
        Node(int pos, int val) : pos (pos), val (val), left (nullptr), right (nullptr) {}
    };
    
    Node* node;
    
    friend Node* insert(Node* node, int pos, int val) {
        if (node == nullptr) {
            node = new Node(pos, val);
        } else if (node->pos == pos) {
            node->val += val;
        } else if (node->pos < pos) {
            node->right = insert(node->right, pos, val);
        } else {
            node->left  = insert(node->left, pos, val);
        }
        return node;
    }
    
    friend void count(Node* node, int& maxCnt, int& curr) {
        if (node != nullptr) {
            count(node->left, maxCnt, curr);
            curr += node->val;
            maxCnt = max(maxCnt, curr);
            count(node->right, maxCnt, curr);
        }
    }
    
public:
    MyCalendarThree() {
        // Do nothing... 
        node = nullptr;
    }
    
    int book(int start, int end) {
        node = insert(node, start, 1);
        node = insert(node, end, -1);
        int maxCnt = 0;
        int curr   = 0;
        count(node, maxCnt, curr);
        return maxCnt;
    }
};
```

(这里其实有一个误区, 类内的类还需要信息隐藏吗? 其实是不用的. 强行信息隐藏只会恶心自己. 

但如果真的是面试的话, 个人还是建议第一种做法, 除非你能熟练手撸线段树啥的.
