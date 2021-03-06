# Table of Contents
* [L02 - Algorithms](#l02---algorithms)
	* [Example: Fibonacci Numbers](#example-fibonacci-numbers)
	* [Memoization](#memoization)
	* [Complexity Analysis: General Method](#complexity-analysis-general-method)
* [L03 - Complexity Analysis](#l03---complexity-analysis)
	* [Big-O Definition](#big-o-definition)
	* [Big-O Arithmetic](#big-o-arithmetic)
	* [Big-O Hierarchy](#big-o-hierarchy)
	* [Big Omega Ω (Lower Bound)](#big-omega-Ω-lower-bound)
	* [Big Theta Ө (Growth Rate)](#big-theta-Ө-growth-rate)
* [L04 - Data Structures 101](#l04---data-structures-101)
	* [Abstract Data Types vs. Data Structures](#abstract-data-types-vs.-data-structures)
	* [Data Structures and Searching](#data-structures-and-searching)
	* [malloc()](#malloc)
* [L05 - Data Structures, The Basics](#l05---data-structures,-the-basics)
	* [Linked Lists](#linked-lists)
		* [Search Operations](#search-operations)
		* [The Node](#the-node)
		* [Traversing the List](#traversing-the-list)
		* [Inserting into the List](#inserting-into-the-list)
		* [Deleting from the List](#deleting-from-the-list)
	* [Arrays vs Linked Lists](#arrays-vs-linked-lists)
* [L06 - Binary Search Trees](#l06---binary-search-trees)
	* [Types](#types)
	* [Best Case Run Time](#best-case-run-time)
	* [Worst Case Run Time](#worst-case-run-time)
* [L07 - AVL Trees](#l07---avl-trees)
	* [General Procedure](#general-procedure)
	* [Rotation](#rotation)
* [L07/L08 - Deletion in BST](#l07/l08---deletion-in-bst)
	* [Tree Traversal](#tree-traversal)
	* [In-order Traversal](#in-order-traversal)
	* [Deleting an Item](#deleting-an-item)
		* [Node With Two Children](#node-with-two-children)
	* [Deletion Complexity Analysis](#deletion-complexity-analysis)
		* [Worst Case:](#worst-case)
		* [Average Case:](#average-case)
* [L09 - Multi-File Programming](#l09---multi-file-programming)
	* [Header Files](#header-files)
	* [Include](#include)
	* [Makefiles](#makefiles)
* [L09/10 - Distribution Counting](#l09/10---distribution-counting)
	* [Definition](#definition)
	* [Steps](#steps)
	* [Stable Sort?](#stable-sort?)
	* [Complexity and Example](#complexity-and-example)
		* [Task](#task)
		* [Count](#count)
		* [Cumulative Count](#cumulative-count)
		* [Redistribution](#redistribution)
* [L10/11 - Hash tables](#l10/11---hash-tables)
	* [Complexity](#complexity)
	* [Hash Function](#hash-function)
	* [Modulus and Prime Utilisation](#modulus-and-prime-utilisation)
	* [Hash Function for Strings](#hash-function-for-strings)
	* [Collisions](#collisions)
		* [Chaining](#chaining)
		* [Open Addressing](#open-addressing)
* [L11/12 - Selection/Insertion Sort](#l11/12---selection/insertion-sort)
	* [Selection Sort](#selection-sort)
	* [Insertion Sort](#insertion-sort)
* [L12 - Quicksort](#l12---quicksort)
	* [Quicksort: Basic idea](#quicksort-basic-idea)
* [L13 - Mergesort](#l13---mergesort)
	* [Procedure](#procedure)
	* [Merging](#merging)
	* [Recurrence Relation](#recurrence-relation)
	* [Bottom Up Mergesort](#bottom-up-mergesort)
* [L14 - Master Theorem](#l14---master-theorem)
	* [Divide and Sorting Algorithms](#divide-and-sorting-algorithms)
	* [Relationship Between a, b, d](#relationship-between-a,-b,-d)
* [L14/L15 - Priority Queues/Heaps](#l14/l15---priority-queues/heaps)
	* [Priority Queues](#priority-queues)
	* [Implementations](#implementations)
	* [Heap](#heap)
	* [Deleting The Max (Downheaping)](#deleting-the-max-downheaping)
	* [Downheaping](#downheaping)
	* [Upheaping](#upheaping)
	* [Complexity Comparison](#complexity-comparison)
	* [Heapsort](#heapsort)
* [L16 - Introduction to Graphs](#l16---introduction-to-graphs)
	* [What is a graph?](#what-is-a-graph?)
	* [Types of Graphs](#types-of-graphs)
		* [Undirected Graphs](#undirected-graphs)
		* [Directed Graphs](#directed-graphs)
	* [Reachability](#reachability)
		* [Bipartite Graph](#bipartite-graph)
		* [Completed Graph](#completed-graph)
	* [Trees](#trees)
	* [Representing Graph Vertices](#representing-graph-vertices)
	* [Array Representation](#array-representation)
	* [Adjacency List](#adjacency-list)
	* [Size Comparison](#size-comparison)
* [L17 - Traversing Trees and Graphs](#l17---traversing-trees-and-graphs)
	* [Traversal](#traversal)
	* [Graph Traversal vs Tree Traversal](#graph-traversal-vs-tree-traversal)
	* [Tree Traversal (BST, DFS, traversal DFS)](#tree-traversal-bst,-dfs,-traversal-dfs)
		* [Depth First Search](#depth-first-search)
		* [Breadth First Search](#breadth-first-search)
	* [Assumptions](#assumptions)
	* [Traversing an Unconnected Graph (DFS)](#traversing-an-unconnected-graph-dfs)
		* [Graph DFS Analysis](#graph-dfs-analysis)
	* [Breadth First Search](#breadth-first-search)
	* [Weighted Graphs](#weighted-graphs)
* [L18 - Shortest Paths](#l18---shortest-paths)
	* [Dijkstra’s Algorithm](#dijkstra’s-algorithm)
	* [Code using a Priority Queue](#code-using-a-priority-queue)
	* [Dijkstra's Algorithm Complexity Analysis](#dijkstras-algorithm-complexity-analysis)
	* [Limitations](#limitations)
	* [Single Source vs All Pairs](#single-source-vs-all-pairs)
		* [Using Dijkstra’s multiple times:](#using-dijkstra’s-multiple-times)
* [L19 - All Pairs (Floyd-Warshall)](#l19---all-pairs-floyd-warshall)
	* [Transitive Closure](#transitive-closure)
	* [Warshall Algorithm](#warshall-algorithm)
	* [Warshall Algorithm Analysis](#warshall-algorithm-analysis)
	* [Floyd-Warshall Algorithm](#floyd-warshall-algorithm)
	* [Notes on the Floyd-Warshall Algorithm](#notes-on-the-floyd-warshall-algorithm)
	* [Big Assumptions](#big-assumptions)
		* [Johnson's Algorithm](#johnsons-algorithm)
* [L20 - Kruskal's Algorithm for MST](#l20---kruskals-algorithm-for-mst)
	* [Greedy Algorithms](#greedy-algorithms)
	* [Spanning Tree](#spanning-tree)
	* [Minimum Spanning Trees](#minimum-spanning-trees)
	* [Why minimum spanning trees?](#why-minimum-spanning-trees?)
	* [Kruskal's Algorithm](#kruskals-algorithm)
	* [Kruskal's Algorithm Analysis](#kruskals-algorithm-analysis)
	* [Union-Find/Disjoint-Set Data Structure](#union-find/disjoint-set-data-structure)
		* [What is a disjoint set?](#what-is-a-disjoint-set?)
		* [Union-Find Algorithms](#union-find-algorithms)
		* [Array-based Union Find](#array-based-union-find)
	* [Application to Kruskal's Algorithm](#application-to-kruskals-algorithm)
* [L21 - Prim's Algorithm](#l21---prims-algorithm)
* [L22 - Topological Sorting (Toposort)](#l22---topological-sorting-toposort)
	* [What is toposort?](#what-is-toposort?)
	* [Topological Sorting Algorithm Overview](#topological-sorting-algorithm-overview)
	* [Toposort Example](#toposort-example)
	* [Toposort Assumptions](#toposort-assumptions)
# L02 - Algorithms
[← Return to Index](#table-of-contents)


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
[← Return to Index](#table-of-contents)


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

## Big Omega Ω (Lower Bound) 

For two function *f(n)* and *g(n)*, we say that *f(n)* is *Ω(g(n))* if there are constants c and N such that f(n) > c * g(n) for all n > N

## Big Theta Ө (Growth Rate) 

For two functions *f(n)* and *g(n)* if there exists three constants c, d, N > 0 such that:

` c * g(n) >= f(n) >= d*g(n) for all n > N `

 then f(n) is in Ө(g(n))

# L04 - Data Structures 101
[← Return to Index](#table-of-contents)


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
[← Return to Index](#table-of-contents)


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
[← Return to Index](#table-of-contents)


*From [Wikipedia](https://en.wikipedia.org/wiki/Binary_search_tree)*

A **binary tree** is a [tree data structure](https://en.wikipedia.org/wiki/Tree_structure) in which each node has at most two [children](https://en.wikipedia.org/wiki/Child_node), which are referred to as the *left child* and the *right child*.

A binary **search** tree is a sorted binary tree where the left child of a node is \<= than the node's value, and the right child of the node is \> the nodes value.

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
[← Return to Index](#table-of-contents)


A valiant attempt at getting a [binary search tree](#l06---binary-search-trees) to stay balanced! 

*But why?* Most operations on a BST take time proportional to the height of the tree, so it is desirable to keep the height small. 

**The idea:** Make BST as close to [perfectly balanced](#best-case-run-time) as possible.

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

[A highly suggested 'click here' for an in-depth look at AVL Tree rotations](avl-tree-rotation.pdf)

The general idea:

* Single rotation if the balance factor signs match
  * For a left heavy tree, do a right rotation
  * For a right heavy tree, do a left rotation
* Double rotation if the balance factor signs do not match
  * For a left heavy tree, do a left rotation on the left subtree, then a right rotation on the root tree
  * For a right heavy tree, do a right rotation on the right subtree, then a left rotation on the root tree 

Rotations are not specific to AVL trees, and appear in other implementations of data structures.

Overall, it is important to remember we are working with [**binary search trees**](#l06---binary-search-trees), which means any rotation must result in a tree which is a valid binary search tree, that is: all node values to the right of a node are greater than the current node value, and vice versa for the nodes to the left.

# L07/L08 - Deletion in BST
[← Return to Index](#table-of-contents)


*Not useful for assignment, but is **tested in exam!***

Deletion from a tree is not as simple as deleting from an array or list. If we delete something, we have to identify what node to substitute it with.

## Tree Traversal

* Visit every node once
* Do something during the visit to the node:
  * Print the node value, or
  * Mark the node as visited, or
  * Check some property of the node

Not specific to trees, as we can also traverse graphs and lists. Thankfully, traversing trees are easier than graphs, as trees are not cyclical (no node points to a parent node).

Example tree:

![Tree](https://i.imgur.com/trNKjd2.png)

**Post-order Traversal**
*Left, Right, Visit*

```C
traverse(t->left);
visit(t);
traverse(t->right);
```

G, F, K, J, Q, S, P, M

You use this to free the nodes of the tree! **You cannot free a tree by just freeing the root**, because the memory addresses to other nodes still exist.

**Pre-order Traversal**
*Visit, Left, Right*

``` 
visit(t);
traverse(t->left);
traverse(t->right);
```

M, J, F, G, K, P, S, Q

## In-order Traversal

*Left, Visit, Right*

F, G, J, K, M, P, Q, S

```C
void traverse(struct node *t)
{
    if(t != NULL)
    {
        traverse(t->left);
        visit(t);
        traverse(t->right);
    }
}
```

## Deleting an Item

* Step 1: Find node to delete
* Step 2: Delete it
  * Case 1: Node is a leaf (no children)
    * Just delete it, ez
  * Case 2: Node has either a left **or** right child, ***not both***
    * Replace with the left or right child respectively
  * Case 3: Node has both a left child **and** a right child!
    * This requires some analysis

### Node With Two Children

Referring back to this example:

![Tree](https://i.imgur.com/trNKjd2.png)

The nodes with two children here are **M** and **J**.

If we want to delete **J**, we have two candidates (inner-most predecessor/successor) which are **K** and **G**. It doesn't matter what one is chosen. We replace **J** with **K** or **G** and still preserve the BST.

If we want to delete **M** our ideal candidates are **K** (inner most predecessor) or **P** (inner-most successor). **K** has no children and as such is a technically better candidate.

**In general, just replace it with the innermost successor (minimum value of right subtree)**

## Deletion Complexity Analysis

### Worst Case: 

* Time to find node is *O(n)*
* Time to find in-order predecessor or successor is *O(n)*
* Total time: *O(2n) = O(n)*

### Average Case:

* Time to find node is *O(log n)*
* Time to find in-order predecessor or successor is *O(log n)* if we specify one, otherwise it is *O(n)*
* Total time is therefore *O(log n)* or *O(n)*

# L09 - Multi-File Programming
[← Return to Index](#table-of-contents)


## Header Files

Just like libraries in C# and Python. 

It is a **.h** file that includes declarations and macro definitions to be shared amongst other source files.

## Include

```C
/* Include file from system path for /include */
#include <file>
/* Include custom file of your own program*/
#include "file.h"
```

The include directive works by telling the C preprocessor to read the specified files before the rest of the current file.

## Makefiles

*[This is a good tutorial, and covers some extra makefile topics too.](http://www.cs.colby.edu/maxwell/courses/tutorials/maketutor/)*

* Simplifies compilation of multiple files

Take these three files for example:

**hello.c**

``` C
#include <hellomake.h>
int main() {
  // call a function in another file
  myPrintHelloMake();
  return(0);
}
```

**hellofunc.c** (function definitions)

```c
#include <stdio.h>
#include <hellomake.h>

/* Uses prototype from header file */
void myPrintHelloMake() {
  printf("Hello makefiles!\n");
  return;
}
```

**hellomake.h** (function declarations)

```c
void myPrintHelloMake(void);
```

Normally you would compile this with `gcc -o hellomake hellomake.c hellofunc.c`

> Unfortunately, this approach to compilation has two downfalls. First, if you lose the compile command or switch computers you have to retype it from scratch, which is inefficient at best. Second, if you are only making changes to one .c file, recompiling all of them every time is also time-consuming and inefficient. So, it's time to see what we can do with a makefile. 

The simplest makefile you could create looks like this:

```makefile
hellomake: hellomake.c hellofunc.c
     gcc -o hellomake hellomake.c hellofunc.c
```

The first line let's the compiler know that if **`hellomake.c`** or **`hellofunc.c`** change then to recompile them.

You can see in the second line, there is a tab before the gcc command. There must be a tab before any command or `make` won't be happy

# L09/10 - Distribution Counting
[← Return to Index](#table-of-contents)


## Definition

A sorting algorithm that stores, for each `sortkey`, the number of records with the given `sortkey` (thus anticipating that keys might not be unique). With this information it is possible to place the records correctly into a sorted file. The algorithm is useful when the keys fall into a small range and many of them are equal.

## Steps

- **Input**: *an array of:*

  - Records

    or

  - Keys + Pointers to Records

- **Count** number of records associated with each key value (lower to upper)

- **Redistribute** array elements

- Output: Stable Sorted Array

## Stable Sort?

If we have elements ***R*** and ***S*** (in that order) with the same key and apply a sorting algorithm to it, it is considered a stable sort if ***R*** appears before ***S*** in the sorted array. Because they have the same key, it is easy to switch them up. Stable sorting algorithms preserve the order of elements with the same key.

## Complexity and Example

### Task

Sort `[ 4, 4, 2, 2, 0, 2, 1, 3, 2, 4, 3, 1, 4, 3, 1, 4]` 

### Count

Count the number of records associated with each key value (lower to upper)

Key **0** occurs **1** time

0->1

1->3

2->4

3->3

4->5

To perform this, we traverse this in **O(n)** worst case as a more effective way to do this for a computer is to go through go through once and increment the `counting` array at index `n` as we progress through the input array.

### Cumulative Count

The cumulative count is an array that stores at index `i` the number of elements from the input that is less than `i`

`cumulativeCount = [0, 1, 4, 8, 11]` (0 elements less than 0, 1 element less than 1, etc.)

### Redistribution

We traverse the original input array, and copy each item to its new position as follows

```C 
aux_array[cumulativeCount[item.key]] = item
cumulativeCount[item.key] += 1
```

# L10/11 - Hash tables
[← Return to Index](#table-of-contents)


This is a data structure that provides a means of accessing a desired item directly. For a hash table:

## Complexity

- Search is **O(1)** average case
  - If the hash table is managed well

However, the worst case is **O(n)**. 

## Hash Function

The hash table is an array/dictionary who's index is the result of a hash function. 

![](images/hash.png)

## Modulus and Prime Utilisation

The number of keys that can be output by the hash table is often not known but it can be squished into an array using the modulo operator. You should always use a **prime number** to multiply and as the right hand side term of the modulo command.

`hash(key) = (key * BIGPRIME ) % prime`

## Hash Function for Strings

Use a base mapping **power of 2** 	like so:

If we want to map **c a t** we map it like so:

` H("cat") = 32^2 * 3 + 32 * 1 + 32^0 + 20`

Because **c = 3**, **a = 1**, and **t = 20**

## Collisions

When two keys map to the same array index. Good hash functions have fewer collisions, but we can never assume there will be none.

### Chaining

Add to the end of the linked list at the array entry.

```C
void insert( HT, item )
{
     new newnode = /* ... make a list node */
    /* put --item-- in the list node */
     index = hash(item->key);
    if( HT[ index ] == NULL)
     	HT[ index ] = newnode;
    else
    {
         newnode->next = HT[ index ]->node;
         HT[ index ] = newnode;
    }
}
```

### Open Addressing

##### Linear Probing

If there is a collision, put the item in the next available slot. Catastrophic failure when table full, also clustering can occur easily.

##### Double Hashing

Choose a second hash function.

##### Load Factor **α**

For **n** keys in **m** cells

- α = n/m

Average case, under some simplifying assumptions, expected time for insertion is:

- Double hashing: **1/(1-α)** 
- Linear probing: **1/(1-α)^2**

Example: **α = 0.75**

- Double hash insertion: 4 probes
- Linear probing insertion: 16 probes

Hash tables show fast lookup

# L11/12 - Selection/Insertion Sort
[← Return to Index](#table-of-contents)


Sorting has many applications and is used widely. The two most naïve sorting algorithms are **selection sort** and **insertion sort**.

## Selection Sort

Select the lowest element and swap it with the first unsorted element

- In place
- Worst case **O(n^2)**
- Best case **O(n^2)**
- Average case **O(n^2)**

```C
void selection(item* A, int n)
{
    int i,j,min;
    for (i = 0; i < n-1; i++) { /* why n-1? */ 
        min = i;
        for( j = i+1; j < n; j++ ) {
            if (cmp( A[j], A[min] ) < 0) 
                min = j;
        }
        SWAP( A[i], A[min] );
    }
}
```

## Insertion Sort

Iterate through the list and move each element to the appropriate spot in the array.

- In place
- Stable
- Worst case **O(n^2)**
- Best case **O(n)** (already sorted)
- Average case **O(n^2)**

For example:

![](images/insertionsort.gif)

```C
void insertionsort()
{ 
    int i, j;
 	for (i = 1; i < n; i++)
        for (j = i; j > 0 && x[j-1] > x[j]; j--)
            swap(j-1, j);
}
```

Usefulness of insertion sort: almost sorted files; or small files

# L12 - Quicksort
[← Return to Index](#table-of-contents)


A divide-and-conquer sorting algorithm.

## Quicksort: Basic idea

- **Partition array:**
  - Pick a pivot point
  - Make everything larger than the pivot has a higher index
  - Make everything smaller than the pivot has a smaller index

- **Recursion**:

  - Partition the left half of the array recursively
  - Partition the right half of the array recursively

  ```C
  int partition(item A[],int l,int r);
  void quicksort(item A[], int l, int r)
  {
      int i;
      if (r <= l) return;
      i = partition(A,l,r);
      quicksort(A,l,i-1);
      quicksort(A,i+1,r);
  }
  ```

  This is conceptually simple, but partitioning is quite tricky.

  ```c
  int partition(item A[], int l, int r)
  {
      int i = l-1, j = r;
      item v = A[r];
      while( 1 )
      {
          while (less(A[++i], v) /* do nothing */ ;
          while (less(v, A[--j]) /* do nothing */;
                        if(i>=j) break;
                        swap(A[i],A[j]);
  	}
      swap(A[i],A[r]);
      return(i);
  }	
  ```

- In place

- Unstable (for efficient implementations)

- Worst case performance: **O(n^2)**

- Best case performance: **O(n log n)**

- Average performance: **O(n log n)**

# L13 - Mergesort
[← Return to Index](#table-of-contents)


![](images/mergesort.gif)

Merge Sort is a **divide and conquer algorithm**. It works by **recursively** breaking down a problem into two or more sub-problems of the same or related type, until these become simple enough to be solved directly. The solutions to the sub-problems are then combined to give a solution to the original problem. 

So Merge Sort first divides the array into equal halves and then combines them in a sorted manner.

- In place
- Unstable (for efficient implementations)

- Worst case: **O(n log n)** *(divide and conquer)*
- Best case: **O(n log n)**
- Average Case: **O(n)**

## Procedure

1. Divide the unsorted list into *n* sublists, each containing 1 element (a list of 1 element is considered sorted).
2. Repeatedly [merge](https://en.wikipedia.org/wiki/Merge_algorithm) sublists to produce new sorted sublists until there is only 1 sublist remaining. This will be the sorted list.

## Merging

Merging is the tricky part, given two arrays we do the following:

- Begin with two pointers that point to the start of the two arrays respectively.
- Compare those pointers
- Whoever has the smallest, we put that in the new merged array at index *k* (=0 initially)
- Increment the pointer of the array that had the smallest element
- Repeat until all pointers go to the end of their arrays

## Recurrence Relation

C(n) = 2 * C(n/2) + n - 1

	= 2 [ 2 * C(n/4) + (n/2 - 1)] + n - 1
	
	--- log_2(n) splits

C(n)	= 2^(log_n) + n + n + n + ... log n times ... + n

## Bottom Up Mergesort

So far, we've looked at top down (recursive) mergesort. Bottom up mergesort 

# L14 - Master Theorem
[← Return to Index](#table-of-contents)


Don't have to remember the equations. If a question were to be asked on this topic, equations would be given and the application of them will be tested.

## Divide and Sorting Algorithms

Recurrence relations:

One pass through the data reduces problem size by half. Process both halves:

- ***Operation*** takes constant time **c**

- ***Base case*** takes time **d**

  T(1) = d

  T(n) = 2*T(n/2) + nc

  	= nc + 2cn/2 + 4cn/4... + n/2*2c + nd

  T(n)	= c(n-1)*log_n + nd

- Most common cases:

  **T(n) = 2*T(n/2) + n**

- General case:

  **T(n) = a*T(n/b) + f(n)**

  Where f(n) ∈ Θ(n^d)

  a = number of sub-problems

  b = size of subproblems

  d = how much work to be done for each element

- Most common case:

  T(n) = 2*T(n/2) + n

  **a = 2**, **b = 2**, **d = 1**

## Relationship Between a, b, d

Recall: 

- a = number of sub problems
- b = size of subproblems
- d = how much work to be done for each element

We can determine the complexity using this logic:

- d > log_b(a) then => T(n) ∈ Θ( n^d )
- d = log_b(a) then => T(n) ∈ Θ( n^d * log(n) )
- d < log_b(a) then => T(n) ∈ Θ( n^(d*log_b(n)) )

# L14/L15 - Priority Queues/Heaps
[← Return to Index](#table-of-contents)


## Priority Queues

Introduction into graphing, as graphing algorithms rely deeply on priority queues. 

> A **priority queue** is an [abstract data type](https://en.wikipedia.org/wiki/Abstract_data_type) which is like a regular [queue](https://en.wikipedia.org/wiki/Queue_(abstract_data_type)) or [stack](https://en.wikipedia.org/wiki/Stack_(abstract_data_type)) data structure, but where additionally each element has a "priority" associated with it.

[From Wikipedia](https://en.wikipedia.org/wiki/Priority_queue)

A priority queue has the following operations:

```C
makePQ(); // Makes the priority queue
enqueue(PQ, item); // Adds an item to the priority queue
deletemax(PQ); // or deletemin()
emptyPQ(); // Empties all of the queue
changeWeight(PQ, item); // Changes the priority attached to an item
```

## Implementations

#### Array

- Unsorted array of ***n*** items
  - Construction: ***O(n)***
  - Get highest priority: ***O(n)***
- Sorted array of N items:
  - Construct: ***O(n^2)*** (depends on implementation)
  - Get highest priority: ***O(1)***

#### List

- Unsorted list:
  - Construct: ***O(n)***
  - Get highest priority: ***O(n)***
- Sorted List
  - Construct: ***O(n^2)***
  - Get highest priority: ***O(1)***

Arrays are evidently superior as they allow random access.

## Heap

A heap is a:

- Complete tree
  - Balanced
- Every node satisfies the "heap condition":
  - parent->key **>=** child->key, for all children
  - **Root is therefore the maximum** 

![](images/heap.png)

This heap can be represented as an array:

![](images\heaparray.png)

- **Parent** = i, value = A[i]
- **Children of Parent** = A[parent * 2] and A[parent * 2 + 1]

## Deleting The Max (Downheaping)

1. Return the highest priority item (**root**)

2. Fix the heap
   - Put last item into the root position (For example, replace X with I in the example array above)
   - Reduce the size of PQ by one
   - Fix the heap condition for the root `downheap()`

## Downheaping

- Compare the new root to the value of its immediate children. 
- Swap the root with a child if the child is greater than the root. 
- Keep doing this as you proceed down the tree. 
- Stop when there are no children or all children are less than the value of the parent

```C
downheap(int[] PQ, int k)
{
     int j,v;
     v = PQ[k]; /* value, or priority */
     while( k <= n/2 ) /* A[k] has children */
     {
         /* point to children*/
         j= k*2;
         /* j set to highest child*/
         if(j<n && PQ[j]< PQ[j+1]) j++;
         if (v>= PQ[j]) break; /* check heap OK */
         PQ[k] = PQ[j]; k = j; /* swap and continue */
     }
     /* final position of original A[k] value*/
     PQ[k] = v;
}
```

## Upheaping

This is the opposite of downheaping where we want to insert into the heap:

```C
void upheap(int* PQ, int k)
{
    int v;
    v = PQ[k];
    PQ[0] = INT_MAX; /* sentinel, limits.h */
    while(PQ[k/2] <= v){ /* note integer arith */
        PQ[k] = PQ[k/2];
        k = k/2;	
    }
    PQ[k] = v;
}
```

## Complexity Comparison

Finding Max = O(1)

Deleting Max = O(log n)

Inserting = O(log n)

## Heapsort

The *heap* suggests a method for sorting:

- Construct the heap
- Swap the root (max) with the last element
- Remove the last element from further consideration (decrease heap size by 1)
- Fix heap using `downheap` ***O(log n)*** 

# L16 - Introduction to Graphs
[← Return to Index](#table-of-contents)


## What is a graph?

- A representation of a set of objects
- Some pairs of objects are connected by links

- Set of vertices **V** and edges **E** that connect objects
- **Vertices** can contain information, while **edges** can have direction and/or weight.
  - Comparing this with trees and linked lists, vertices are like nodes and edges are the links

## Types of Graphs

### Undirected Graphs
![](images/undirectedgraph.png)

Edges have no direction specified

#### Connected

- Every pair of vertices is connected (possibly indirectly)

#### Unconnected

- One or more vertices cannot be accessed from another one or more vertices

### Directed Graphs

Edge direction is specified

##### Acyclic, Unconnected Directed Graph

![](images/dag.png)=

## Reachability
[← Return to Index](#table-of-contents)


Can you get from vertex A to vertex B?

#### Weakly Connected Directed Graph

If only some vertices are reachable 

![](images/weakconnected.png)

#### Strongly Connected Directed Graph

Each vertex is reachable from every other vertex

### Bipartite Graph

![](images/bipartitegraph.png)

- **U** and **V** are disjoint sets of vertexes
- Every vertex in **U** connects to a vertex in **V** and vice versa

### Completed Graph

![](images/completegraph.png)

- A complete graph has `V(V-1)/2` edges

## Trees

Trees are simply an undirected graph that is connected and acyclic. Any two vertices are connected by one simple path.

## Representing Graph Vertices

## Array Representation

![](images/arrayrepresentationgraph.png)

## Adjacency List

![](images/adjacencylistrepresentationgraph.png)

## Size Comparison

The size of a array (matrix) representation is: ***O(V^2)***

The size of an adjacency list representation is: ***O(V+E)***

# L17 - Traversing Trees and Graphs
[← Return to Index](#table-of-contents)


## Traversal

- **Traverse**: to pass or move over, along, or through
- **Tree traversal:** the process of visiting (examining or updating) each node exactly once, in a systematic way
- **Graph traversal:** the process of visiting all the nodes in a graph

## Graph Traversal vs Tree Traversal

Graph traversal complications due to:

- Possible cycles
- Not necessarily connected

## Tree Traversal (BST, DFS, traversal DFS)

The depth first search looks for the deepest node when searching.

### Depth First Search

Depth-first tree search can be done as:

- In order
- Pre order
- Post order

### Breadth First Search

The obvious complement to depth first search (choose shallowest children)

## Assumptions

- Assumes every node is reachable from the root
- Assumes every node has only one parent, can only be visited once

However, graph traversal needs to make sure that:

- Every node is reached
- Every node is visited only once
- No cycles, so you need to mark nodes as visited!

## Traversing an Unconnected Graph (DFS)

- Need to traverse each connected component
- Still need to mark nodes as visited

Take this graph for example:

![Unconnected Graph DFS](images/unconnecteddfs.png)

It can be represented as either an adjacency list or matrix representation. We will use the adjacency list for this question.

In code, this can be represented using a linked list:

```C
/* adjacency list is an array of pointers to nodes; node is struct with value (nodeID)
and next ptr*/
struct node{
    int value;
	struct node *next;
};
struct node* adj[V];
```

Now we need to visit the notes, and update an array to track where we've visited.

```C
int visited[V];
int order=0; /*keeps track of the order in
 which nodes are visited */
void visitDFS(int k)
{
    struct node* t;
    visited[k] = ++order;
    for(t = adj[k]; t != NULL; t = t->next){
        if( !visited[t->v] )
            visitDFS( t->v );
    }
}
```

### Graph DFS Analysis

- Fill in the visited array: **|V|**
- Examine (at most) each edge twice: **|E|**
- Overall: **|V|** + **|E|**

## Breadth First Search

We need to make sure:

- Every node is visited, even if the graph is not connected,
- Every node is visited only once

```C
int visited[V]; int order=0;
void visitBFS(int k){
    struct node* t;
    enQ(Q,k);
    while(!Qempty(Q)){
        k = deQ(Q);
        if( !visited[k] ){
            visited[k] = ++order;
            for(t = adj[k]; t != NULL; t = t->next){
                if( !visited[t->num] )
                    enQ(Q,t->num);
            }
        }
    }
}
```

## Weighted Graphs

So far, we used arbitrary ordering of the connected nodes (determined by position in adjacency list or matrix). If we have a weighted graph, with each edge telling us information about that path taken to the next node, we can make better informed decisions. 

# L18 - Shortest Paths
[← Return to Index](#table-of-contents)


![Weighted Graph](images/weightedgraph.png)

Given: 

- Directed graph **G(V, E)**
- Source vertex `s` in `V` 
- Determine: Shortest distance path from `s` to every other vertex in `V`

The brute force approach (calculating all paths from `a` to `b`) is not feasible. For a graph with 20 nodes, there are 20! possibilities to traverse.

## Dijkstra’s Algorithm 

Given a graph and a source vertex in the graph, find shortest paths from source to all vertices in the given graph. Below are the detailed steps used in Dijkstra’s algorithm to find the shortest path from a single source vertex to all other vertices in the given graph. 

Algorithm

1. Create a set `sptSet` (shortest path tree set) that keeps track of vertices included in shortest path tree, i.e., whose minimum distance from source is calculated and finalized. Initially, this set is empty.
2. Assign a distance value to all vertices in the input graph. Initialize all distance values as INFINITE. Assign distance value as 0 for the source vertex so that it is picked first.
3. While `sptSet` does not include all vertices:
   a) Pick a vertex `u` which is not in `sptSet` and has a minimum distance value. 
   b) Include `u` to `sptSet`
   c) Update distance value of all adjacent vertices of `u`. To update the distance values, iterate through all adjacent vertices. For every adjacent vertex `v`, if sum of distance value of `u` (from source) and weight of edge `u-v`, is less than the distance value of `v`, then update the distance value of `v`.

See example [here](https://www.geeksforgeeks.org/dijkstras-shortest-path-algorithm-greedy-algo-7/)

## Code using a Priority Queue

```C
void run(int** G, int Vsize, int s, int* pred, int* dist)
{
    pq_node_t* pq; /********** Assuming PQ is a minheap */
    int u, v;
    pq = makePQ(G); /************************** big-O(V) */
    while( !emptyPQ(pq) ) /************************** big-O(V) */
    {
        u = deletemin(pq); /******************* big-O(log V) */
        for(/*each v conneted to u */)
            if(dist[u] + edgeweight(u,v) < dist[v])
                update(v, pred, dist, pq); /***** big-O(log V) */
        /************ big-O(E) for for loop */
    }
}
```

## Dijkstra's Algorithm Complexity Analysis

Using the complexities in the code: total is **O((V+E) log V)**

## Limitations

- Assumes no negative edges

## Single Source vs All Pairs

What has been shown is an algorithm that can calculate the shortest path from a given node to a destination node. However, what if we want to find the shortest path from every other node? 

### Using Dijkstra’s multiple times:

Dijkstra’s algorithm: **O((V+E) log V)**

Once for every vertex: O((V^2+VE) log V)

Dense graphs have a lot of edges close to the number of vertices: making '**all pairs**' calculation **O(V^3 log V)** for dense graphs

We can do better.

# L19 - All Pairs (Floyd-Warshall)
[← Return to Index](#table-of-contents)


## Transitive Closure

We begin this topic on the basis of ***transitive closure***. The [definition](https://www.geeksforgeeks.org/transitive-closure-of-a-graph/) of this is: Given a directed graph, find out if a vertex `j` is reachable from another vertex `i` for all vertex pairs (`i`, `j`) in the given graph. 

![Transitive Easy Example](images/transitive1.png)

Take for example the following graph:

![Transitive Lecture Example](images/transitiveexample.png)

This can be represented in the following matrix representation:

|       |  0   |  1   |  2   |  3   |  4   |  5   |  6   |
| :---: | :--: | :--: | :--: | :--: | :--: | :--: | :--: |
| **0** |  0   |  1   |  0   |  0   |  0   |  0   |  0   |
| **1** |  0   |  0   |  0   |  0   |  0   |  0   |  0   |
| **2** |  0   |  0   |  0   |  1   |  0   |  0   |  0   |
| **3** |  0   |  0   |  0   |  0   |  1   |  0   |  0   |
| **4** |  0   |  0   |  0   |  0   |  0   |  0   |  0   |
| **5** |  0   |  0   |  0   |  0   |  1   |  0   |  0   |
| **6** |  0   |  0   |  0   |  0   |  0   |  1   |  0   |

*The **left** side denotes the ''from" nodes, while the **right** side denotes the "to" node*

If we look back at the graph, we can see that there is a path from node `6` to node `4` (through 5). There is also a final extra path from `2` to `4`.

To achieve transitive closure, our matrix representation should look like so (changes in bold):

|       |  0   |  1   |  2   |  3   |   4   |  5   |  6   |
| :---: | :--: | :--: | :--: | :--: | :---: | :--: | :--: |
| **0** |  0   |  1   |  0   |  0   |   0   |  0   |  0   |
| **1** |  0   |  0   |  0   |  0   |   0   |  0   |  0   |
| **2** |  0   |  0   |  0   |  1   | **1** |  0   |  0   |
| **3** |  0   |  0   |  0   |  0   |   1   |  0   |  0   |
| **4** |  0   |  0   |  0   |  0   |   0   |  0   |  0   |
| **5** |  0   |  0   |  0   |  0   |   1   |  0   |  0   |
| **6** |  0   |  0   |  0   |  0   | **1** |  1   |  0   |

## Warshall Algorithm

There exists an algorithm to achieve transitive closure, known as the Warshall Algorithm.

```C
/* intermediate nodes */
for( i=0; i < V; i++)
    /* from nodes */
    for( s=0; s < V; s++)
        /* to nodes */
        for( t=0; t < V; t++)
            if( A[s][i] && A[i][t])
                A[s][t] = TRUE; /* TRUE == 1 */
```

## Warshall Algorithm Analysis

- **O(V^3)**

## Floyd-Warshall Algorithm

The Floyd Warshall Algorithm is for solving the All Pairs Shortest Path problem. The problem is to find shortest distances between every pair of vertices in a given edge weighted directed Graph.

```C
// Solves the all-pairs shortest path problem using Floyd Warshall algorithm 
void floydWarshall (int graph[][V]) 
{ 
    /* dist[][] will be the output matrix that will finally have the shortest  
      distances between every pair of vertices */
    int dist[V][V], i, j, k; 
  
    /* Initialize the solution matrix same as input graph matrix. Or  
       we can say the initial values of shortest distances are based 
       on shortest paths considering no intermediate vertex. */
    for (i = 0; i < V; i++) 
        for (j = 0; j < V; j++) 
            dist[i][j] = graph[i][j]; 
  
    /* Add all vertices one by one to the set of intermediate vertices. 
      ---> Before start of an iteration, we have shortest distances between all 
      pairs of vertices such that the shortest distances consider only the 
      vertices in set {0, 1, 2, .. k-1} as intermediate vertices. 
      ----> After the end of an iteration, vertex no. k is added to the set of 
      intermediate vertices and the set becomes {0, 1, 2, .. k} */
    for (k = 0; k < V; k++) 
    { 
        // Pick all vertices as source one by one 
        for (i = 0; i < V; i++) 
        { 
            // Pick all vertices as destination for the 
            // above picked source 
            for (j = 0; j < V; j++) 
            { 
                // If vertex k is on the shortest path from 
                // i to j, then update the value of dist[i][j] 
                if (dist[i][k] + dist[k][j] < dist[i][j]) 
                    dist[i][j] = dist[i][k] + dist[k][j]; 
            } 
        } 
    }  
    // Print the shortest distance matrix 
    printSolution(dist); 
} 
```

## Notes on the Floyd-Warshall Algorithm

- Gives the distance of the shortest path for all vertices
- Does not establish the actual paths
- Path information can be obtained through a small addition to the code:
  - For each update to distance array, update path array to save: node that made the path shorter 

## Big Assumptions

For sparse graphs, adjacency list representation, use Johnson’s algorithm

### Johnson's Algorithm

- Run Dijkstra’s single source algorithm for each vertex
- Use Fibonacci heap for priority queue

Not that important for exam I think?

# L20 - Kruskal's Algorithm for MST
[← Return to Index](#table-of-contents)


## Greedy Algorithms

Greedy algorithms are used in optimization problems. They work on the assumption that the global optimal solution can be found by choosing the local optimal solution for each step. 

- Dijkstra’s algorithm is greedy: takes the next best edge to add to the path tree

## Spanning Tree

[Source](https://www.ics.uci.edu/~eppstein/161/960206.html)

A *spanning tree* of a graph is just a subgraph that contains all the vertices and is a tree. A graph may have many spanning trees; for instance the complete graph on four vertices.

Take this graph for example:

```asciiarmor
   	o---o
    |\ /|
    | X |
    |/ \|
    o---o
```

This graph has sixteen spanning trees:

has sixteen spanning trees:

```asciiarmor
    o---o    o---o    o   o    o---o
    |   |    |        |   |        |
    |   |    |        |   |        |
    |   |    |        |   |        |
    o   o    o---o    o---o    o---o

    o---o    o   o    o   o    o   o
     \ /     |\ /      \ /      \ /|
      X      | X        X        X |
     / \     |/ \      / \      / \|
    o   o    o   o    o---o    o   o

    o   o    o---o    o   o    o---o
    |\  |       /     |  /|     \
    | \ |      /      | / |      \
    |  \|     /       |/  |       \
    o   o    o---o    o   o    o---o

    o---o    o   o    o   o    o---o
    |\       |  /      \  |       /|
    | \      | /        \ |      / |
    |  \     |/          \|     /  |
    o   o    o---o    o---o    o   o
```

## Minimum Spanning Trees

Now we consider the original graph having weights/lengths for edges, a problem can now be developed:

**How to find the spanning tree with a minimum length?**

## Why minimum spanning trees?

The standard application is to a problem like phone network design. You have a business with several offices; you want to lease phone lines to connect them up with each other; and the phone company charges different amounts of money to connect different pairs of cities. You want a set of lines that connects all your offices with a minimum total cost. It should be a spanning tree, since if a network isn't a tree you can always remove some edges and save money.

## Kruskal's Algorithm

- Sort the edges of the graph in increasing order by length.
- Keep an empty subgraph
- For each edge `e` in sorted order
  - If the endpoints of `e` are disconnected in the subgraph
    - add `e` to the subgraph
- Return the subgraph

## Kruskal's Algorithm Analysis

The crux of the processing time goes into sorting the edge list. This can be done using mergesort/quicksort in O(E log E).

## Union-Find/Disjoint-Set Data Structure

[Source](https://www.geeksforgeeks.org/union-find/)

### What is a disjoint set?

A *disjoint-set data structure* is a data structure that keeps track of a set of elements partitioned into a number of disjoint (non-overlapping) subsets. Disjoint sets play a key role in Kruskal's algorithm

### Union-Find Algorithms

A [*union-find algorithm*](http://en.wikipedia.org/wiki/Disjoint-set_data_structure) is an algorithm that performs two useful operations on such a data structure:

**Find:** Determine which subset a particular element is in. This can be used for determining if two elements are in the same subset.

**Union:** Join two subsets into a single subset.

### Array-based Union Find

First, we construct a **bijection** - which is a fancy say of mapping our objects (i.e. nodes on a graph) to an id > 0. We can map arbitrarily. 

We then get an array (assuming all objects are mapped to a distinct value). Take for example this array:

| A    | B    | C    | D    | E    |
| ---- | ---- | ---- | ---- | ---- |
| 0    | 1    | 2    | 3    | 4    |

If we apply the following instruction: **Union(C, E)** 

either C takes on the value of E or vice versa. We can think of this as a parent-child relationship. The resulting array representation is:

| A    | B    | C     | D    | E     |
| ---- | ---- | ----- | ---- | ----- |
| 0    | 1    | **4** | 3    | **4** |

Now, let's say we want to apply the following operation: **Union(C, D)**

We know from the previous operation that C is a child of E, the given operation will simply make D a child of E too!

| A    | B    | C    | D     | E    |
| ---- | ---- | ---- | ----- | ---- |
| 0    | 1    | 4    | **4** | 4    |

Not too complicated at all!

## Application to Kruskal's Algorithm

https://www.youtube.com/watch?v=JZBQLXgSGfs

# L21 - Prim's Algorithm
[← Return to Index](#table-of-contents)


Kruskal's algorithm builds a MST one edge at a time. Prim's algorithm builds the MST one vertex at a time. 

```pseudocode
let T be a single vertex x
while (T has fewer than n vertices) {
    find the smallest edge connecting T to G-T
    add it to T
}
```

As we can see: ''find the smallest edge connecting T to G-T" can be computationally expensive. However, we can utilise a min heap to remember, for each vertex, the smallest edge connecting T with that vertex.

```pseudocode
Prim with heaps:
	make a heap of values (vertex,edge,weight(edge))
    initially (v,-,infinity) for each vertex
        let tree T be empty
    while (T has fewer than n vertices) {
        let (v,e,weight(e)) have the smallest weight in the heap
        remove (v,e,weight(e)) from the heap
        add v and e to T
        for each edge f=(u,v)
        if u is not already in T
            find value (u,g,weight(g)) in heap
            if weight(f) < weight(g)
            replace (u,g,weight(g)) with (u,f,weight(f))
}
```

# L22 - Topological Sorting (Toposort)
[← Return to Index](#table-of-contents)


[Geeks for Geeks](https://www.geeksforgeeks.org/topological-sorting/)

Requirements:

- DAG Graph
  - Directed
  - Acyclic

## What is toposort?

A linear ordering of vertices such that for every directed edge `u->v`, vertex u comes before vertex v in the ordering.

## Topological Sorting Algorithm Overview

We can modify the depth-first search algorithm to sort the graph topologically. We can model the problem to use a stack. We start at an arbitrary vertex, and recursively traverse the neighbours the vertex points to. Once we encounter a sink (a vertex that does not point to another vertex, but rather has only vertices that point to it), we push the vertex to the stack and backtrack, adding each prior vertex into the stack. 

## Toposort Example

Consider the following graph:

![Topological Sorting Example from Lecture](images/toposortexample.png)

Let us apply the topological sorting algorithm using a stack.

Let us start at an arbitrary vertex, say **4**.

Here are the steps taken:

- Start at `4`, recursively traverse its neighbours `0` and `2`. 
  - Looking at `0` first, we see that it has neighbour `1` 
  - Looking at `1`, we see that it has neighbour `2`
  - `2` is a sink (points to no other vertex) and we add this to the stack
- Our stack looks like: [2, ]
- Now we backtrack - adding `1`, then `0` then `4` to the stack. 
- We don't look at `2` again, since its already visited (in our stack).
- Our stack looks like: [2, 1, 0, 4]
- Now we start with another unvisited vertex (node), say **3**
- Since all neighbours of 3 are in the stack (just `4` in this case), we just add 3 to the stack
- Our stack looks like: [2,1,0,4,3]
- Now we start with another unvisited vertex (node), say **7**
- Since all neighbours of 7 are in the stack (just `0` in this case), we just add 7 to the stack
- Our stack looks like: [2,1,0,4,3,7]
- Now we start with another unvisited vertex (node), say **5**
- Since all neighbours of 5 are in the stack (just `1` in this case), we just add 5 to the stack
- Our stack looks like: [2,1,0,4,3,7,5]
- Now we start with another unvisited vertex (node), say **6**
- There are no neighbours of 6, just add it to the stack
- Our stack looks like: [2,1,0,4,3,7,5,6]

Our topological sorting result is an array comprised of the stack of elements taken in order. So one possible sorting is:

6, 5, 7, 3, 4, 0, 1, 2

## Toposort Assumptions

- There must be at least one source, and one sink
- This satisfies the condition: no cycles.

