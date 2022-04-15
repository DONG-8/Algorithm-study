// 1차 풀이 시간초과 3문제로 실패
function solution(n) {
  let arr = [];
  for (let i = 1; i < n + 1; i++) {
    arr.push(i);
  }
  var count = [];
  // sliding window
  for (let i = 2; i < n + 1; i++) {
    // 슬라이딩 시킬 크기 & 한번 나오면 다음 크기로 넘어가야함
    let slideNum = arr.slice(0, i);
    let num = slideNum.reduce((pre, cur) => {
      return pre + cur;
    });

    if (num > n) break;

    for (let j = 0; j < n - i; j++) {
      if (num === n) {
        count.push(num);
        break;
      } else {
        // console.log(num)
        let change = num + -arr[j] + arr[j + i];
        if (num > n) break;
        num = change;
      }
    }
  }

  return count.length + 1;
}

// 2차 풀이 딘슨 for문
function solution(n) {
  var answer = 0;

  for (let i = 1; i < n / 2; i++) {
    for (let j = i, tmp = 0; j < n + 1; j++) {
      tmp += j;
      if (tmp === n) {
        answer += 1;
      } else if (tmp > n) {
        break;
      }
    }
  }
  return answer + 1;
}

// 3차 awsome한 풀이
// "주어진 자연수를 연속된 자연수의 합으로 표현하는 방법의 수와
// 주어진 수의 홀수인 약수 갯수는 같다."

function solution(n) {
  let answer = 0;

  for (let i = 0; i <= n; i++) {
    if (n % i === 0 && i % 2 === 1) answer++;
  }

  return answer;
}

// test
console.log(solution(15)); // 4
