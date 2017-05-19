//! this is first line
//! the second line
/// add one to a number given.
///
/// #Example:
///
/// let x = 5;
///
/// assert_eq!(6, add_one(x));
/// # fn add_one(x: i32) -> i32 {
/// #     x + 1
/// # }
/// ...
fn add_one(x: i32) -> i32 {
    x + 1
}

fn main() {
    let x = 5;
    assert_eq!(6, add_one(x));
}
