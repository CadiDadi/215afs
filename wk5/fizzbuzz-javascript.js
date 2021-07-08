// Example 1
for(i=0;i<20;)console.log((++i%3?'':'Meat')+(i%5?'':'Ball')||i)

// linebreak
console.log('\n')

// Example 2
for (var i = 1; i <= 20; i++) {
    var f = i % 3 == 0, b = i % 5 == 0;
    console.log(f ? b ? "FizzBuzz" : "Fizz" : b ? "Buzz" : i)
  }