function solution(id_list, report, k) {
  // 객체를 신고받은사람의 id, value를 신고한 사람 list
  let obj = new Map();
  let answer = [];
  console.log(answer);
  for (let i = 0; i < id_list.length; i++) {
    obj.set(id_list[i], []);
    answer.push(0);
  }

  report.forEach((v) => {
    a = v.split(" ");
    b = obj.get(a[1]);
    b.push(a[0]);
    obj.set(a[1], b);
  });

  obj.forEach((v, key) => {
    let a = new Set(v);
    if (a.size >= k) {
      a.forEach((name) => {
        answer[id_list.indexOf(name)] += 1;
      });
    }
  });
  // console.log(answer)

  return answer;
}
