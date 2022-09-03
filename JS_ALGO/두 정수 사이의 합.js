function solution(a, b) {
  var answer = 0;
  let start, end;
  if (a < b) {
    start = a;
    end = b;
  } else {
    start = b;
    end = a;
  }

  for (let i = start; i < end + 1; i++) {
    answer += i;
  }

  return answer;
}
