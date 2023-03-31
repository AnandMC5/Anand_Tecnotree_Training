function findMissingNumber(arr) {
    const n = arr.length + 1; 
    const sum = (n * (n + 1)) / 2; 
  
    let arrSum = 0;
    for (let i = 0; i < arr.length; i++) {
      arrSum += arr[i]; 
    }
  
    return sum - arrSum; 
}
 
  const arr1 = [1, 2, 4, 5, 6];
  console.log(findMissingNumber(arr1)); // Output: 3
  
  const arr2 = [10, 7, 6, 8, 5, 9, 2, 3, 1];
  console.log(findMissingNumber(arr2)); // Output: 4
 