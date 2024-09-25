#!/usr/bin/python3
"""Module verbose_list using abstract class to defines a list"""


class VerboseList(list):
    """Inherited class of list built-in python"""

    def append(self, item):
        """Implementing append method"""
        super().append(item)
        print("Added {} to the list".format(item))

    def extend(self, lst):
        """Implementing extend method"""
        item_count = len(lst)
        super().extend(lst)
        print("Extend the list with {} items.".format(item_count))

    def remove(self, item):
        """Removing extend method"""
        print("Removed {} from the list".format(item))
        super().remove(item)

    def pop(self, index=-1):
        """Popping extend method returning index item"""
        item = self[index]
        print("Popped {} from the list".format(item))
        return super().pop(index)


if __name__ == "__main__":
    """Instantation of VerboseList objects"""
    vlist = VerboseList()

    vlist.append(1)
    print("Current list:", vlist)
    vlist.append(2)
    print("Current list:", vlist)

    vlist.extend([3, 4, 5, 6])
    print("Current list:", vlist)

    vlist.remove(2)
    print("Current list:", vlist)

    vlist.pop()
    print("Current list:", vlist)
    vlist.pop(1)
    print("Current list:", vlist)
    vlist.pop(0)
    print("Current list:", vlist)
