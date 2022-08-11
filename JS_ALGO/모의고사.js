// 1번 수포자  1,2,3,4,5
// 2번 수포자  2,1,2,3,2,4,2,5
// 3번 수포자  3,3,1,1,2,2,4,4,5,5,

// 반복,, 범위 answer
// 유효성 검사 answer의 index%(각 수포자의 찍는방식 arr의 길이)
// 정답 체크 --> 맞춘 갯수 === answer의 길이

function solution(answers) {
  console.log(answers, "정답");
  var answer = [];
  const dict = { 1: 0, 2: 0, 3: 0 };
  const one = [1, 2, 3, 4, 5];
  const two = [2, 1, 2, 3, 2, 4, 2, 5];
  const three = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5];
  for (let i = 0; i < answers.length; i++) {
    if (one[i % one.length] === answers[i]) {
      dict["1"] += 1;
    }
    if (two[i % two.length] === answers[i]) {
      dict["2"] += 1;
    }
    if (three[i % three.length] === answers[i]) {
      dict["3"] += 1;
    }
  }

  let arr = Object.values(dict);
  let max = Math.max(...arr);

  arr.forEach((v, i) => {
    if (v === max) {
      answer.push(i + 1);
    }
  });
  return answer;
}
