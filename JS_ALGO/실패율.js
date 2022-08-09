var answer = [];
let map = new Map();
let arr = [];
for (let i = 1; i < N + 1; i++) {
  // map.set(stages[i],(map.get(stages[i])|| 0) +1 )
  const a = stages.filter((value) => {
    return i <= value;
  }).length;

  const b = stages.filter((value) => {
    return i == value;
  }).length;

  // console.log(b,a,"실패율",b/a ,"---",i,"번 스테이지")
  arr.push([b / a, i]);
}

const result = arr.sort((a, b) => {
  return b[0] - a[0];
});

answer = result.map((v) => {
  return v[1];
});

return answer;
