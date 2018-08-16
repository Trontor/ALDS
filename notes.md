# L02 - Algorithms

An algorithm is **a set of steps** to accomplish a task.

Computer algorithms must be:

* Specific
* Correct
* Reasonably efficient

## Example: *Fibonacci Numbers*

If we wish to compute the *n*'th number of the Fibonacci sequence, we do so with the following algorithm:

* F(n) = F (n-1) + F (n-2)
* Base Case: **F (1) = F(2) = 1** or **F (0) = 0**, **F(1) = 1**

If T(n) is the ***number of operations*** to calculate the ***n'th*** Fibonacci number, then 

* T(n) = T(n-1) + T(n-2) + 3
* The '3' comes from comparing if n == 0, then n == 1, then the summation of **F(n-1)** and **F(n-2)**

## Memoization

* Store previously computed values
* For example, if whenever we calculate F(n) we store it in an array at index *n* then anytime we need F(n) we can look it up in the array instead of re-calculating it
* This is trade off between space and time, as meoization is faster but it takes up more space

## Complexity Analysis: General Method

**Count operations** for T(n) "time" (number of ops) taken for input n

* It is best to identify the **most expensive operation** (i.e. drop anything that becomes insignificant)
* We can sometimes trade off *space* for *time*



# L03 - Complexity Analysis

We want to characterize the run time of **any** algorithm

* Identify the **most expensive operation**
* Count that operation
* Express in terms of input size n

## Big-O Definition

* For two functions *f(n)* and *g(n)*, we say that *f(n)* is *O(g(n))* if there are constants c and N such that f(n) \< c * g(n) for all n > N
* n^2 +33 is in O(n^2) because c = 2 and N= sqrt(33) then n^2+33 < 2n^2
* n^2 + 33n + 17 is in O(n^2)
  * Because c = 2, N = 34 and as such n^2 +33n + 17 < 2n^2 for all n > 34

## Big-O Arithmetic

* If a program is in stages:
  * Stage 1 operates on m inputs in **O(n)**
  * Then Stage 2 operates on n inputs in **O(m)**
  * The whole program is then 
    * **O(m)** + **O(n)** = **O(m+n)**
    * If m << n then just **O(n)**
* If the program operates on each of *n* inputs *m* times the program is **O(m*n)**

## Big-O Hierarchy

It should be memorized that n! >> 2^n >> n^3 >> n^2 >> n log n >> n >> log n >> 1

* Log base does not matter

### Big Omega Ω (Lower Bound) and Big Theta Ө (Growth Rate) 

For two function *f(n)* and *g(n)*, we say that *f(n)* is *Ω(g(n))* if there are constants c and N such that f(n) > c * g(n) for all n > N



# L04 - Data Structures 101

A lightning tour of fundamental data structures used for search.

## Abstract Data Types vs. Data Structures

* Abstract Data Types are things like stacks, queue, dictionary
  * Does not specify an implementation
* Concrete data structures
  * Array, linked list, tree
  * Implements an abstract data type

## Data Structures and Searching

* Organising data is important
* It is helpful to organise data **with the task in mind**

## malloc()

* malloc(size_t size)
* size_t is
  * An unsigned integer
  * Can be returned by the *sizeof* operator
  * Widely used in **stdlib** to represent sizes
  * *e.g.* malloc(sizeof(int))

```C
int A[NUMBER];
/**
 * while insertions < NUMBER array is OK
 * BUT… has a limit
 */
int* B;
/* always check return value of malloc()*/
if( (B = (int *) calloc( NUMBER * sizeof(int) )) == NULL )
{
 printf(“malloc() error\n”);
 exit(1);
}
/* B now comes with each slot initialized to 0 */
```



# L05 - Data Structures, *The Basics*

## Linked Lists

* Each item (*key*) is located in an arbitrary place in memory
* With a link (pointer) to the next item

### Search Operations

* If unsorted, finding an item in a linked list is still in Ө(n) time.
* Once an insertion point has been determined, it is easy to insert (or delete) a new item, by rearranging links.
* It takes extra space for each item in the list, and extra time to allocate the memory for the node for each item.

### The Node

```c
typedef struct node {
 record r; 
 struct node *next;
 } node_t;

typedef node_t* node_ptr;

node_ptr newnode;
```

###  Traversing the List

```c
p = listhead;
/* Check if list is empty */
if (p != NULL) {
    /* Check if there exists a next node */
    while (p -> next != NULL){
        /* Print node information */
        printf("%d\n", p->key);
        /* Move to next node */
        p = p -> next;
    }
    /* If there does not exist a next node, we reached the last node */
    printf("%d\n", p -> key);
}
```

### Inserting into the List

```C
/* First, you find a correct place in the list to insert the node */

/* Adjust the pointers, for a parent node q that points to p */
q -> next = newnode;
newnode -> next = p

```

### Deleting from the List

```c 
/* We want to delete p */
q -> next = p -> next;
/* Free memory used at address p */
free(p);
```

## Arrays vs Linked Lists

Sorted arrays have a **fast binary search** but **slow insertion** in order to keep it sorted.

Linked lists, we can't do binary search even if it is sorted, as we have to traverse through the whole list.

|                      | One Search | One Insert |
| -------------------- | :--------: | :--------: |
| Unsorted Array       |     n      |     1      |
| Sorted Array         |   log n    |     n      |
| Unsorted Linked List |     n      |     1      |
| Sorted Linked List   |     n      |     n      |

We can see that using a sorted linked list provides no gain.

# L06 - Binary Search Trees

*From [Wikipedia](https://en.wikipedia.org/wiki/Binary_search_tree)*

A **binary tree** is a [tree data structure](https://en.wikipedia.org/wiki/Tree_structure) in which each node has at most two [children](https://en.wikipedia.org/wiki/Child_node), which are referred to as the *left child* and the *right child*.

A binary **search** tree is a sorted binary tree where the left child of a node is \< than the node's value, and the right child of the node is \> the nodes value.

## Types

![Image result for types of binary trees](http://www.csie.ntnu.edu.tw/~u91029/BinaryTree2.png) 



| Type of Tree |                         Description                          |
| :----------: | :----------------------------------------------------------: |
|  Full Tree   |            Every node has either 0 or 2 children             |
|   Complete   | Every level is completely filled (except possibly the last)  |
|   Perfect    | All inner nodes have two children and all leaves have the same depth or same level |

 

## Best Case Run Time

* When it is *perfectly balanced*
* Height of tree with *n* items is at most the ceiling of *log_2(n)*
  * Ceiling means the upper value (ceiling of 2.5 is 3)
  * Quite simple: a perfectly balanced tree with 20 items will have a height of  5
* Insertion/search/deletion are all *O(log n)* for a well-balanced tree 

## Worst Case Run Time 

* The worst case run time occurs when items are inserted in a sorted order. 
* This makes the BST degenerate into a linked list
* The height of this tree of *n* items is *n*
* Insertion/search/deletion are all O(n), yikes!

Evidently, a balanced tree is preferred. 

# L07 - AVL Trees

A valiant attempt at getting a [binary search tree](#L06---Binary-Search-Trees) to stay balanced! 

*But why?* Most operations on a BST take time proportional to the height of the tree, so it is desirable to keep the height small. 

**The idea:** Make BST as close to [perfectly balanced](#Best Case Run Time) as possible.

There is overhead to this operation. With every insertion into a BST, a *rotation* may be performed to keep it balanced. As such, the Big O time complexity of insertion is:O(n log n).

However, search is guaranteed to be O(log n).

There are many balanced tree implementations, but we care only about **AVL Trees**.

## General Procedure

* Insert node in its appropriate location as you would to a regular BST.

* For each node, we can evaluate the *balance factor* for the node

  ##### Balance Factor

  Balance_Factor(N) = Height(Right_Subtree(N)) – Height(Left_Subtree(N)) 

* If the difference is > 1, then we balance using an operation called **rotation**

Note: A **binary tree** is an **AVL tree** as long as each node has a balance factor that is -1, 0 or 1

## Rotation

[Click here for a in-depth look at AVL Tree rotations](avl-tree-rotation.md)

