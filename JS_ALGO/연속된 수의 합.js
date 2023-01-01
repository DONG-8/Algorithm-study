function solution(num, total) {
  var answer = [];
  // 0부터 채워지는 배열 생성
  let arr = Array.from(new Array(num), (x, i) => i);
  let sum = arr.reduce((a, b) => a + b, 0);
  let startNumber = parseInt((total - sum) / num);

  answer = arr.map((v) => v + startNumber);

  return answer;
}
