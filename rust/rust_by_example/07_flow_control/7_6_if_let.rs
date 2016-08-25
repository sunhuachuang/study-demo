#[allow(non_snake_case)]
fn main() {
    let number = Some(7);
    let letter: Option<i32> = None;
    let emotion: Option<i32> = None;

    if let Some(i) = number {
        println!("match: {:?}", i);
    }

    if let Some(i) = letter {
        println!("match {:?}", i);
    } else {
        println!("donot match");
    }

    let i_like_letters = false;

    if let Some(i) = emotion {
        println!("match {:?}", i);
    } else if i_like_letters {
        println!("get an i like letters");
    } else {
        println!("get nothing")
    }

    let Option_test =  Some(4);
    if let Some(x) = Option_test {
        foo(x);
    } else {
        bar();
    }
    println!("{:?}", Option_test);
}

fn foo(x: i32) -> i32 {
    x + 1
}

fn bar() -> i32 {
    0
}
