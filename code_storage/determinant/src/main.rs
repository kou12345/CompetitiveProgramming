use proconio::input;

fn main() {
    /*
    input
    a b
    c d
     */
    input! {
        a: i32,
        b: i32,
        c: i32,
        d: i32
    }

    let output: i32 = a * d - b * c;
    println!("{}", output);
}
