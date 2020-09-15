mod file;

fn main() {
    let t = file::read_conf();
    println!("{}", t.name);

}
