# $ global variable
# @ instance variable
# @@ class variable
# [a-z] or _ local variable
# [A-Z]      constant
#
# two pseudo nil(constant) & self(global variable by interpreter)

$global_variable = 'ggggg'
class Test
  AAA = 'aaa'
  attr :bbb
  @@ccc = 'ccc'

  def get_bbb
    @bbb = 'bbb'
    puts @bbb
    puts AAA
    @bbb
  end
end

class Test2 < Test
  def get_ccc
    puts "#@bbb"
    puts "#@@ccc"
    puts "#$global_variable"
    @@ccc
  end
end

puts Test.new.get_bbb
puts Test::AAA
# puts Test::bbb

puts Test2.new.get_ccc

a = 'aaa'
puts "#{a}"

trace_var :$x, 'puts "$x is now: #$x"'
$x = 0
$x = 3
$x = 10
puts $x
puts $0 #....my_projects/study-demo/ruby/variable.rb
# $!	latest error message
# $@	location of error
# $_	string last read by gets
# $.	line number last read by interpreter
# $&	string last matched by regexp
# $~	the last regexp match, as an array of subexpressions
# $n	the nth subexpression in the last match (same as $~[n])
# $=	case-insensitivity flag
# $/	input record separator
# $\	output record separator
# $0	the name of the ruby script file
# $*	the command line arguments
# $$	interpreter's process ID
# $?	exit status of last executed child process

class T
  def set_foo foo
    @foo = foo
  end

  def get_foo
    @foo
  end
end

puts T.new.get_foo
t = T.new
t.set_foo 'foo'
puts t.get_foo

puts 'unless true' unless true #除非是true, 不然执行
puts 'unless false' unless false
puts 'if true' if true
puts 'until true' until true #直到是true, 不然一直执行
#puts 'until true' until false
#puts 'while true' while true

a = 1

p = proc {|n| a = n } #procedure can get local variable
p.call(2)
puts a #2

def box
  content = nil
  get = proc { content }
  set = proc {|n| content = n}
  return get, set
end

reader, writer = box
puts reader, writer

puts reader.call
writer.call 'aaaa'
puts reader.call

class Test
  AAA = '11111'
end
puts Test::AAA
# puts Test.new::AAA object is not a class/module TypeError
