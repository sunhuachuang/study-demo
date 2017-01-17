#TODO proc vs block vs lambda
p = proc {
  puts 'this is proc'
}

def show_proc p
  puts 'call the proc'
  p.call
end

show_proc p

# trap "SIGINT", proc{ puts "^C was pressed." }
# trap "SIGINT", 'puts "^C was pressed."'

#lambda
bar = ->(n) { puts n }
bar.call(100)

l = lambda do |a, b|
  puts '----'
  puts a, b
  a+b
end
puts l.call(1, 2)
puts '----'

#block
(1..5).each { |n| puts n }
