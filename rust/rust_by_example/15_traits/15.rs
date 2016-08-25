trait Animal {
    fn new(name: &'static str) -> Self;

    fn name(&self) -> &'static str;
    fn noise(&self) -> &'static str;
    fn talk(&self) {
        println!("{} and {}", &self.name(), &self.noise());
    }
}

struct Dog { name: &'static str }

impl Dog {
    fn wag_tail(&self) {
        println!("{} is waging tail", self.name);
    }
}

impl Animal for Dog {
    fn new(name: &'static str) -> Dog {
        Dog{ name: name }
    }

    fn name(&self) -> &'static str {
        self.name
    }

    fn noise(&self) -> &'static str {
        "woof!"
    }

    fn talk(&self) {
        self.wag_tail();

        println!("{} say {}", self.name, self.noise());
    }
}

struct Sheep { naked: bool, name: &'static str }

impl Sheep {
    fn is_naked(&self) -> bool {
        self.naked
    }

    fn shear(&mut self) {
        if self.is_naked() {
            println!("{} is already naked", self.name());
        } else {
            println!("{} get a haircut", self.name);
            self.talk();
            self.naked = true;
        }
    }
}

impl Animal for Sheep {
    fn new(name: &'static str) -> Sheep {
        Sheep { name: name, naked: false }
    }

    fn name(&self) -> &'static str { self.name }

    fn noise(&self) ->&'static str {
        if self.is_naked() {
            "aaa"
        } else {
            "baaaaaz"
        }
    }
}

fn main() {
    let mut dolly: Sheep = Animal::new("Dolly");
    let spike: Dog = Animal::new("Spike");

    dolly.shear();
    dolly.talk();
    spike.talk();
}
