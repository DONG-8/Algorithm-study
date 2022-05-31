function solution(people, limit) {
  let answer = 0;
  people.sort(function (a, b) {
    return b - a;
  });

  for (let i = 0, j = people.length - 1; i <= j; i++) {
    if (people[i] + people[j] > limit) {
      answer++;
    } else {
      answer++;
      j--;
    }
  }

  return answer;
}
