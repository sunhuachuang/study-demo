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

format('%{first} %{second}', first: 20, second: 10)
format('%d %d', 20, 10)

%w(one two three)

# 测试是否是数组然后操作
Array(maybe_array).each {|| puts ''}

do_something if x.between?(1000, 2000)

# even? odd? zero? nil?

#永远不要使用 END 区块。使用 Kernel#at_exit 来替代
END { puts 'end' }
at_exit { puts 'end' }

# 避免使用  flip-flops 操作符
# bad
(1..20).each do |xx|
  puts xx if (xx == 5) .. (xx == 10)
end

# bad
[0, 1, 2, 3].each do |item|
  if item > 1
    puts item
  end
end

# 好
[0, 1, 2, 3].each do |item|
  next unless item > 1
  puts item
end

# map 而不是 collect，
# find 而不是 detect，
# select 而不是 find_all，
# reduce 而不是 inject
# size 而不是 length, count

(0..3).reduce { |sum, n| sum+=n }

# 只适用于一层嵌套
# 差
all_songs = users.map(&:songs).flatten.uniq

# 好
all_songs = users.flat_map(&:songs).uniq

array = [1, 2, [3, 4, [5, 6]]]
# 差
array.reverse.each { |n| puts n }

# 好
array.reverse_each { |n| puts n }

# 当配合单行区块使用 reduce 时，将参数命名为 |a, e|（accumulator/累加器，element/元素）

# 使用 TODO 标记应当加入的特征与功能。
# 使用 FIXME 标记需要修复的代码。
# 使用 OPTIMIZE 标记可能引发性能问题的低效代码。
# 使用 HACK 标记代码异味，即那些应当被重构的可疑编码习惯。
# 使用 REVIEW 标记需要确认与编码意图是否一致的可疑代码。

class Person
  # 首先是 extend 与 include
  extend SomeModule
  include AnotherModule

  # 内部类
  CustomErrorKlass = Class.new(StandardError)

  # 接着是常量
  SOME_CONSTANT = 20

  # 接下来是属性宏
  attr_reader :name

  # 跟着是其他宏（如果有的话）
  validates :name

  # 公开的类方法接在下一行
  def self.some_method
  end

  # 初始化方法在类方法和实例方法之间
  def initialize
  end

  # 跟着是公开的实例方法
  def some_method
  end

  # 受保护及私有的方法等放在接近结尾的地方
  protected

  def some_protected_method
  end

  private

  def some_private_method
  end
end

# 当你想将模块的实例方法变成类方法时，倾向使用 module_function 而不是 extend self

# 好
class Person
  attr_accessor :first_name, :last_name

  def initialize(first_name, last_name)
    @first_name = first_name
    @last_name = last_name
  end
end
p = Person.new('a', 'b')
p.first_name

# 更好
Person2 = Struct.new(:first_name, :last_name) do
  puts 'ok'
end
p2 = Person2.new('a', 'b')
puts p2.first_name

#当创建一组符号类型的数组（且不需要保持 Ruby 1.9 兼容性）时，倾向使用 %i。此规则只适用于数组元素有两个或以上的时候。
# 差
STATES = [:draft, :open, :closed]

# 好
STATES = %i(draft open closed)

#当访问数组的首元素或尾元素时，倾向使用 first 或 last 而不是 [0] 或 [-1]

#好
a = { one: 1, two: 2, three: 3 }

heroes = { batman: 'Bruce Wayne', superman: 'Clark Kent' }

# 差 - 如果我们打错了哈希键，则难以发现这个错误
heroes[:batman] # => 'Bruce Wayne'
heroes[:supermann] # => nil

# 好 - fetch 会抛出 KeyError 使这个错误显而易见
heroes.fetch(:supermann)

# fetch 设置默认值
batman = { name: 'Bruce Wayne', is_evil: false }

# 差 - 如果仅仅使用 || 操作符，那么当值为假时，我们不会得到预期结果
batman[:is_evil] || true # => true

# 好 - fetch 在遇到假值时依然可以正确工作
batman.fetch(:is_evil, true) # => false
# bad
email = data['email']
username = data['nickname']
#good
email, username = data.values_at('email', 'nickname')

# 差
Regexp.last_match[1]

# 好
Regexp.last_match(1)

# 不要忘记使用 {} 包裹字符串插值中的实例变量或全局变量
