LeetCode - 207.Course Schedule

link: https://leetcode.com/problems/course-schedule/

题目

There are a total of n courses you have to take, labeled from 0 to n-1.

Some courses may have prerequisites, for example to take course 0 you have to first take course 1, which is expressed as a pair: [0,1]

Given the total number of courses and a list of prerequisite pairs, is it possible for you to finish all courses?

Example 1:

    Input: 2, [[1,0]] 
    Output: true
    Explanation: There are a total of 2 courses to take. 
                 To take course 1 you should have finished course 0. So it is possible.

Example 2:

    Input: 2, [[1,0],[0,1]]
    Output: false
    Explanation: There are a total of 2 courses to take. 
                 To take course 1 you should have finished course 0, and to take course 0 you should
                 also have finished course 1. So it is impossible.

Note:

1. The input prerequisites is a graph represented by a list of edges, not adjacency matrices. Read more about how a graph is represented.
2. You may assume that there are no duplicate edges in the input prerequisites.



问题描述

给出一系列的先修课程关系，判断如果按照这个关系，是否能顺利完成所有课程学习



题目分析

此题目实际是判断有向图中是否存在环，而拓扑排序的一个重要应用就是判断有向图中是否存在环，如果图中不存在环，那么是可以根据这个图求出一个拓扑序列

- 根据拓扑排序的求取方式，我们先记录每个节点的入度数，以及以其为起始节点，对应的所有终止节点
- 每次去选取入度数为0的节点，然后访问掉这个节点，如果节点不存在，那就是说这个图中剩余所有节点都有指向其的边，此时即存在环
- 对应的，将其所指向的节点的入度数全部减1
- 接下来接着去寻找入度为0的节点，已经访问过的节点不再检查，重复步骤，直至节点全部被访问，或者存在环



代码实现

    # -*- coding: utf-8 -*-
    
    
    class Solution:
        def canFinish(self, numCourses, prerequisites):
            """
            :type numCourses: int
            :type prerequisites: List[List[int]]
            :rtype: bool
            """
            all_nodes = {i: {'num': 0, 'node': []} for i in range(numCourses)}
            for end, start in prerequisites:
                all_nodes[start]['node'].append(end)
                all_nodes[end]['num'] += 1
    
            all_nodes_set = set([_ for _ in range(numCourses)])
    
            while len(all_nodes_set) != 0:
                flag = False
                for start_node in all_nodes_set:
                    if all_nodes[start_node]['num'] == 0:
                        flag = True
                        break
                if not flag:
                    return False
                all_nodes_set.remove(start_node)
                for end_node in all_nodes[start_node]['node']:
                    all_nodes[end_node]['num'] -= 1
            return True
    
    
    if __name__ == '__main__':
        solution = Solution()
        assert solution.canFinish(2, [[1, 0]]) is True
    



运行结果

  Time Submitted   	Status  	Runtime	Language
  a few seconds ago	Accepted	268 ms 	python3 



吐槽

LeetCode给出的模板，函数名和变量名没有按照PEP8规范来，正常是不应该驼峰命名的，而应该是小写加下划线形式
