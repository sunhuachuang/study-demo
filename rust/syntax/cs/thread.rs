use std::thread;

fn main() {
    let handle = thread::spawn(||{
        "hello from a thread"
    });

    println!("{}", handle.join().unwrap());
}
