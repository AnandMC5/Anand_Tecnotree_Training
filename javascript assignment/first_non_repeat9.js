function firstNonRepeatingCharacter(str) {
    // Create an empty object to store character counts
    const counts = {};
  
    // Loop through each character in the string and count their occurrences
    for (let i = 0; i < str.length; i++) {
      const char = str[i];
      counts[char] = counts[char] ? counts[char] + 1 : 1;
    }
  
    // Loop through the string again and return the first character with count 1
    for (let i = 0; i < str.length; i++) {
      const char = str[i];
      if (counts[char] === 1) {
        return char;
      }
    }
  
    // If no non-repeating character was found, return null
    return null;
  }
  