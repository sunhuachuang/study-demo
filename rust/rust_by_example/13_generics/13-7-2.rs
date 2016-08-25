struct Container(i32, i32);

trait Contains {
    type A;
    type B;

    fn contain(&self, &Self::A, &Self::B) -> bool;
    fn first(&self) -> i32;
    fn last(&self)  -> i32;
}

impl Contains for Container {
    type A = i32;
    type B = i32;

    fn contain(&self, number: &i32, digit: &i32) -> bool {
        (&self.0 == number) && (&self.1 == digit)
    }

    fn first(&self) -> i32 { self.0 }
    fn last(&self)  -> i32 { self.1 }
}

fn difference<C: Contains>(container: &C) -> i32 {
    container.first() - container.last()
}

fn main() {
    let number = 3;
    let digit  = 10;
    let container = Container(number, digit);

    println!("does contanier has {} and {} : {}",
             &number, &digit,
             container.contain(&number, &digit)
             );
    println!("first is {}", container.first());
    println!("lase is {}", container.last());

    println!("the difference is {}", difference(&container));

}
