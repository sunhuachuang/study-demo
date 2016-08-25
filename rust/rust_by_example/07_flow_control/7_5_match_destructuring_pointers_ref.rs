fn main() {
    let reference = &4;

    match reference {
        &val => println!("got the destructuring: {:?}", val),
    }

    match *reference {
        val => println!("got the deferencing: {:?}", val),
    }

    let _not_a_reference = 3;

    let ref _is_a_referece = 3;

    let value = 5;
    let mut mut_value = 5;
    let test = 3;
    let mut mut_test = 7;

    match test {
        val => println!("this is a {}", val),
    }

    match mut_test {
        ref mut val => {
            *val += 5;
            println!("mut_test is {}", val)
        }
    }

    match value {
        ref r => println!("got a refernce to a value: {}", r),
    }

    match mut_value {
        ref mut m => {
            *m += 10;
            println!("we add 10 the m is {:?}", m)
        }
    }
}
