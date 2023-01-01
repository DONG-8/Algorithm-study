function solution(progresses, speeds) {
  var answer = [];
  let check = 0;
  while (progresses.length !== 0) {
    const nextArr = progresses.map((v, i) => {
      return progresses[i] + speeds[i];
    });
    let cnt = 0;

    while (nextArr[0] >= 100) {
      // 앞자리가 100
      nextArr.shift();
      speeds.shift();
      cnt += 1;
    }

    if (cnt !== 0) {
      answer.push(cnt);
      cnt = 0;
    }
    progresses = nextArr;
  }
  return answer;
}
