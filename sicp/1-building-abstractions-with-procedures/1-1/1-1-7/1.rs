fn main() {
    println!("{}", sqrt(2));
}

fn sqrt(x: i32) -> f64 {
    sqrt_iter(1.0, x)
}

fn sqrt_iter(guess: f64, x: i32) -> f64 {
    if good_enough(guess, x) {
        guess
    } else {
        sqrt_iter(improve(guess, x), x)
    }
}

fn good_enough(guess: f64, x: i32) -> bool {
    self_abs(guess * guess - x) < 0.001
}

fn self_abs(x: i32) -> i32 {
    if x < 0 {
        -x
    } else {
        x
    }
}

fn improve(guess: f64, x: i32) -> f64 {
    (guess + x / guess) / 2
}
