#![crate_type = "dylib"]
#![crate_name = "points"]
#![allow(unstable)]

// Based on http://blog.skylight.io/bending-the-curve-writing-safe-fast-native-gems-with-rust/
// by Yehuda Katz


use std::num::{Int, Float};

#[derive(Copy)]
pub struct Point { x: isize, y: isize }
struct Line { p1: Point, p2: Point }

impl Line {
  pub fn length(&self) -> f64 {
    let xdiff = self.p1.x - self.p2.x;
    let ydiff = self.p1.y - self.p2.y;
    ((xdiff.pow(2) + ydiff.pow(2)) as f64).sqrt()
  }
}

#[no_mangle]
pub extern "C" fn make_point(x: isize, y: isize) -> Box<Point> {
    Box::new(Point{x: x, y: y})
}

#[no_mangle]
pub extern "C" fn free_point(p: Box<Point>)  {
   drop(p);
}

#[no_mangle]
pub extern "C" fn get_distance(p1: Box<Point>, p2: Box<Point>) -> f64 {
    Line{p1: *p1, p2: *p2 }.length()
}
