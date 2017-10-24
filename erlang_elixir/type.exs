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

IO.puts "__list and tuple:"
f = [1, 2, 3] # list
g = ["a", true, 1]
IO.puts (List.last g) * (List.first f)
IO.puts length f


h = {1, 2, 3} # tuple
IO.puts List.last Tuple.to_list h

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
