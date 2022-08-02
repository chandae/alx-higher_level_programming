#!/usr/bin/python3
""" Class Based Linked List Module """


class Node():
    """ Base Class For Linked List: Node """

    def __init__(self, data, next_node=None):
        """ Constructor """
        self.__data = data
        self.__next_node = next_node

    def __str__(self):
        """ Printable Node Instance """

        if self.__next_node:
            return f"Data: {self.__data} Next Node: {self.__next_node.data}"
        else:
            return f"Data: {self.__data} Next Node: None"

    @property
    def data(self):
        """ Return node data """
        return self.__data

    @data.setter
    def data(self, value):
        """ Data attribute setter method """
        if (isinstance(value, int)):
            self.__data = value
        else:
            raise TypeError("data must be an integer")

    @property
    def next_node(self):
        """ Return next node """
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        """ Next node attribute setter function """
        if value is None or (isinstance(value, Node)):
            self.__next_node = value
        else:
            raise TypeError("next_node must be a Node object")


class SinglyLinkedList():
    """ Singly Linked List Class """

    def __init__(self):
        """ Constructor """
        self.__head = None

    def __str__(self):
        """ Printable Linked List Instance """
        if self.__head is None:
            print('Linked list is empty')
        else:
            itr = self.__head
            linked_list = ""
            while itr:
                linked_list += str(itr.data) + '\n'
                itr = itr.next_node
            return linked_list

    def sorted_insert(self, value):
        """ Adds a new node in sorted increasing order """

        # if linked list is empty set new node as head
        if self.__head is None:
            node = Node(value, None)
            self.__head = node
        else:
            curr_node = self.__head
            while curr_node:
                if not curr_node.next_node:
                    if value < curr_node.data:
                        node = Node(value, curr_node)
                        self.__head = node
                    else:
                        node = Node(value, None)
                        curr_node.next_node = node
                    break
                else:
                    if value < curr_node.data:
                        node = Node(value, curr_node)
                        self.__head = node
                        break
                    elif curr_node.data <= value <= curr_node.next_node.data:
                        node = Node(value, curr_node.next_node)
                        curr_node.next_node = node
                        break
                    else:
                        curr_node = curr_node.next_node
