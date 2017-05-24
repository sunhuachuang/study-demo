//trait对象在Rust中是指使用指针封装了的 trait，比如 &SomeTrait 和 Box<SomeTrait>
trait Foo {
    fn method(&self) -> String;
}

impl Foo for u8 {
    fn method(&self) -> String {
        println!("{}", self);
        format!("u8: {}", *self)
    }
}

impl Foo for String {
    fn method(&self) -> String {
        println!("{}", self); //Helllo
        format!("string: {}", *self) //string: Helllo
    }
}

fn do_something(x: &Foo) {
    println!("{}", x.method());
}

fn main() {
    let x = "Helllo".to_string();
    do_something(&x);

    let u = 2u8;
    do_something(&u);
}
