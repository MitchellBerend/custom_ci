mod file;

fn main() {
    let t = file::read_conf();
    file::read_dev_hash(&t);
    file::read_master_hash(&t);
    // file::merge_branch();
}
