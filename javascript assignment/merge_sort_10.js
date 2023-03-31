function mergeSort(arr) {
    // Base case: If the array has one or fewer elements, it's already sorted
    if (arr.length <= 1) {
      return arr;
    }
    
    const mid = Math.floor(arr.length / 2);
    const left = arr.slice(0, mid);
    const right = arr.slice(mid);
    
    const sortedLeft = mergeSort(left);
    const sortedRight = mergeSort(right);

    const result = [];
    let leftIndex = 0;
    let rightIndex = 0;
    while (leftIndex < sortedLeft.length && rightIndex < sortedRight.length) {
      if (sortedLeft[leftIndex] < sortedRight[rightIndex]) {
        result.push(sortedLeft[leftIndex]);
        leftIndex++;
      } else {
        result.push(sortedRight[rightIndex]);
        rightIndex++;
      }
    }
    // Add any remaining elements from the left or right half
    return result.concat(sortedLeft.slice(leftIndex)).concat(sortedRight.slice(rightIndex));
  }
  
  
  const arr = [4, 2, 1, 3, 5];
  console.log(mergeSort(arr)); // Output: [1, 2, 3, 4, 5]
  