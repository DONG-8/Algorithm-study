function solution(s) {
  let answer = "";
  const dic = {
    0: "zero",
    1: "one",
    2: "two",
    3: "three",
    4: "four",
    5: "five",
    6: "six",
    7: "seven",
    8: "eight",
    9: "nine",
  };
  let nullnull = "";
  for (let i = 0; i < s.length; i++) {
    if (s[i] in dic) {
      answer += s[i];
    } else {
      nullnull += s[i];
      const keyOfValue = Object.keys(dic).find((key) => dic[key] === nullnull);
      console.log(nullnull, keyOfValue, "오엥");
      if (keyOfValue) {
        answer += keyOfValue;
        nullnull = "";
      }
    }
  }

  return Number(answer);
}

// better sol

function solution(s) {
  let numbers = [
    "zero",
    "one",
    "two",
    "three",
    "four",
    "five",
    "six",
    "seven",
    "eight",
    "nine",
  ];
  var answer = s;

  for (let i = 0; i < numbers.length; i++) {
    let arr = answer.split(numbers[i]);
    answer = arr.join(i);
  }

  return Number(answer);
}

// better sol2

const digit2word = [
  "zero",
  "one",
  "two",
  "three",
  "four",
  "five",
  "six",
  "seven",
  "eight",
  "nine",
];
function solution(s) {
  return Number(
    digit2word.reduce(
      (ans, word, digit) => ans.replace(new RegExp(word, "g"), digit),
      s
    )
  );
}
