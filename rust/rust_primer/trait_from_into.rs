#[derive(Debug)]
struct Person {
    name: String,
}

impl Person {
    fn new(name: String) -> Person {
        Person { name: name }
    }
}

impl Person {
    fn new2<S: Into<String>>(name: S) -> Person {
        Person { name: name.into() }
    }
}

//From<T>
fn main() {
    let s = "hello".to_string();
    let ss = String::from("hello");
    assert_eq!(s, ss);
    is_hello(s);
    is_hello("hello");

    let name = "Sun".to_string();
    let person = Person::new(name);
    println!("{:?}", person);

    let person2 = Person::new2("sun");
    println!("{:?}", person2);
}

fn is_hello<T: Into<Vec<u8>>>(s: T) {
    let h = b"hello".to_vec();
    assert_eq!(h, s.into());
}
