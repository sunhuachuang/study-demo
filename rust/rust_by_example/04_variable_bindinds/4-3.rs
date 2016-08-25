fn main() {
    let a;

    {
        let x = 2;
        a = x * x;
    }

    println!("a: {}", a);

    let an;

    an = 1;

    println!("an: {}", an);
}
