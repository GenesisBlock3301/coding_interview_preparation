package main

import "unsafe"

type hmap struct {
	count      int
	flags      uint8
	B          uint8
	neverflow  uint16
	hash0      uint32
	buckets    unsafe.Pointer
	oldbuckets unsafe.Pointer
	//extra *
}
