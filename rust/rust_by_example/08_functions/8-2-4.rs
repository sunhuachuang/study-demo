//<>括号内相当于变量的类型进行简写
fn call_function<F: Fn()>(f: F) {
    f()
}

fn print() { println!("this is a function"); }

fn main() {
    call_function(print);
}
