def first_line filename
  begin
    puts 'begin...'
    file = open filename
    info = file.gets
    file.close
    info
  rescue
    nil
  ensure # ensure that this code always runs, no matter what
    puts 'ensure' # 还是返回info, 而不是这儿的最后一句
  #else code that runs only if *no* exception was raised
    #puts 'else'
  end
end

puts first_line './foo.c' ##include <stdio.h>
puts first_line './bar.c'
