fn main() {
    let x = 1u8;
    let y = 2u32;
    let z = 3f32;

    let i = 1;
    let j = 1.0;

    println!("size if x in bytes: {}", std::mem::size_of_val(&x));
    println!("size if y in bytes: {}", std::mem::size_of_val(&y));
    println!("size if z in bytes: {}", std::mem::size_of_val(&z));
    println!("size if i in bytes: {}", std::mem::size_of_val(&i));
    println!("size if j in bytes: {}", std::mem::size_of_val(&j));
}
