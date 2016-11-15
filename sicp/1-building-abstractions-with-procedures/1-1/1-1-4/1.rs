fn square(x: i32) -> i32 {
    return x * x;
}

fn sum_of_square(x: i32, y: i32) -> i32 {
    return square(x) + square(y);
}

fn main() {
    println!("{}", square(5));
    println!("{}", sum_of_square(2, 3));

    let a = |x: i32| x * x;
    println!("{}", a(5));
}
