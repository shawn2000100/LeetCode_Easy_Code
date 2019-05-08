#!/usr/bin/env python
# coding: utf-8

# In[56]:


import gc # 實作上可以考慮用這個
class MyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0
        
    def print_list(self):
        if(self.size == 0):
            print('Null List')
        else:
            for i in range(self.size):
                print(self.get(i), end=' ')
            print()

    def get(self, index):
        if index < 0: #處理異常狀況 -1, -2, -3...
            return -1
        
        ret_val = -1
        i = 0
        iter_node = self.head
        while(i < index):
            if(iter_node == None):
                break
            else:
                iter_node = iter_node.get_next()
            i += 1
        
        if(iter_node != None):
            ret_val = iter_node.get_data()
            
        return ret_val

    def addAtHead(self, data):
        node = Node(data) # 新增一個node存data
        
        # 如果原本就是空串列
        if(self.head == None):
            self.head = node
            self.tail = node
        # 正常情況下
        elif(self.head != None):
            node.set_next(self.head)
            self.head.set_prev(node)
            self.head = node
        
        self.size += 1

    def addAtTail(self, data):
        node = Node(data) # 新增一個node存data
        
        # 如果原本就是空串列
        if(self.tail == None):
            self.head = node
            self.tail = node
        # 正常情況下
        elif(self.tail != None):
            node.set_prev(self.tail)
            self.tail.set_next(node)
            self.tail = node
            
        self.size += 1
        
    def addAtIndex(self, index, data):
        # 處理異常狀況 index -1, -2...
        if index < 0:
            self.addAtHead(data) # leetcode上-1代表插入在頭...
        # 處理異常狀況 index > size
        elif index > self.size:
            return
        # 處理異常狀況 index == size
        elif index == self.size:
            self.addAtTail(data)
        elif index == 0:
            self.addAtHead(data)
        # 正常情況
        else:
            iter_node = self.head
            i = 0
            while(i <= index-1):
                iter_node = iter_node.get_next()
                i += 1
            
            node = Node(data)
            node.set_next(iter_node) 
            node.set_prev(iter_node.get_prev())
            node.get_prev().set_next(node)
            iter_node.set_prev(node)
            self.size += 1
        
    def deleteAtIndex(self, index):
        # 處理異常情形
        if index >= self.size or index < 0:
            return 
        
        # 刪頭
        if index == 0:
            iter_node = self.head
            if iter_node.get_next() != None: 
                iter_node.get_next().set_prev(None)
            self.head = iter_node.get_next()
            del iter_node
        # 刪尾
        elif index == self.size-1:
            iter_node = self.tail
            iter_node.get_prev().set_next(None)
            self.tail = iter_node.get_prev()
            del iter_node
        else:
            iter_node = self.head
            i = 0
            while(i < index):
                iter_node = iter_node.get_next()
                i += 1  
            iter_node.get_prev().set_next(iter_node.get_next())
            iter_node.get_next().set_prev(iter_node.get_prev())
            del iter_node
        
        self.size -= 1
#         gc.collect() # 這個好像會讓runtime增加不少... memory則減少一點

class Node:

    def __init__(self, data=None):
        self.data = data
        self.next_node = None
        self.prev_node = None

    # 得到此node的指標
    def get_data(self):
        return self.data

    # 得到下一個node的指標
    def get_next(self):
        return self.next_node
    
    # 得到上一個node的指標
    def get_prev(self):
        return self.prev_node
    
    # 設定下一個Link指向的node
    def set_next(self, new_node):
        self.next_node = new_node
    
    # 設定上一個Link指向的node
    def set_prev(self, new_node):
        self.prev_node = new_node


# Your MyLinkedList object will be instantiated and called as such:
obj = MyLinkedList()
obj.addAtHead(1)
obj.deleteAtIndex(0)
obj.print_list()
print(obj.size)

obj = MyLinkedList()
obj.addAtIndex(-1, 0)
obj.get(0)
obj.deleteAtIndex(-1)
obj.print_list()
print(obj.size)


# In[ ]:




