use std::error::Error;
use std::num::ParseIntError;
use std::fs::File;
use std::io::Read;
use std::path::Path;


/// Option<T> {
///   Some(T),
///     None
/// }
fn find(haystack: &str, needle: char) -> Option<usize> {
    for (offest, c) in haystack.char_indices() {
        if c == needle {
            return Some(offest);
        }
    }

    None
}

/// Result
/// enum Result<T, E> {
///     Ok(T),
///     Err(E),
/// }
fn double_int(number_str: &str) -> i32 {
    2 * number_str.parse::<i32>().unwrap()
}

fn double_int2(number_str:&str) -> Result<i32, ParseIntError> {
    number_str.parse::<i32>().map(|n| n *2)
}

fn file_double<P: AsRef<Path>>(file_path: P) -> Result<i32, String> {
    File::open(file_path)
         .map_err(|err| err.to_string())
         .and_then(|mut file| {
              let mut contents = String::new();
              file.read_to_string(&mut contents)
                  .map_err(|err| err.to_string())
                  .map(|_| contents)
         })
         .and_then(|contents| {
              contents.trim().parse::<i32>()
                      .map_err(|err| err.to_string())
         })
         .map(|n| 2 * n)
}

/// try!
fn file_double2<P: AsRef<Path>>(file_path: P) -> Result<i32, Box<Error>> {
    let mut file = try!(File::open(file_path));
    let mut contents = String::new();
    try!(file.read_to_string(&mut contents));
    let n = try!(contents.trim().parse::<i32>());
    Ok(2*n)
}

fn main() {
    let filename = "error_handing.rs";
    match find(&filename, '.') {
        Some(i) => println!("got at {}", i),
        None => println!("not"),
    }
    println!("{:?}", find(&filename, '.').map(|x| &filename[x + 1..])); //Some("rs")
    //println!("{:?}", find("test", '.').unwrap()); panic
    println!("{}", find("test", '.').unwrap_or(0)); //0

    println!("{}", double_int("10"));
    //println!("{}", double_int("abc")); //thread 'main' panicked at 'called `Result::unwrap()` on an `Err` value: ParseIntError { kind: InvalidDigit }'

    match double_int2("0a") {
        Ok(n) => println!("{}", n),
        Err(err) => println!("{:?}", err), //ParseIntError { kind: InvalidDigit }
    }

    match file_double("foo") {
        Ok(n) => println!("{}", n),
        Err(err) => println!("Error: {}", err),
    }

    match file_double2("foo") {
        Ok(n) => println!("{}", n),
        Err(err) => println!("Error: {}", err),
    }
}
