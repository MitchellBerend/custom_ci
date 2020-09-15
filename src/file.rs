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

