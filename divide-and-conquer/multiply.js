/**
 * PROBLEM: https://www.acmicpc.net/problem/1629
 * Type: Divide and Conquer
 * Issue
 * 01. Memory Limit -> Binary Search, Memoization(Dynamic Programming)
 * 02. Large integer issue -> to use BigInt
 */

const memoization = [];

function multiply(a, b, c)
{
  if (b === 0) {
    return memoization[b] = BigInt(1 % c);
  };

  if (b === 1) {
    return memoization[b] = BigInt(a % c);
  };

  const half = Math.ceil(b / 2);

  if (!memoization[half]) multiply(a, half, c);
  if (!memoization[b - half]) multiply(a, b - half, c);
  if (b % 2 === 0) return memoization[b] = (BigInt(memoization[half]) * BigInt(memoization[half])) % BigInt(c);
  return memoization[b] = (BigInt(memoization[half]) * BigInt(memoization[b - half])) % BigInt(c);
}

(function main()
{
  const result = multiply(2147483646, 2147483646, 2147483647);
  console.log(Number(result));
})()
