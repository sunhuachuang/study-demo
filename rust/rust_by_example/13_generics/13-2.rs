struct Val(f64);
struct GenVal<T>(T,);

impl Val {
    fn value(&self) -> &f64 { &self.0 }
}

impl <T>GenVal<T> {
    fn value(&self) -> &T { &self.0 }
}

fn main() {
    let x = Val(3.0);
    let y = GenVal(3i32);

    println!("{}, {}", x.value(), y.value());
}
