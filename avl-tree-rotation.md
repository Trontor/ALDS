# AVL Tree Rotation

*[Thanks to John Hargrove for his tutorial](https://www.cise.ufl.edu/~nemo/cop3530/AVL-Tree-Rotations.pdf)*

This process may seem intimidating, and can be confusing very fast. Let's try to formulate a procedure.

## Identify a Need for Rotation

Imagine we have such a tree:

**a**
   \
      **b**
         \
            **c**

With the following balance factors

**a** = 2 - 0 = 2
**b** = 1 - 0 = 1
**c** = 0 - 0 = 0

As we can see, node **a** has an imbalance out of the acceptable range (-1, 0, 1).

We have an **unbalanced state** and therefore need a rotation.

Simple.

## Determining Rotation Type

This is the harder part. In the previous example, we see that node **a** has a balance factor of **2**. If we think back to the balance equation: 

Balance_Factor = Height(Right_Subtree) - Height(Left_Subtree)

Since Height() will always be positive, a balance factor of **+2** means that Height(Right_Subtree) > Height(Left_Subtree)

This means that the tree is ***right heavy***. Logically, to fix a right heavy tree, we can perform a ***left rotation***!

Trivially, a ***left heavy*** tree requires a ***right rotation***!

### Single Left Rotation

Back to the example, with example numbers this time:

**a** = 9
   \
      **b** = 14
         \
            **c** = 200

* **b** becomes the new root
* **a** takes **b's** *left* child and makes it is right child (in this case, null)
* **b** makes **a** its *left* child

​      **b** = 14
   /       \
**a** = 9      **c** = 200

A simple sanity check is to verify that order has been preserved!

### Single Right Rotation

Mirror of left rotation:

​            **c** = 200, *Balance* = 0 - 2 = **-2 !!!**
          /
       **b** = 14, *Balance* = 0 - 1 = -1
    /
**a** = 9 , *Balance* = 0

*Category*: ***left heavy*** 
*Fix*: ***right rotation***

* **b** becomes new root
* **c** takes **b's** *right* child, and makes it its left child (in this case, null)
* **b** makes **c** its *right* child

​      **b** = 14
   /       \
**a** = 9      **c** = 200



Here is some pseudocode to keep in mind:

```pseudocode
IF tree is right heavy
{
	IF tree's right subtree is left heavy
 	{
 		Perform Double Left rotation
 	}
 	ELSE
 	{
		Perform Single Left rotation
 	}
}
ELSE IF tree is left heavy
{
     IF tree's left subtree is right heavy
     {
     	Perform Double Right rotation
     }
     ELSE
     {
     	Perform Single Right rotation
     }
} 
```

