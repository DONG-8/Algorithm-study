function solution(s) {
  var answer = '';
  
  if (s.length %2 == 0) {
      word = parseInt(s.length/2)
      console.log(word)
      answer = s.slice(word-1,word+1)
  } else {
      word = parseInt(s.length/2)
      answer = s[word]
  }
  
  return answer;
}