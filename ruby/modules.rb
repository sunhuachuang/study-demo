# include vs extend
# include 是 实例方法
# extend  是 类方法

module Say
  attr :name
  def say_name
    puts @name
  end

  def change_name
    @name = 'Nobody'
  end
end

module Extend
  def say_hello
    puts "this is class method #{self.class}"
  end
end

class Dog
  extend Extend
  include Say

  def initialize name
    @name = name
  end
end

d = Dog.new 'HHH'
d.say_name
d.change_name
d.say_name
Dog.say_hello
