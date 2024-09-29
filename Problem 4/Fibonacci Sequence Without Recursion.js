function fibo(n) {
  if (n <= 0) {
    return 0;
  }
  let values = [0, 1];
  for (let i = 2; i < n; i++) {
    values[i] = values[i - 1] + values[i - 2];
  }
  return values[n - 1] + values[n - 2];
}

console.log(fibo(10));
