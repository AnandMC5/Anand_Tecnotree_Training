function intersection(arr1, arr2) {
    return arr1.filter(value => arr2.includes(value));
  }
  const arr1 = [7, 2, 8, 4];
  const arr2 = [3, 5, 8, 6];
  const result = intersection(arr1, arr2);
  console.log(result); // Output: [8]
  