fn main() {
    println!("{} days", 31);

    println!("{0},this is {1},{1}; this is {0}", "A", "B");

    println!("this is a:{a}, this is b:{b}, this is c:{c}",
             a = "A",
             b = "B",
             c = "C"
             );

    println!("{} is {:b} half", 2, 0);//:b 0=>0; 1=>1; 2=>10; 3=>11; 4=>100; 5=>101; 6=>110; 7=>111

    println!("{number:>width$}", number = 1, width = 6);//six space before
    println!("{number:>0width$}", number = 1, width = 6);//six 0 before

}
