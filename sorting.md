# Insertion Sort

* Start at the second index (i = 1)
* The key is designated as A[i]
* Loop through every item before it and check if it is greater than the key, 
  * If it is, shift the item to the right and decrement *i*
  * If it isn't then assign the key to the new index at *i*                                                                                                                                                                                                                                                         

```pseudocode
i ← 1
while i < length(A)
    j ← i
    while j > 0 and A[j-1] > A[j]
        swap A[j] and A[j-1]
        j ← j - 1
    end while
    i ← i + 1
end while
```

