# bad
class Test<String
end
# good
Test1 = Class.new(String)

# 空方法
def test2; end

# 指数操作符,不要空格
puts 1 * 2**2

# () [] 两端不要空格， {}两端加空格
a = { one: 1, two: 2 }
puts "#{a}"

# when case 缩排在同一层级

kind =
  case year
  when 1850..1889 then 'Blues'
  when 1890..1909 then 'Ragtime'
  when 1910..1929 then 'New Orleans Jazz'
  when 1930..1939 then 'Swing'
  when 1940..1950 then 'Bebop'
  else 'Jazz'
  end

puts kind

#当给方法的参数赋予默认值时，在 = 前后添加空格
def some_method(arg1 = :default, arg2 = nil, arg3 = [])
  # 做一些事情
end

def send_mail(source)
  Mailer.deliver(
    to: 'bob@example.com',
    from: 'us@example.com',
    subject: 'Important message',
    body: source.text
  )
end

# 差
def some_method()
 # 省略主体
end

# 好
def some_method
 # 省略主体
end

# 差
def some_method_with_parameters param1, param2
 # 省略主体
end

# 好
def some_method_with_parameters(param1, param2)
 # 省略主体
end

x = Math.sin y  # 差
x = Math.sin(y) # 好

array.delete e  # 差
array.delete(e) # 好

temperance = Person.new 'Temperance', 30  # 差
temperance = Person.new('Temperance', 30) # 好

# 好 - 与 * 操作符配合使用
first, *list = [1, 2, 3, 4] # first => 1, list => [2, 3, 4]
puts first, list

hello_array = *'Hello' # => ["Hello"]
puts hello_array

a = *(1..3) # => [1, 2, 3]

foo = 'one,two,three,four,five'
# 好
a, = foo.split(',')
a, b, = foo.split(',')
puts a, b

# 好 - 可有可无，但提供了额外信息
first, _second = foo.split(',')
first, _second, = foo.split(',')
first, *_ending = foo.split(',')

# 好 - 占位符，_ 担当最后一个元素
*beginning, _ = foo.split(',')
*beginning, something, _ = foo.split(',')
puts beginning, something

# 差
result = if some_condition then something else something_else end

# 好
result = some_condition ? something : something_else

# 差
some_condition ? (nested_condition ? nested_something : nested_something_else) : something_else

# 好
if some_condition
  nested_condition ? nested_something : nested_something_else
else
  something_else
end

# 使用 ! && || 而不是 not, and 与 or 关键字

names.map(&:upcase)

# 好 - 当且仅当 name 为 nil 或 false 时，设置 name 的值为 'Bozhidar'
name ||= 'Bozhidar'

#使用 &&= 预先检查变量是否存在，如果存在，则做相应动作。使用 &&= 语法可以省去 if 检查
something &&= something.downcase

#未被使用的区块参数或局部变量，添加 _ 前缀或直接使用 _（尽管表意性略差）。这种做法可以抑制 Ruby 解释器或 RuboCop 等工具发出“变量尚未使用”的警告
