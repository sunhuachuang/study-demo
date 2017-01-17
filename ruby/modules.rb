module Say
  attr :name
  def say_name
    puts @name
  end

  def change_name
    @name = 'Nobody'
  end
end

class Dog
  include Say

  def initialize name
    @name = name
  end
end

d = Dog.new 'HHH'
d.say_name
d.change_name
d.say_name
