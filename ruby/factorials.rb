def fact(n)
  if n < 1
    1
  else
    n * fact(n-1)
  end
end

puts fact(ARGV[0].to_i)

puts ARGV
puts ARGV.class # Array
