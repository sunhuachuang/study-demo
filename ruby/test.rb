require './modules.rb'
OnlyFunction.test

d = Dog.new('aaaaaa')
d.say_name

exit
class TestNumber
  attr_accessor :value
  def +(other)
    @value + other + other
  end
end

t = TestNumber.new
t.value = 1
puts t + 2 #5

# 数组定义的几种方式
a = [1, 2, 3]
a = *(1..3)

a = ('1'..'3').to_a #["1", "2", "3"]
a = %w(1 2 3) #["1", "2", "3"]
a = *?1..?3 #["1", "2", "3"]

a = Array.new([1, 2, 3])
a = Array[*(1..3)]
a = Array.new(3, 0)
a = Array.new(3) { |i| (i+1).to_s } # 从0开始

a = 1.step(10, 3).to_a
a = [] << 1 << 2 << 3

plus_one = 1.method(:+)
a = Array.new(3, &plus_one)

plus_one = proc {|n| n+1 }
a = Array.new(3, &plus_one)

a = Array.new(3).map(&:to_i)

1.step(10, 3) #<Enumerator: 1:step(10, 3)>
3.times #<Enumerator: 3:times

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
