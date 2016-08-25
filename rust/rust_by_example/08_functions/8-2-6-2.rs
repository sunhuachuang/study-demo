fn main() {
    let vec1 = vec![1, 2, 3];
    let vec2 = vec![1, 4, 3];

    let mut iter = vec1.iter();
    let mut into_iter = vec2.into_iter();

    println!("find 2 in vec1 is {:?}", iter.find(|&&x| x == 2));
    println!("find 2 in vec2 is {:?}", into_iter.find(|&x| x == 2));

    let array1 = [1, 2, 3];
    let array2 = [1, 2, 3];
    println!("find 2 in array1 is {:?}", array1.iter().find(|&&x| x == 2));
    println!("find 2 in array2 is {:?}", array2.into_iter().find(|&&x| x == 2));
}
