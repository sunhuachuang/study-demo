fn main() {
    struct Foo { x: (u32, u32), y: u32 }

    let foo = Foo { x: (2, 3), y: 4 };
    let Foo{ x:(a, b), y } = foo;

    println!("a = {}, b={}, y={}", a, b, y);

    let Foo{ x: i, y:j } = foo;
    println!("i:{:?}, j:{:?}", i, j);

    let Foo { y, .. } = foo;
    println!("y={:?}", y);
}
