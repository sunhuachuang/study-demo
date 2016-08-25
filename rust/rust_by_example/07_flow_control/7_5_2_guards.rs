fn main() {
    let pair = (2, -2);

    println!("tell me about pair {:?}", pair);

    match pair {
        (x, y) if x == y     => println!("these are twins"),
        (x, y) if x + y == 0 => println!("there are kaboom"),
        (x, _) if x % 2 == 0 => println!("first is odd"),
        _                    => println!("there are none"),
    }
}
