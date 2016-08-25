fn main() {
    let i = 5;

    {
        let x = &i;
        println!("x:{}", x);
    }
    {
        let y = &i;
        println!("y:{}", y);
    }

    println!("i:{}", i)
}
