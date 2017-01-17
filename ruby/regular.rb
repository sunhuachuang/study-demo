def chab(s)
  (s =~ /<0(x|X)(\d|[a-f]|[A-F])+>/) != nil # =~匹配运算符，匹配到返回位置，否则返回nil
end

puts chab('nothing')
puts chab('this one? {0x58}')
puts chab('this one? <0x37zab>')
puts chab('this one? <0x37ab>')
puts chab('this one? <0xFA001>')
