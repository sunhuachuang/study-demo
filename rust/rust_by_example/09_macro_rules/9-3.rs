macro_rules! min {
    ($x: expr) => ($x);
    ($x: expr, $($y: expr), +) =>(std::cmp::min($x, min!($($y), +)));
}

fn main() {
    println!("{}", min!(1u32));
    println!("{}", min!(1u32 + 2, 2u32));
    println!("{}", min!(1u32 + 1, 2u32, 4u32 - 3));
}
