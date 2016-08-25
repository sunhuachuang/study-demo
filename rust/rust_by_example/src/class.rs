struct Person {
    name: &'static str,
    age: u32,
}

trait Eat {
    fn eat(&self) {}
}

impl Eat for Person {
    fn eat(&self) { println!("{} is eating, age is {}", &self.name, &self.age); }
}

fn main() {
    let p = Person {
        name: "hello",
        age:   20,
    };

    p.eat();
}
