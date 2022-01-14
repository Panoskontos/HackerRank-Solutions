def sansaXor(arr):
    length = len(arr)

    if not length % 2:
        return 0

    sums = 0
    for i in range(0, length, 2):
        sums ^= arr[i]
    return sums

    # My observation is: if number of elements in the array are even: Then the number of times each element will repeat is 0 considering all the sub arrays, so the XOR of any number repeated even number of times is 0, Hence answer is straight away 0 if number of elements are even. if number of elements in the array are odd: Then the first element will repeat odd number of times, 2nd element will repeat even number of times and 3rd element odd times and so on in the final cumulative subarrays. Performing XOR for odd number of times will result in the same number, hence performing XOR with the alternate elements will give the same answer.
