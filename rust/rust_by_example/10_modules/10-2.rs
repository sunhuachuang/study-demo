mod my {
    pub struct WhiteBox<T> {
        pub content: T,
    }

    #[allow(dead_code)]
    pub struct BlackBox<T> {
        content: T,
    }

    impl <T>BlackBox<T> {
        pub fn new(contents: T) ->BlackBox<T> {
            BlackBox{
                content: contents,
            }
        }
    }
}

fn main() {
    let while_box = my::WhiteBox { content: "public infomation" };

    println!("the while box content is {}", while_box.content);

    //can get the contrust for blackbox
    let _black_box = my::BlackBox::new("private infomation");

    //cannot get the content in _black_box.content
}
