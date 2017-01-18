#TODO proc vs block vs lambda
x = proc {|n| n+1 } #=> #<Proc:0x00556700da5360@(irb):135>
x = lambda {|n| n+1} # => #<Proc:0x00556700b3a238@(irb):132 (lambda)>

# {|n| n+1} block only is syntax, only can use behand method
#  The '&' tells ruby to turn the proc or lambda into a block

# proc vs lambda
# 1. lambda check params number, proc not, *x = lambda {|n=0| n+1} is ok
# 2. return in lambda not triggers outside, proc will return. example.

def test_return_lambda
  l = lambda { return }
  l.call
  puts 'this is lambda'
end

def test_return_proc
  p = proc { return }
  p.call
  puts 'this is proc'
end

test_return_lambda #this is lambda
test_return_proc   #nothing

def test_proc_context
  n = 0
  proc {
    puts n
    n += 1
  }
end

p1 = test_proc_context
puts p1.call
puts p1.call

p2 = test_proc_context
puts p2.call

p3 = p1
puts p3.call

def test_lambda_context
  n = 0
  lambda {
    puts n
    n += 1
  }
end

l = test_lambda_context
puts l.call
puts l.call

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
