// 1-3 a: abcde
const correct = require('fs')
  .readFileSync('input.txt', 'utf-8')
  .split('\n')
  .filter(line => !!line)
  .map(line => line.match(/(\d+)-(\d+) (\w): (\w*)/))
  .map(reg =>
    [parseInt(reg[1]) - 1, parseInt(reg[2]) - 1]
      .map(x => reg[4][x] == reg[3])
      .reduce((acc, val) => acc ^ val)
  )
  .reduce((a, b) => a + b)

console.log(correct)
