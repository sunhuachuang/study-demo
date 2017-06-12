use std::sync::mpsc;
use std::thread;

// thread
fn create_new_thread() {
    let new_thread = thread::spawn(move || {
                                       println!("I am in a new thread");
                                   });
    new_thread.join().unwrap();

    let new_thread2_result = thread::Builder::new()
        .name("thread1".to_string())
        .stack_size(4 * 1024 * 1024)
        .spawn(move || {
                   println!("I am in a new thread");
               });
    new_thread2_result.unwrap().join().unwrap();
}

fn create_channel() {
    let (tx, rx): (mpsc::Sender<i32>, mpsc::Receiver<i32>) = mpsc::channel();
    thread::spawn(move || { tx.send(1).unwrap(); });
    let recv = thread::spawn(move || {
                                 let num = rx.recv().unwrap();
                                 println!("{}", num);
                             });

    recv.join().unwrap();
}

fn main() {
    create_new_thread();
    create_channel();
}
