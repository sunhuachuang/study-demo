fn main() {
    let pair = (0, -2);
    println!("tell me about {:?}", pair);

    match pair {
        (0, y) => println!("first is 0, second is {}", y),
        (x, 0) => println!("first is {}, second is 0", x),
        _      => println!("it doesnot matter what they are"),
    }
}
