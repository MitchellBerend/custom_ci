#![feature(proc_macro_hygiene, decl_macro)]
#[macro_use] extern crate rocket;


// index
// Created so the landing page exists and can direct to other endpoints.
//
// WIP
// 
//
#[get("/")]
fn index() -> String {
    format!("Landing page.")
}


// pipeline
// Endpoint for creating new and managing existing pipelines.
//
//
#[get("/")]
fn get_pipeline() ->  String { //name: String, path: String, master_branch: String, master_hash: String, feature_branch: String, feature_hash: String, test_path: String) -> String {
    // Takes 7 argumetns, all strings.
    // Adds pipeline model instance to database
    format!("Not implemented yet.")
}


#[post("/")]
fn post_pipeline() ->  String { //name: String, path: String, master_branch: String, master_hash: String, feature_branch: String, feature_hash: String, test_path: String) -> String {
    // Takes 7 argumetns, all strings.
    // Adds pipeline model instance to database
    format!("Not implemented yet.")
}


#[put("/")]
fn put_pipeline() -> String {
    format!("Not implemented yet.")
}


#[delete("/")]
fn delete_pipeline() -> String {
    format!("Not implemented yet.")
}


// see current piplines
//
#[get("/")]
fn get_current_pipelines() -> String {
    format!("Not implemented yet.")
}


// check current pipeline status
//
#[get("/")]
fn get_current_status() -> String {
    format!("Not implemented yet.")
}


//rebuild pipeline
//
#[post("/")]
fn post_rebuild() -> String {
    format!("Not implemented yet.")
}


// main
// 
fn main() {
    rocket::ignite()
        .mount("/", routes![index])
        .mount("/pipeline", routes![get_pipeline, post_pipeline, put_pipeline, delete_pipeline])
        .mount("/manage", routes![get_current_pipelines])
        .mount("/rebuild", routes![post_rebuild]) 
        .launch();
}

