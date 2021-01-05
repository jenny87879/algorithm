let arr = [0];
function getFibonacci(n) {
  if (n <= 2) {
    return 1;
  }
  if (!arr[n]) {
    // 내가 저장한 값 중에 없다면...
    arr[n] = getFibonacci(n - 1) + getFibonacci(n - 2);
  }
  return arr[n];
}

console.log(getFibonacci(2));
