class Test
  attr_accessor :name

  def test
    if name == 'aaa'
      name
    else
      @name = 'bbb' # return 'bbb'
      nil           # return nil
    end
  end
end
t = Test.new
t.name = 'aaa'
puts t.test

exit
def block_test(&block)
  (1..5).each {|num| block.call(num) }
end

block_test {|num| puts num}

a = (1..5).map(&:to_s)
puts a.inspect

exit
a = 1

case a
  when 1..2
    puts '1..2'
  when 6..10
    puts '6..10'
end

exit
def test
  if test
    aaa
  else
    aaa
  end
end

puts gets
puts STDIN.gets
exit

print 'output'+"\n"
print 'output'; STDOUT.flush
exit
a = {'a' => 'aaa', 'b' => 'bbb', 'c' => {'d' => 'ddd'}}

def test(s)
  s += 'aaaa'
end

test(a['a']) #{"a"=>"aaa", "b"=>"bbb", "c"=>{"d"=>"ddd"}}
puts a

test(a['c']['d'])
puts a


exit
puts puts.class #NilClass
exit

print "input? "

a = STDIN.gets
puts a[-1] == "\n"


puts STDIN.methods
puts STDIN.class

exit

puts STDIN.gets

puts 'start from here'

def test
  'hello world'+'----'
end

a = 3.times { "#{test}" }

puts a

puts 4.times { "#{test}" }

5.times { puts "#{test}" }
