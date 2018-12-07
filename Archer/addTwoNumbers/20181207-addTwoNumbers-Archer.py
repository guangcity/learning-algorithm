#!/usr/bin/env python
# -*- coding:utf-8 -*-

class Node(object):
     """创建节点"""
     def __init__(self, elem):
         self.elem = elem
         self.next = None  # 初始设置下一节点为空

class Linklist(object):
    """节点的一系列操作"""
    def __init__(self,node):
        self.head = node

    def is_empty(self):   #判断节点是否为空
        return self.head == None

    def append(self,item):   #在尾部添加节点
        node = Node(item)
        if self.is_empty():
            self.head = node
        else:
            cur = self.head
            while cur.next != None:
                cur = cur.next
            cur.next = node

    def delete(self,item):  #删除值为item的节点
        if self.is_empty():
            print "Null"
        else:
            curNow = self.head
            cur = None
            while curNow != None:
                if curNow.elem == item:
                    if curNow == self.head:
                        self.head = curNow.next
                    else:
                        cur.next = curNow.next
                    break
                else:
                    cur = curNow
                    curNow = curNow.next

    def travel(self):   # 遍历节点
        if self.is_empty():
            print "Null"
        else:
            cur = self.head
            while cur != None:
                print cur.elem
                cur = cur.next

if __name__ == "__main__":

    a = 619    #加数1
    b = 10     #加数2
    al = Linklist(None)
    bl = Linklist(None)
    add = Linklist(Node(0))

    # 将加数1变成逆序链表
    c = a
    if c != 0 :
        while c != 0:
            al.append(c%10)
            c /= 10
    else:
        al.append(0)

    # 将加数2变成逆序链表
    d = b
    if d != 0:
        while d != 0:
            bl.append(d%10)
            d /= 10
    else:
        bl.append(0)

    l1 = al.head
    l2 = bl.head
    la = add.head

    c_l1= l1
    c_l2 = l2
    c_la = la

    ext = 0   #加法中的进位

    while c_l1 != None or c_l2 != None:
        if c_l1 == None:   # 如果到了加数1的尾端，则执行以下操作
            while c_l2 != None:
                temp = c_l2.elem + ext
                if temp/10:
                    c_la.elem = temp %10
                    ext = 1
                else:
                    c_la.elem = temp
                    ext = 0
                c_l2 = c_l2.next
                c_la.next = Node(0)
                c_la = c_la.next
        if  c_l2 == None : # 如果到了加数2的尾端，则执行以下操作
            while c_l1 != None:
                temp = c_l1.elem + ext
                if temp/10:
                    c_la.elem = temp%10
                    ext = 1
                else:
                    c_la.elem = temp
                    ext = 0
                c_l1 = c_l1.next
                c_la.next = Node(0)
                c_la = c_la.next
        if c_l1 != None and c_l2 != None : # 如果两个加数的链表都还没到尾端，则执行以下操作
            temp = c_l1.elem + c_l2.elem +ext
            if temp / 10:
                c_la.elem = temp % 10
                ext = 1
            else:
                c_la.elem = temp
                ext = 0
            c_l1 = c_l1.next
            c_l2 = c_l2.next
            c_la.next = Node(0)
            c_la = c_la.next



    if ext == 1: #如果进位为1，则最后应该加上1
        c_la.elem = 1

    #上面循环加法后，会多出来一个结点，下面删除
    c_la = la
    pre_c_la = c_la
    while c_la != None:
        if c_la.next == None:
            if c_la == la:
                c_la = None
            elif c_la.elem == 0:  # 该结点为0才是冗余的，如果不为0，则是为进位的1，不能删除
                pre_c_la.next = None
                break
        pre_c_la = c_la
        c_la = c_la.next

    add.travel()  # 遍历加法得到的结果链表

