def max_subarray(A):
    max_so_far = max_ending_here = lo = hi = 0
    for y,x in enumerate(A):
        if x > max_ending_here + x:
            max_ending_here, lo = x, y
        else:
           max_ending_here += x
        if max_ending_here > max_so_far:
           max_so_far, hi = max_ending_here, y
    return (A[lo:hi + 1], max_so_far)


lst = [31, -41, 59, 26, -53, 58, 97, -93, -23, 84]
print max_subarray(lst)