#[cfg(target_os = "linux")]
fn are_you_on_linux() {
    println!("you are running linux");
}

#[cfg(not(target_os = "linux"))]
fn are_you_on_linux() {
    println!("you are not in linux");
}

fn main() {
    are_you_on_linux();

    println!("are you sure?");

    if cfg!(target_os = "linux") {
        println!("you are in linux");
    } else {
        println!("you are not in linux");
    }
}
