def find_primes
  primes = []
  primes << 2 << 3
  counter = 4
  until primes.length == 10001
    if is_prime?(counter)
      primes << counter
      #puts primes.length
    end
    counter += 1
    #puts counter
  end
  puts primes[10000]
end
      
def is_prime?(num)
  isPrime = true
  (2..(num/2)).each do |i|
    if (num % i) == 0
      isPrime = false
      break
    end
  end
  isPrime
end

find_primes


      
  
  