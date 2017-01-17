'abc'.each_byte {|c| puts c} #97 98 99
'abc'.each_char {|c| puts c} #a b c

"a\nb\nc\n".each_line {|c| puts c} #a b c

c = 0
for i in 0..4
  print i
  if i == 2 and c == 0
    c = 1
    print "\n"
    redo # 012 234
  end
end
print "\n"

c = 0
begin
  for i in 0..4
    puts i
    c += 1
  end
rescue
  puts c, '-------'
  retry if c < 100
end

puts 'aaa'

def repeat(num)
  while num > 0
    yield
    num -= 1
  end
end

repeat(3) { puts 'a' }

def test
  puts 'here is first'
  yield 1

  puts 'here is secound'

  yield 2
end

test {|num| puts "num is #{num}" } #ok

def test_num num
  while num > 0
    yield num
    num -= 1
  end
end

test_num 10 {|n| puts "num is #{n}"} #ok

def test_param n, m
  puts n, m.inspect #10 {:abc=>"abc"}
end

test_param 10, abc: 'abc'

def test_default_args n=10
  puts n
end

test_default_args
test_default_args 2

BEGIN {
  puts 'this is start first in this file'
}

END {
  puts 'this is end last in this file'
}
