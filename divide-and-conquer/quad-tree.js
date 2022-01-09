// PROBLEM: https://www.acmicpc.net/problem/1992
// Type: Divide and Conquer

function sum(arr)
{
  return arr.reduce((result, item) => result + item, 0)
}

function checkShouldMerge(n, arr)
{
  if (sum(arr.flat()) === 0) return 0
  if (sum(arr.flat()) === (n * n)) return 1
  return -1;
}

function quadTree(n, input)
{
  const result = checkShouldMerge(n, input);
  if (result !== -1) return String(result);
  if (n === 2) return `(${input[0][0]}${input[0][1]}${input[1][0]}${input[0][1]})`;

  const topLeft = input.slice(0, n / 2).map((item) => item.slice(0, n / 2));
  const topRight = input.slice(0, n / 2).map((item) => item.slice(n / 2, n));
  const bottomLeft = input.slice(n / 2, n).map((item) => item.slice(0, n / 2));
  const bottomRight = input.slice(n / 2, n).map((item) => item.slice(n / 2, n));

  return `(${quadTree(n / 2, topLeft)}${quadTree(n / 2, topRight)}${quadTree(n / 2, bottomLeft)}${quadTree(n / 2, bottomRight)})`
}

(function main()
{
  const n = 8;
  const data = [
    [1, 1, 1, 1, 0, 0, 0, 0],
    [1, 1, 1, 1, 0, 0, 0, 0],
    [0, 0, 0, 1, 1, 1, 0, 0],
    [0, 0, 0, 1, 1, 1, 0, 0],
    [1, 1, 1, 1, 0, 0, 0, 0],
    [1, 1, 1, 1, 0, 0, 0, 0],
    [1, 1, 1, 1, 0, 0, 1, 1],
    [1, 1, 1, 1, 0, 0, 1, 1]
  ]

  const result = quadTree(n, data);
  console.log(result);
})()

