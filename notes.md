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

* For two function *f(n)* and *g(n)*, we say that *f(n)* is *O(g(n))* if there are constants c and N such that f(n) \< c * g(n) for all n > N
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

### Big Omega (Lower Bound) and Big Theta (Growth Rate) 

For two function *f(n)* and *g(n)*, we say that *f(n)* is *Ω(g(n))* if there are constants c and N such that f(n) > c * g(n) for all n > N