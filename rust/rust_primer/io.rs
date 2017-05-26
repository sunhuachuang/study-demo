use std::io;
use std::env;
use std::io::prelude::*;
use std::fs::File;

macro_rules! numin {
    () => {
        {
            let mut input = String::new();
            std::io::stdin().read_line(&mut input).expect("Fail to read line");
            input.trim().parse().unwrap()
        }
    };
}

fn main() {
    let args = env::args();
    for arg in args {
        println!("{}", arg);
    }

    let mut input = String::new();
    io::stdin()
        .read_line(&mut input)
        .expect("fail to read line");

    let n: i32 = input.trim().parse().unwrap();
    println!("{}", n);

    let m: i32 = numin!();
    println!("{}", m * 2);

    let f = "foo";
    let mut buf = String::new();

    match create_file(f, b"hello, world") {
        Ok(()) => {
            match read_file(f, &mut buf) {
                Ok(()) => println!("{}", buf),
                Err(err) => println!("{:?}", err),
            }
        }
        Err(err) => println!("{:?}", err),
    }

    let mut binput = String::new();
    std::io::stdin()
        .read_line(&mut binput)
        .expect("fail to read line");;

    match create_file(f, binput.as_bytes()) {
        Ok(()) => {
            match read_file(f, &mut buf) {
                Ok(()) => println!("{}", buf),
                Err(err) => println!("{:?}", err),
            }
        }
        Err(err) => println!("{:?}", err),
    }
}

fn create_file(filename: &str, buf: &[u8]) -> io::Result<()> {
    let mut f = try!(File::create(filename));
    try!(f.write(buf));
    Ok(())
}

fn read_file(filename: &str, mut buf: &mut String) -> io::Result<()> {
    let mut f = try!(File::open(filename));
    try!(f.read_to_string(&mut buf));
    Ok(())
}
