fn used_function() {
    println!("this is used function");
}

#[allow(dead_code)]
fn unused_function() {
    println!("this is unused function");
}

fn main() {
    used_function();
}
