# python-bug

后面会不定期更新解决方案

## Question:


You are developing software to help a bookstore keep track of its inventory. You have been given a base class called Item which is constructed using a given name and an initial amount available. Method getAmount returns the amount of that item available. Calling the buy method increases the amount by a given number. Calling sell decreases the amount by a given number. The function getName returns the name of the item.

You have also been given incomplete classes that you need to edit. Hint: When modifying derived classes it is a good idea to call methods from the base class.

In the incomplete NewBook class below, edit __init__ to initialize with the name "new book". You should call a method/constructor from Item to do this.
New books are bought in packs of 10. In the NewBook class edit buy to increase the amount by 10. You should call a method from Item to do this.
New books are sold one at a time. In the NewBook class edit sell to decrease the amount by 1. You should call a method from Item to do this.
The bookstore wants to track how the number of items change over time. Thus class Item should be modified such that it saves the amount history as a list. In the Item class edit __init__, buy and sell to record the history. Then edit the getHistory so that it returns the history as a list.


Here is an example of how the NewBook class should be used

B = NewBook(20)
B.sell()
B.sell()
B.buy()

print(B)    
print("History is: " + str(B.getHistory()))。                    
The corresponding output would be

There are 28 new books available.
History is: [20, 19, 18, 28]




