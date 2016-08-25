fn main() {
    let a = [1, 2, 3];
    let _b = a;

    let t = (1, "abc");
    let _m = t;
    println!("{:?}", a);
    println!("{:?}", t);

    let mut x = 5;
    {
        let y = &mut x;
        *y += 1;
    }
    println!("{}",x);
}
