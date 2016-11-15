#![feature(step_by)]
fn main() {
    let n = 1000000;

    let mut prime_numbers = Vec::new();
    prime_numbers.push(2);

    if n <= 2 {
        println!("2");
    } else {
        'a: for x in (3..n).step_by(2) {
            'b: for y in &prime_numbers {
                if x%y == 0 {
                    continue 'a;
                }
            }
            prime_numbers.push(x);
        }

        println!("{:?}", prime_numbers.pop());
    }
}
