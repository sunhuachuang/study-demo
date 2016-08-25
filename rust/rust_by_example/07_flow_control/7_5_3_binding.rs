fn age() -> i32 {
    15
}

fn main() {
    println!("tell me");

    match age() {
        0             => println!("i am not born yet"),
        n @ 1 ... 12  => println!("child has age {}", n),
        n @ 13 ... 19 => println!("teen has age {} ", n),
        n             => println!("age is {}", n),
    }
}
