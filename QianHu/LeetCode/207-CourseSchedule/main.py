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
