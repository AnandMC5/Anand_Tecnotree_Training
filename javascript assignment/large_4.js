function nthLargestElement(arr, n) {
    // Sort the array in descending order
    arr.sort(function(a, b) {
      return b - a;
    });
    
    // Return the nth largest element
    console.log( arr[n - 1]);
  }
  nthLargestElement([3, 6, 2, 8, 1, 9], 3);

  