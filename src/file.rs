use std::fs::File;
use std::io::prelude::*;
use serde::{Deserialize, Serialize};

#[derive(Serialize, Deserialize)]
pub struct Config {
    pub name: String,
    pub enabled: bool,
    pub dev_branch: String,
    pub dev_hash: String,
    pub master_branch: String,
    pub master_hash: String,
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

pub fn read_dev_hash(config: &Config) -> bool {
    let path = format!("{}{}{}", &config.path, "/.git/refs/heads/", &config.dev_branch);
    let mut file = File::open(path).expect("Could not read file");
    let mut content = String::new();
    file.read_to_string(&mut content).expect("Could not read file.");
    if content.trim() == config.dev_hash {
        return true;
    } else {
        return false;
    }
}


pub fn read_master_hash(config: &Config) -> bool {
    let path = format!("{}{}{}", &config.path, "/.git/refs/heads/", &config.master_branch);
    let mut file = File::open(path).expect("Could not read file");
    let mut content = String::new();
    file.read_to_string(&mut content).expect("Could not read file.");
    if content.trim() == config.master_hash {
        return true;
    } else {
        return false;
    }
}
