use std::sync::{Arc, Mutex};
use std::thread;
use std::sync::mpsc;

fn main() {
    /*
    let data = Arc::new(Mutex::new(0u32));

    let (tx, rx) = mpsc::channel();

    for _ in 0..10 {
        let (data, tx) = (data.clone(), tx.clone());

        thread::spawn(move || {
            let mut data = data.lock().unwrap();
            *data += 1;

            tx.send(());
        });
    }

    for _ in 0..10 {
        rx.recv();
    }
     */
    _channel_answer();
}

fn _channel_answer() {
    let (tx, rx) = mpsc::channel();

    for _ in 0..10 {
        let tx = tx.clone();

        thread::spawn(move || {
            let answer = 42u32;
            tx.send(answer);
        });
    }

    rx.recv().ok().expect("Could not receive answer");
}
