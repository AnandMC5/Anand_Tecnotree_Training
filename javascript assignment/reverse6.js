function reverseWords(str) {
   
    var wordsArr = str.split(' ');
    wordsArr.reverse();
    
    
    var reversedStr = wordsArr.join(' ');
    return reversedStr;
  }
  
  var str = "Hello World!";
  var reversedStr = reverseWords(str);
  console.log(reversedStr); 
  