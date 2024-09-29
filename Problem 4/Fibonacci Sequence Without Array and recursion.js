function fibo(n) {
  let a = 1;
  let b = 1;
  let fib = 1;

  if (n <= 0) {
    return 0;
  }
  if (n == 1 || n == 2) {
    return 1;
  }
  for (let i = 3; i <= n; i++) {
    fib = a + b;
    a = b;
    b = fib;
  }

  return fib;
}

console.log(fibo(10));
