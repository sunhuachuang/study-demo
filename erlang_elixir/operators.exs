# and or not 只能接受 boolean
# && || ! 接受任意类型 除了false, nil为false, 其他 true
IO.puts true or false
IO.puts false or nil # nil
# IO.puts nil or false # expected a boolean on left-side of "or", got: nil
IO.puts not true

IO.puts !nil         # true
IO.puts !0           # false
IO.puts nil || false # false
IO.puts '' || false  # ''
IO.puts  '' && 0     # 0

IO.puts 1 == 1    # true
IO.puts 1 === 1   # true
IO.puts 1 == 1.0  # true
IO.puts 1 === 1.0 # false

# number < atom < reference < functions < port < pid < tuple < maps < list < bitstring
IO.puts 1 < []    # true
