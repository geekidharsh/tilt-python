### How do you do multithreading and multiprocessing in python?

 Multithreading:
*Read more: https://realpython.com/python-gil/#the-impact-on-multi-threaded-python-programs.* 
	- When you look at a typical Python program—or any computer program for that matter—there’s a difference between
    those that are CPU-bound in their performance and those that are I/O-bound.
    - CPU-bound programs are those that are pushing the CPU to its limit. This includes programs that do mathematical 
    computations like matrix multiplications, searching, image processing, etc.
	- I/O-bound programs are the ones that spend time waiting for Input/Output which can come from a user, file, 
    database, network, etc. 
    - I/O-bound programs sometimes have to wait for a significant amount of time till they get what they need from the source due to the fact that the source may need to do its own processing before the 
    input/output is ready, for example, a user thinking about what to enter into an input prompt or a database query running in its own process.

**Multi processing vs multithreading:**
https://towardsdatascience.com/multithreading-vs-multiprocessing-in-python-3afeb73e105f

- Process is an independent instance executed in a processor core. Threads are components of a process and 
        run concurrently (inside that process).
- Processes do not share the same memory space, while threads do (their mother’s memory).
 - Threads are lighter and cause less overhead. Also, because they share the same memory inside a process, it is easier, faster, and safer to share data.
- True parallelism can ONLY be achieved using multiprocessing. That is because only one thread can be executed at a given time inside a process time-space. This is assured by Python’s global interpreter lock (GIL).
- Processes execution is scheduled by the operating system, while threads are scheduled by the GIL.
- Multithreading implements concurrency, multiprocessing implements parallelism. Processes run on separate processing nodes.

-**What is GIL in python or What Problem Did the GIL Solve for Python?**
    Python uses reference counting for memory management. It means that objects created in Python have a 
    reference count variable that keeps track of the number of references that point to the object. 
    When this count reaches zero, the memory occupied by the object is released.

   Let’s take a look at a brief code example to demonstrate how reference counting works:

    >>>
    import sys
    a = []
    b = a
    sys.getrefcount(a)

   In the above example, the reference count for the empty list object [] was 3. The list object was referenced 
    by a, b and the argument passed to sys.getrefcount().

  Back to the GIL:
  - The problem was that this reference count variable needed protection from race conditions where two threads 
    increase or decrease its value simultaneously. If this happens, it can cause either leaked memory that is never 
    released or, even worse, incorrectly release the memory while a reference to that object still exists. 
  - This can cause crashes or other “weird” bugs in your Python programs.
- This reference count variable can be kept safe by adding locks to all data structures that are shared across t
    hreads so that they are not modified inconsistently.

- But adding a lock to each object or groups of objects means multiple locks will exist which can cause another 
    problem—Deadlocks (deadlocks can only happen if there is more than one lock). Another side effect would be decreased performance caused by the repeated acquisition and release of locks.
- The GIL is a single lock on the interpreter itself which adds a rule that execution of any Python bytecode 
    requires acquiring the interpreter lock. This prevents deadlocks (as there is only one lock) and doesn’t 
    introduce much performance overhead. But it effectively makes any CPU-bound Python program single-threaded.



### Different testing types: 

Testing in python. 

In Python, there are several types of testing that can be performed to ensure the quality of the code. 
    
Some of the commonly used testing types in Python are:
  1. Unit Testing: Unit testing involves testing individual components or modules of the code to ensure 
        they function as expected. The aim is to test the smallest possible piece of code in isolation from 
        the rest of the system.
    2. Integration Testing: Integration testing involves testing how different modules of the code interact 
        with each other to ensure they work together as expected. This type of testing ensures that the various
        components of the system can communicate and function together properly.
    3. Functional Testing: Functional testing involves testing the overall functionality of the software system
         to ensure that it meets the business requirements and functions as expected. This type of testing is 
         focused on testing the end-to-end functionality of the system.
    4. Acceptance Testing: Acceptance testing is a type of testing where the end user or customer tests the system
         to ensure that it meets their requirements and works as expected.
    5. Regression Testing: Regression testing involves retesting the code after making changes to ensure that 
        the changes have not introduced any new bugs or issues in the system. This type of testing is important 
        to ensure that changes do not negatively impact existing functionality.
    6. Performance Testing: Performance testing involves testing the system's performance under various loads 
        to ensure that it can handle the expected number of users and transactions without slowing down or crashing.
    7. Security Testing: Security testing involves testing the system for potential vulnerabilities and 
        weaknesses to ensure that it is secure from external threats and attacks.
    
   Python provides various frameworks such as unittest, pytest, and nose to perform these testing types.

### unitests in python?

In Python, unittests are a way to test individual units of code, such as functions, methods, and classes, in isolation from the rest of the program. The `unittest` module provides a framework for writing and running tests in Python.

- Unit tests help ensure that individual parts of a program are working as expected, and can be used to catch 
    bugs and errors early in the development process. 
-  Unit tests are typically automated, and can be run frequently during development to ensure that changes 
    to the code do not introduce new bugs or break existing functionality.
    example:
	    import unittest

	    def add_numbers(x, y):
	        return x + y

	    class TestAddNumbers(unittest.TestCase):

        def test_add_numbers(self):
            self.assertEqual(add_numbers(2, 3), 5)
            self.assertEqual(add_numbers(-1, 1), 0)
            self.assertEqual(add_numbers(0, 0), 0)

	    if __name__ == '__main__':
	        unittest.main()
    
- Different assert methods in python unittest:
    assertEqual(a, b): Checks if a and b are equal.
    assertNotEqual(a, b): Checks if a and b are not equal.
    assertTrue(x): Checks if x is true.
    assertFalse(x): Checks if x is false.
    assertIs(a, b): Checks if a and b are the same object.
    assertIsNot(a, b): Checks if a and b are not the same object.
    assertIsNone(x): Checks if x is None.
    assertIsNotNone(x): Checks if x is not None.
    assertIn(a, b): Checks if a is a member of the sequence b.
    assertNotIn(a, b): Checks if a is not a member of the sequence b.
    assertIsInstance(a, b): Checks if a is an instance of the class b.
    assertNotIsInstance(a, b): Checks if a is not an instance of the class b.

- What is an instance in python
    An instance refers to an individual occurrence of a class. When a class is defined, it is like a blueprint or 
    a template for creating objects. An instance is created when the class is instantiated, 
    which means that an object is created based on the class definition.
    class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
    
    my_car = Car('Ford', 'Mustang', 2022)
    Here my_car is an instance of Car

- Object and instance:
    Not all objects are instances but all instances are an object (of some specific class).
    Since in python, object is a more general term, it can be an instance but can also include 
    other built-in types such as strings, lists, and dictionaries.


## Different data structures in python:
   Python provides a variety of built-in data structures that can be used to store and manipulate data. 
  Here are some of the most commonly used data structures in Python:

### Lists: 
A list is a collection of ordered and mutable elements, which can be of any data type. 
    Lists are created using square brackets [] and items are separated by commas. 
    Example: my_list = [1, 2, "three", 4.0]

   ### Tuples: 
   A tuple is similar to a list, but it is immutable, meaning it cannot be changed once it is created. 
   Tuples are created using parentheses () and items are separated by commas. 
   Example: my_tuple = (1, 2, "three", 4.0)
   
   ### Sets: 
   A set is an unordered collection of unique elements. Sets are created using curly braces {} or the set() function. Example: 
    my_set = {1, 2, 3, 4}
   
   ### Dictionaries: 
   A dictionary is a collection of key-value pairs, where each key is unique and mapped 
   to a corresponding value. 
   Example: my_dict = {'name': 'John', 'age': 25, 'city': 'New York'}
   
   Strings: A string is a sequence of characters enclosed in single or double quotes. Strings can be 
   manipulated using various methods and operators. 
   Example: my_string = "Hello, World!"
   
   ### Arrays: 
   An array is a collection of similar data types, which can be of fixed size or dynamic size. Arrays are created using the array module. 
       
    Example: my_array = array('i', [1, 2, 3, 4, 5])

       Implement array in python vs list:
       import array as arr

       my_array = arr.array('i', [1, 2, 3, 4, 5])  # creating an array of integers
       my_list = [1, 2, 'hello', 3.14, True]       # creating a list of elements of different data types

 In array(), takes two parameter: typecode and initializer. my_array = arr.array(typecode, initializer) in the example above 'i' typecode is used for integers.
        The typecode argument specifies the data type of the elements in the array. 
        The available type codes are:

        'b': signed integer (1 byte)
        'B': unsigned integer (1 byte)
        'h': signed integer (2 bytes)
        'H': unsigned integer (2 bytes)
        'i': signed integer (4 bytes)
        'I': unsigned integer (4 bytes)
        'l': signed integer (4 bytes on 32-bit platform, 8 bytes on 64-bit platform)
        'L': unsigned integer (4 bytes on 32-bit platform, 8 bytes on 64-bit platform)
        'f': floating point (4 bytes)
        'd': floating point (8 bytes)


   ### Linked Lists: 
   A linked list is a linear data structure that consists of nodes connected by pointers. 
   Each node contains a data element and a reference to the next node in the sequence. 
   Linked lists can be implemented using classes in Python.
    
        Implement Linked Lists in python:
        ----------------
        class Node:
            def __init__(self, data):
                self.data = data
                self.next = None

        class LinkedList:
            def __init__(self):
                self.head = None
            
            def append(self, data):
                new_node = Node(data)
                
                if not self.head:
                    self.head = new_node
                    return
                
                curr_node = self.head
                while curr_node.next:
                    curr_node = curr_node.next
                
                curr_node.next = new_node
            
            def prepend(self, data):
                new_node = Node(data)
                
                if not self.head:
                    self.head = new_node
                    return
                
                new_node.next = self.head
                self.head = new_node
            
            def delete(self, data):
                if not self.head:
                    return
                
                if self.head.data == data:
                    self.head = self.head.next
                    return
                
                curr_node = self.head
                while curr_node.next:
                    if curr_node.next.data == data:
                        curr_node.next = curr_node.next.next
                        return
                    curr_node = curr_node.next
            
            def print_list(self):
                curr_node = self.head
                while curr_node:
                    print(curr_node.data)
                    curr_node = curr_node.next
        
   The Node class represents a single node in the linked list, which contains a data attribute and a next attribute that points to the next node in the list. The LinkedList class represents the linked list itself, which contains a head attribute that points to the first node in the list.
   - The append() method adds a new node to the end of the list, 
   - the prepend() method adds a new node to the beginning of the list, 
   - and the delete() method removes a node from the list. 
   - The print_list() method prints out the values of all the nodes in the list.
        

    
### Stacks: 
A stack is a data structure that follows the Last-In-First-Out (LIFO) principle, 
    where the last element added to the stack is the first one to be removed. Stacks can be implemented 
    using lists or linked lists in Python.
        items.pop()
        items.append() // equivalent for push() but using list
    
        Implement Stacks using list in python: 
        ----------------
        class Stack:
            def __init__(self):
                self.items = []

            def push(self, item):
                self.items.append(item)

            def pop(self):
                return self.items.pop()

            def peek(self):
                return self.items[-1]

            def is_empty(self):
                return len(self.items) == 0

            def size(self):
                return len(self.items)
    
   
 ### Queues: 
 A queue is a data structure that follows the First-In-First-Out (FIFO) principle, where the 
    first element added to the queue is the first one to be removed. Queues can be implemented using lists or linked lists in Python.

        Implement Queue in python:
        ---------------
        from collections import deque

        class Queue:
            def __init__(self):
                self.items = deque()

            def enqueue(self, item):
                self.items.append(item)

            def dequeue(self):
                return self.items.popleft()

            def is_empty(self):
                return len(self.items) == 0

            def size(self):
                return len(self.items)

            my_queue = Queue()
            my_queue.enqueue(1)
            my_queue.enqueue(2)
            my_queue.enqueue(3)

            print(my_queue.dequeue())  # Output: 1

            print(my_queue.is_empty()) # Output: False

            print(my_queue.size())     # Output: 2


### What are decorators in python?
   In Python, a decorator is a special type of function that can modify or enhance the behavior of another function. Decorators are used to add functionality to existing functions, without modifying their source code.

- In Python, functions are first-class objects, which means they can be passed around and used 
    as arguments to other functions. Decorators take advantage of this feature to modify the 
    behavior of functions.
- Here is an example of a simple decorator in Python:
	

		def my_decorator(func):
         def wrapper():
             print("Before the function is called.")
             func()
             print("After the function is called.")
         return wrapper

		@my_decorator
		def say_hello():
			print("Hello!") 
		say_hello()

 
 - In this example, my_decorator is a function that takes another function (func) as an argument, and returns a new function (wrapper) that modifies the behavior of the original function. 
- The @my_decorator syntax is a shorthand for calling say_hello with my_decorator as an argument,  like this:

	    say_hello = my_decorator(say_hello)

    
- Decorators can be used to add logging, caching, authentication, or any other type of behavior to functions. They are a powerful tool for adding functionality to code without modifying its source.


### How to go about debugging an issue using testing: 

   If any of the components fail during the integration test, there are several steps we can take to debug the issue. 
   Here are some general guidelines:
   
   1. Review the test output: When a test fails, the unittest module provides detailed output indicating which 
       assertions failed and what the expected and actual values were. Reviewing this output can help to identify the specific component that is failing and give you a clue about what might be causing the issue.
   2. Check the logs: If your components generate logs, review them to see if there are any errors or warnings 
       that could explain the issue. Logs can provide valuable information about what is happening inside each 
       component and can help to identify where the problem is occurring.
   3. Isolate the failing component: If you suspect that a specific component is causing the issue, try running 
       a standalone test for that component. This can help to isolate the problem and make it easier to debug.
   4. Use a debugger: Python provides a built-in debugger (pdb) that you can use to step through your code 
       and examine variables at each step. Using a debugger can help you to identify where your code is going 
       wrong and why.
   5. Add more logging: If you're still having trouble identifying the issue, consider adding additional logging 
       to your code to provide more information about what is happening. You can use Python's built-in logging 
       module to generate detailed logs that can help you to pinpoint the problem.
   
   Debugging integration issues can be challenging, but by following these guidelines and being systematic 
   in your approach, you can usually identify the root cause of the issue and fix it.

### Which frameworks have you used in python?**

### When do you use Flask vs Django?

###  `__init__` and `self` in python:

### You have a data of 500k records, how to you efficiently fetch it on a repeated basis and you cant return everything at once because browser cant handle huge data?
When dealing with large data sets, it's important to use some form of pagination or lazy loading to avoid overwhelming the browser with too much data at once. Here are some strategies you can use to efficiently fetch and display data from a large data set:

1.  Use server-side pagination: Instead of fetching all 500k records at once, you can fetch data in smaller chunks from the server. For example, you can fetch the first 100 records initially, and then load additional records as needed based on user actions (such as clicking on a "load more" button).
    
2.  Use client-side pagination: If you can't use server-side pagination for some reason, you can fetch all the data at once, but only display a smaller subset of records in the browser. You can use JavaScript to implement client-side pagination, which involves breaking the data into smaller chunks and displaying them on different pages. Users can then navigate between pages to view different parts of the data set.
    
3.  Use lazy loading: This is a technique where you only load data when it's needed, such as when the user scrolls down to view more records. You can use JavaScript to detect when the user reaches the bottom of the page and then load additional records from the server.
    
4.  Use caching: If the data set is relatively static (i.e., it doesn't change frequently), you can use caching to store the data in the browser or on the server. This can improve performance by reducing the number of network requests needed to fetch data.
    
5.  Use filtering and sorting: If the data set is large, it can be helpful to allow users to filter and sort the data based on specific criteria. This can help users find the information they need more quickly and reduce the amount of data that needs to be displayed at once.


### How do you do take care of CSRF in django and XSS in Flask?


