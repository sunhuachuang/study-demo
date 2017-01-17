secrets = ['aaa', 'bbb', 'ccc']

secret = secrets[rand(3)]

print "guess? "

while guess = STDIN.gets
  guess.chop!
  if guess == secret
    puts 'you win!'
    break
  else
    puts "you are wrong"
  end
  print "guess? "
end

puts "the secret is #{secret}"

