#![feature(box_syntax, box_patterns)]

fn main() {
    let x = stack_var();
    println!("{}", x);

    let boxed = Some(box 5);
    match boxed {
        Some(box unboxed) => println!("some {}", unboxed),
        None => println!("None"),
    }
}

/// not work because destory variable in heap when fn over.
/// fn heap_var() -> &str {
///     let x = "test";
///     &x
/// }

fn stack_var() -> String {
    let x = "test";
    x.to_string()
}
