class Dog
  attr :name
  def speck
    puts self.name
  end

  def initialize name
    @name = name
  end
end

(Dog.new 'Tom').speck
# puts Dog.new.methods.inspect

class Test
  def self.self_method
    puts 'self method'
  end

  def default_method
    puts 'default method'
  end

  def get_default_method
    self.default_method
  end

  def get_default_method_not_self
    default_method
  end

  def get_self_method
    # self_method, self.self_method wrong
    Test.self_method
  end
end

Test.self_method
#Test.new.self_method wrong
#Test.default_method wrong
Test.new.default_method
Test.new.get_default_method
Test.new.get_default_method_not_self
Test.new.get_self_method

#inheritance
class Animals
  attr :name, :age

  def self.class_method
    puts 'this is class method'
  end

  def Animals.static_method
    puts 'this is static method'
  end

  def breathe
    puts 'breathe...'
  end

  def speck
    puts "#{@name} here is super speck"
  end

  def initialize name, age
    @name = name
    @age = age + 1
  end
end

class Cat < Animals
  def speck
    #puts (Animals.methods.include? :speck) ? super : 'super no speck'
    begin
      super
    rescue NoMethodError
      puts 'super no speck method'
    else
      puts '-----super ok--------'
    end

    puts "name is #{@name}, age is #{@age}"
  end

  def initialize name, age=1
    @name = name
    @age = age
    super #call parent same name method
    puts super
  end

  def fail_say
    fail 'I am not say' #TODO fail vs raise
  end
end

(Cat.new 'Jerry', 10).speck
(Cat.new 'Jerry').breathe
#(Cat.new 'Jerry').fail_say
Cat.class_method
Cat.static_method

def test
end
puts test.class #TODO test.class vs NilClass 参数接收

class Access
  def get_private_method name
    puts "name is #{private_method name}"
  end

  def get_protected_method name
    puts "name is #{protected_method name}"
  end

  def public_method name
    puts "--public name: #{name}---"
  end

  private
  def private_method name
    "--private name: #{name}---"
  end
  protected
  def protected_method name
    "--protected name: #{name}---"
  end
end

class AccessChild < Access
end

Access.new.get_private_method 'Tom'
Access.new.get_protected_method 'Tom'
AccessChild.new.get_private_method 'Child'
AccessChild.new.get_protected_method 'Child'
AccessChild.new.public_method 'Child'

#TODO protected vs private
puts '------------------'
a = Access.new

# puts a.protected_method NoMethodError

# singleton method
def a.get_protected_method_out sub
  puts sub.protected_method 'out'
end

def a.get_private_method_out sub
  puts sub.privated_method 'out'
end

def get_protected_method_out_a a
  puts a.protected_method 'out'
end

#get_protected_method_out_a a protected
#同一个类的其他对象可以调用该对象的protected方法

a.get_protected_method_out a
#a.get_private_method_out a NoMethodError

puts '---------------------'
# accessor
class Test
  def inspect
    'hello this is inspect'
  end
  def to_s
    'this is to_s'
  end
end

t = Test.new # irb(main):444:0> t
             # => hello this is inspect
puts t #this is to_s

# attr == attr_reader
# attr_reader :v	def v; @v; end
# attr_writer :v	def v=(value); @v=value; end
# attr_accessor :v	attr_reader :v; attr_writer :v
# attr_accessor :v, :w	attr_accessor :v; attr_accessor :w
class Test
  attr :a
  attr_reader :reader
  attr_writer :writer
  attr_accessor :accessor, :accessor2

  # 不支持函数重载， 使用默认参数方式实现
  # def test_overload name
  #   puts name
  # end

  def test_overload name, age=1
    puts name, age
  end
end

t = Test.new
t.test_overload 'name'
t.test_overload 'name', 22


a = 'asdafdsasdf\
asdfasdfasdf'
puts a # asdafdsasdf\
       # asdfasdfasdf

a = "asdafdsasdf\
asdfasdfasdf"
puts a #asdafdsasdfasdfasdfasdf

a = '
abc
def
ghi
'
puts a

# comments
=begin
this is big comment
=end
