function solution(nums) {
  let answer = -1;
  const cnt = [];
  let result = [];

  combination(0, 0, nums, result, cnt);
  // console.log(cnt.length)
  return cnt.length;
}

function combination(n, start, arr, result, cnt) {
  if (n == 3) {
    // console.log(result)

    if (sosu(sum(result))) {
      cnt.push(1);
    }
    return;
  }

  for (let i = start; i < arr.length; i++) {
    result.push(arr[i]);
    combination(n + 1, i + 1, arr, result, cnt);
    result.pop();
  }
}

function sosu(num) {
  // console.log(num,'들어온숫자')
  for (let i = 2; i < num; i++) {
    if (i * i > num) {
      break;
    }
    // 소수라면
    if (num % i === 0) {
      return false;
    }
  }
  return true;
}

function sum(arr) {
  let number = 0;
  for (let i = 0; i < arr.length; i++) {
    number += arr[i];
  }
  return number;
}
