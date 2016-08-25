struct Ower(i32);

impl Ower {
    fn add_one<'a>(&'a mut self) {
        self.0 += 1;
    }

    fn print<'a>(&'a self) {
        println!("ower is {}", self.0);
    }
}

fn main() {
    let mut a = Ower(8);
    a.add_one();
    a.print();
}
