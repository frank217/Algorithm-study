# DP

Dynamic programming uese extra memory to store already caculated value
to avoid repetitive caculation and decrease runtime. Also know as overlapping subproblems.

Depending on the how DP is structured runtime may vary. 
Key is to structure this DP carefully to optimize memory and space required to solve the problem.

Generally have top down(Memoization) and bottom up(Tabulation) implementation of DP,
where top down uses recursion to navigate through stored value,
where as bottom up start from base case and build up stored value. 