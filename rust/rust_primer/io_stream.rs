static WORDS: &'static str = "
这是即将写入文件的内容
";

use std::io::{self, Write};
use std::error::Error;
use std::fs::File;
use std::io::prelude::*;
use std::path::Path;

fn read_input() -> io::Result<()> {
    let mut input = String::new();
    try!(io::stdin().read_line(&mut input));
    println!("you typed: {}", input.trim());
    Ok(())
}

fn main() {
    let isok = read_input();
    println!("{:?}", isok);

    let mut input = String::new();
    io::stdin().read_line(&mut input).expect("WTF!");
    println!("you input: {}", input.trim());

    print!("hello, ");
    print!("world\n");

    let mut input2 = String::new();
    print!("input something: ");
    io::stdout().flush().unwrap(); //直接写并不会渲染出来， 行缓冲(line-buffered)
    io::stdin().read_line(&mut input2).expect("failure!");
    println!("input is: {}", input2);

    let path = Path::new("hello.txt");
    let display = path.display();

    //写入文件
    let mut file = match File::create(&path) {
        Err(why) => {
            panic!("coundn't create file {}: {}",
                   display,
                   Error::description(&why))
        }
        Ok(file) => file,
    };

    match file.write_all(WORDS.as_bytes()) {
        Err(why) => panic!("coundn't write {}: {}", display, Error::description(&why)),
        Ok(_) => println!("successful write {}", display),
    }

    //读取文件
    let mut file = match File::open(&path) {
        Err(why) => panic!("coundn't open {}, {}", display, Error::description(&why)),
        Ok(file) => file,
    };

    let mut s = String::new();
    match file.read_to_string(&mut s) {
        Err(why) => panic!("coundn't read {}: {}", display, Error::description(&why)),
        Ok(_) => println!("{} contains:\n {}", display, s),
    }
}
