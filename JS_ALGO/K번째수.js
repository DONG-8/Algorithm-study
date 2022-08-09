function solution(array, commands) {
  let len = commands.length;
  let answer = [];
  for (let i = 0; i < len; i++) {
    let arr = commands[i];
    let start = arr[0] - 1;
    let end = arr[1];
    let idx = arr[2] - 1;

    let slicing = array.slice(start, end).sort((a, b) => a - b);
    answer.push(slicing[idx]);
  }

  return answer;
}
