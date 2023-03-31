// Sample array of objects
const people = [
    { name: 'Anand', age: 30 },
    { name: 'Harish', age: 25 },
    { name: 'Sachin', age: 35 },
    { name: 'Lokesh', age: 20 },
  ];
  
  // Property to sort by
  const sortBy = 'age';
  
  // Sort the array of objects by the specified property
  people.sort((a, b) => (a[sortBy] > b[sortBy]) ? 1 : -1);
  
  console.log(people);
  