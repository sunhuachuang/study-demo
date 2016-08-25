static LANGUAGE: &'static str = "rust";
const THRESHOLD: i32 = 10;
//static NOW: i32 = 23;

fn is_big(n: i32) -> bool {
    n > THRESHOLD
}

fn main() {
    let n = 16;

    println!("this is language {}", LANGUAGE);
    println!("the threshold is {}", THRESHOLD);
    println!("{} is {}", n, if is_big(n) { "big" } else { "small" });

    //NOW = 23;
    println!("now is {}", LANGUAGE);
}
