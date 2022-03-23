# CMPS 2200 Assignment 3
## Answers

**Name:** Mikey Sison

Place all written answers from `assignment-03.md` here for easier grading.



- **b. (8pts)** What are the recurrences for the Work and Span of this solution? What are their Big Oh solutions?
<br>W(n) = W(n - 1) + 1
<br>S(n) = S(n - 1) + 1
<br>W(n) = O(n)
<br>S(n) = O(n)


- **d. (8pts)** Assume that any `map`s are done in parallel, and that we use the efficient implementation of `scan` from class. What are the recurrences for the Work and Span of this solution? 
<br>W(n) = 4W(n/2) + 1
- 2W(n/2) + 2W(n/2) + 1: reduce + scan + map
<br>S(n) =  S(n/2) + 1





**f. (8pts)** Assuming any recursive calls are done in parallel, what are the recurrences for the Work and Span of this solution? What are their Big Oh solutions?
<br>W(n) = 2W(n/2) + 1
<br>S(n) = S(n/2) + 1
<br>W(n) = O(n)
<br>S(n) = O(logn)