fn main() {
    println!("{}", add(1, 2));
    //let x: i32 = diverges();
    //thread 'main' panicked at 'This function never returns', func_method.rs:15
    //note: Run with `RUST_BACKTRACE=1` for a backtrace.
}

fn add(x: i32, y: i32) -> i32 {
    x + y
}

#[allow(dead_code)]
fn diverges() -> ! {
    panic!("This function never returns");
}
