fn main() {
    let mut arr: [i32; 3] = [0; 3];
    arr[1] = 1;
    arr[2] = 2;

    assert_eq!([1, 2], &arr[1..]);

    for x in &arr {
        println!("{}", x);
    }

    for x in arr.iter() {
        println!("{}", x);
    }

    let v: Vec<i32> = Vec::new();
    let v2: Vec<i32> = vec![]; //使用宏
    let v3 = vec![1, 2, 3, 4, 5];
    let v4 = vec![0; 10];
    println!("{:?}, {:?}, {:?}, {:?}", v, v2, v3, v4);

    let mut v5 = vec![1, 2];
    v5.push(3);
    println!("{:?}", v5); // [1, 2, 3]
    v5.pop();
    println!("{:?}", v5); // [1, 2]

    // str &str => &[u8]
    let s = "hello";
    let ss: &'static str = "hello";
    assert_eq!(s, ss);

    let s1 = String::from("hello, ");
    let mut hello = String::from("hello, ");
    hello.push('w');
    hello.push_str("orld!");
    println!("{}, {}", s1, hello);

    let mut foo = String::from("foo");
    assert_eq!(foo.pop(), Some('o'));
    assert_eq!(foo.pop(), Some('o'));
    assert_eq!(foo.pop(), Some('f'));
    assert_eq!(foo.pop(), None);
}
