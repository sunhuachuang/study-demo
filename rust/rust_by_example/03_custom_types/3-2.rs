#![allow(dead_code)]

enum Person {
    //like unit
    Skinny,
    Fat,
    //like tuple
    Height(i32),
    Weight(i32),
    //like structures
    Info { name: String, height: i32 }
}

fn inspect(p: Person) {
    match p {
        Person::Skinny  => println!("is skinny!"),
        Person::Fat     => println!("is fat"),
        Person::Height(i) => println!("has a height of {}", i),
        Person::Weight(j) => println!("has a weight of {}", j),
        Person::Info{ name, height } => { println!("{} has {} height", name, height); },
    }
}

fn main() {
    let person = Person::Height(32);
    let danny  = Person::Weight(18);
    let dave   = Person::Info { name: "Dave".to_owned(), height: 18 };
    let john   = Person::Fat;
    let larry  = Person::Skinny;

    inspect(person);
    inspect(danny);
    inspect(dave);
    inspect(john);
    inspect(larry);
}
