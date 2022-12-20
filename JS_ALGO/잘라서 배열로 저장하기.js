function solution(my_str, n) {
  var answer = [];
  // const length = my_str.length
  // for (let i = 0; i < Math.ceil(length/n); i ++) {
  //     answer.push(my_str.slice(0,n))
  //     my_str = my_str.slice(n)
  // }
  const a = my_str.match(new RegExp(`.{1,${n}}`, "g"));
  return a;
}
