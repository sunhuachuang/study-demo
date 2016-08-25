#[allow(dead_code)]
#[derive(Clone, Copy)]

struct Book {
    title:  &'static str,
    author: &'static str,
    year:   u32,
}

fn borrow_book(book: &Book) {
    println!("I borrow book {}, year {}", book.title, book.year);
}

fn mut_borrow_book(book: &mut Book) {
    book.year = 2015;
}

fn main() {
    let abook = Book {
        title: "a-title",
        author: "a-author",
        year: 2000,
    };

    borrow_book(&abook);
    //mut_borrow_book(&mut abook);

    let mut bbook = Book {
        title: "b-book",
        author: "b-author",
        year: 1999,
    };

    borrow_book(&bbook);
    mut_borrow_book(&mut bbook);
    borrow_book(&bbook);
}
