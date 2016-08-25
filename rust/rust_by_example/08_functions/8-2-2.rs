fn apply<F>(f: F) where F: FnOnce() {
    f()
}

fn apply_to_3<F>(f: F) -> i32 where F: Fn(i32) -> i32 {
    f(3)
}

fn main() {
    let greeting = "hello";

    let mut farewell = "gooodbye".to_owned();

    let diary = || {
        println!("I sad {}.", greeting);

        farewell.push_str("!!!");

        println!("when I screamed {}", farewell);
        println!("now I can sleep!!!");
        drop(farewell);
    };

    apply(diary);

    let double = |x| 2 * x;
    println!("3 dobled: {}", apply_to_3(double));
}
