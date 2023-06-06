use proconio::input;

fn main() {
    input! {
        x: u32,
        y: u32,
        z: u32,
    }

    let tmp: u32 = x;
    let x: u32 = y;
    let y: u32 = tmp;
    let _tmp: u32 = x;
    let x: u32 = z;
    let z: u32 = _tmp;
    println!("{} {} {}", x, y, z);
}
