a = 'abcd'

puts a[0, 1]  # a [start, num)
puts a[1, 2]  # bc
puts a[1..2]  # bc
puts a[-1, 2] # d
puts a[-1..0] #
puts a[0..-1] # abcd [start, end]

puts '-------MARK integer & float symbol'

a = 'w'
b = 'w'
puts 'string eq' if a == b #true
puts 'string id eq' if a.__id__ == b.__id__ #false

c = 1000
d = 1000
puts 'number eq' if c == d #true
puts 'number id eq' if c.__id__ == d.__id__ #true

e = 1000.1
f = 1000.1
puts 'float eq' if e == f #true
puts 'float id eq' if e.__id__ == f.__id__ #true


