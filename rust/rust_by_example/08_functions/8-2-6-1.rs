fn main() {
    let vec1 = vec![1, 2, 3];
    let vec2 = vec![1, 2, 3];

    println!("2 in vec1: {}", vec1.iter() .any(|&x| x == 2));
    println!("2 in vec2: {}", vec2.into_iter().any(|x| x == 2));

    let array1 = [1, 2, 3];
    let array2 = [1, 2, 3];

    println!("2 in array1: {}", array1.iter().any(|&x| x == 2));
    println!("2 in array2: {}", array2.into_iter().any(|&x| x == 2));
}
