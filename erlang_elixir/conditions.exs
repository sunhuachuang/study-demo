# case
# 卫兵模式
# cond
# if unless
# do
case {1, 2, 3} do
  {4, 5, 6} -> IO.puts "cannot match it"
  {1, x, 3} -> IO.puts "match it x is #{x}"
  _ -> IO.puts "nothing"
end

x = 1
case 1 do
  ^x -> IO.puts "it will match"
  _ -> IO.puts "nothing"
end

case 1 do
  1 ->
    IO.puts "block"
    IO.puts "block"
  _ -> IO.puts "nothing"
end

case {1, 2, 3} do
  {1, x, 3} when x > 1 -> IO.puts "match it, x > 1"
  _ -> IO.puts "nothing"
end
