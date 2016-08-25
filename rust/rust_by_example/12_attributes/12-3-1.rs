#[cfg(some_condition)]
fn conditional_function() {
    println!("call some condition function");
}

//rustc --cfg some_condition 12-3-1.rs && ./12-3-1

fn main() {
    conditional_function();
}
