a = 1   # integer
IO.puts is_integer a
a1 = 1.0e10
IO.puts is_integer a1

b = 0.1 # float64
IO.puts is_float b

c = true # boolean
IO.puts is_boolean c
IO.puts c == :true

d = :a # atom
IO.puts is_atom d

e = "hello" # string
IO.puts e <> " world!"
IO.puts "say #{e}"
IO.puts is_binary(e) # true
e1 = "abc字"
IO.puts byte_size e1     # 6 UTF-8
IO.puts String.length e1 # 4

IO.puts "__list and tuple: 链表"
f = [1, 2, 3] # list
g = ["a", true, 1]
IO.puts (List.last g) * (List.first f)
IO.puts length f
ff = f ++ g
IO.puts hd tl ff
Enum.map(ff, fn x -> IO.write x end)
IO.puts ''
IO.puts hd ff


h = {1, 2, 3} # tuple 连续空间段，数组
IO.puts List.last Tuple.to_list h
{ok, msg} = File.read('./test')

## *_size 用于对常数范围的长度取值 byte_size tuple_size
## *_length 用于需要遍历的长度取值 String.length length

IO.puts "__functions:"
# function
# 匿名函数 .
add = fn x, y -> x + y end
add_2 = fn x -> x + 2 end
j = add.(1, 2)
k = add_2.(1)
IO.puts (add. (1, 2))
IO.puts j
IO.puts k
