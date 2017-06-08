/// Borrow => AsRef
/// BorrowMut => AsMut
/// ToOwned    => Clone

fn main() {
    is_hello("hello");
    is_hello("hello".to_string());
}

fn is_hello<T: AsRef<str>>(s: T) {
    assert_eq!("hello", s.as_ref());
}
