use std::borrow::Cow;

fn main() {
    let mut cow: Cow<[_]> = Cow::Owned(vec![1, 2, 3]);
    let hello = cow.to_mut();
    assert_eq!(hello, &[1, 2, 3]);

    let cow2: Cow<[_]> = Cow::Owned(vec![1, 2, 3]);
    let hello2 = cow2.to_owned();
    assert_eq!(hello2, vec![1, 2, 3]);

    let mut a: Cow<[_]> = Cow::Owned(vec![-1, 2, -3]);
    abs_all(&mut a);
    println!("{:?}", a);

    let a1 = remove_spaces("abc def");
    let a2 = remove_spaces("abcdef");
    println!("{:?}", a1);
    println!("{:?}", a2);
    assert_eq!(a1, a2);
}

fn abs_all(input: &mut Cow<[i32]>) {
    for i in 0..input.len() {
        let v = input[i];
        if v < 0 {
            // clones into a vector the first time (if not already owned)
            input.to_mut()[i] = -v;
        }
    }
}

fn remove_spaces<'a>(input: &'a str) -> Cow<'a, str> {
    if input.contains(' ') {
        let mut buf = String::with_capacity(input.len());

        for c in input.chars() {
            if c != ' ' {
                buf.push(c);
            }
        }

        return Cow::Owned(buf);
    }

    return Cow::Borrowed(input);
}
