use std::fs::File;
use std::io::prelude::*;
use serde::{Deserialize, Serialize};
use std::process::Command;

#[derive(Serialize, Deserialize)]
pub struct Config {
    pub name: String,
    pub enabled: bool,
    pub feature_branch: String,
    pub feature_hash: String,
    pub target_branch: String,
    pub target_hash: String,
    pub master_hash: String,
    pub master_branch: String,
    pub continuous_integration: bool,
    pub continuous_delivery: bool,
    pub path: String,
}


pub fn read_conf() -> Config {
    let mut file = File::open("conf.json").expect("Could not open file.");
    let mut content = String::new();
    file.read_to_string(&mut content).expect("Could not read file.");
    let data: Config = serde_json::from_str(&content).expect("Could not serialize json.");

    return data;
}


pub fn read_feature_hash(config: &Config) -> bool {
    let path = format!("{}{}{}", &config.path, "/.git/refs/heads/", &config.feature_branch);
    let mut file = File::open(path).expect("Could not read file");
    let mut content = String::new();
    file.read_to_string(&mut content).expect("Could not read file.");
    if content.trim() == config.feature_hash {
        return true;
    } else {
        return false;
    }
}


pub fn read_target_hash(config: &Config) -> bool {
    let path = format!("{}{}{}", &config.path, "/.git/refs/heads/", &config.target_branch);
    let mut file = File::open(path).expect("Could not read file");
    let mut content = String::new();
    file.read_to_string(&mut content).expect("Could not read file.");
    println!("{}", config.path);
    if content.trim() == config.target_hash {
        return true;
    } else {
        return false;
    }
}


pub fn merge_branch(feature_branch: &String, master_branch: &String) {
    // git -C path checkout feature_branch && git merge master_branch && run tests && git -C path
    // checkout  master_branch
    let mut shell = Command::new("bash");
    let command = format!("git checkout", );
    shell
        .arg("-c")
        .arg("/home/mitchell/testy/target/debug/testy");
    let o = String::from_utf8(shell.output().expect("Couldnt read std in/err").stdout).unwrap();
    println!("{:#?}", o.trim());

}



