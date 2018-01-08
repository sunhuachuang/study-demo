# = 模式匹配运算符
# ^ pin运算符，访问前一次绑定值

a = 1 # 变量左侧赋值
1 = a # ok
# 2 = a # error (MatchError) no match of right hand side value

{a, bb} = {'a', 'b'}
IO.puts a
IO.puts bb


{aa, bb} = {'a', 1}
IO.puts aa
IO.puts bb

{aa, bb} = {'aa', 'b'} # ok
IO.puts aa
IO.puts bb

{:ok, msg} = {:ok, "ss"}
# {:ok, msg} = {:error, "ss"} #(MatchError) no match of right hand side value: {:error, "ss"}
IO.puts msg

[h|t] = [1, 2, 3]
IO.puts h    # 1
IO.puts hd t # 2

[h|_] = [1, 2, 3, 4]
IO.puts h    # 1

x = 1
^x = 1
IO.puts x
# ^x = 2 match error
{x, ^x} = {2, 1}
IO.puts x # 2
x = 1
y = 2
{x, y} = {y, x}
IO.puts x
IO.puts y
