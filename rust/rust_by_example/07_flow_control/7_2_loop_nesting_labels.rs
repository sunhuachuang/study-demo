#[allow(unreachable_code)]

fn main() {
    'outer: loop {
        println!("Entered the outer loop");
        'inner: loop {
            println!("Entered the inner loop");
            break 'outer;
        }
        println!("this will never show");
    }

    println!("exit the loop");
}
