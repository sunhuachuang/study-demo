#[derive(Debug)]
struct Borrowed<'a>(&'a i32);

#[derive(Debug)]
struct NameBorrowed<'a> {
    x: &'a i32,
    y: &'a i32,
}

#[derive(Debug)]
enum Either<'a> {
    Num(i32),
    Ref(&'a i32),
}

fn main() {
    let x = 18;
    let y = 15;

    let single = Borrowed(&x);
    let double = NameBorrowed {x: &x, y: &y};
    let refence = Either::Ref(&y);
    let number  = Either::Num(x);

    println!("{:?}", single);
    println!("{:?}", double);
    println!("{:?}", refence);
    println!("{:?}", number);
}
