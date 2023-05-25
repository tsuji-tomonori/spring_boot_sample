package com.example.demo;

import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;
import org.springframework.web.bind.annotation.*;

@SpringBootApplication
@RestController
public class DemoApplication {

	public static void main(String[] args) {
		SpringApplication.run(DemoApplication.class, args);
	}
	public Book[] books = {
			new Book("978-4-04-427-101-5", "氷菓"),
			new Book("978-4-8002-1747-9", "響け！ユーフォニアム 北宇治高校吹奏楽へようこそ"),
			new Book("978-4-04-891421-5", "安達としまむら")
	};

	Book serchBook(String isbn){
		for(Book book: books){
			if (book.isbn().equals(isbn))
				return book;
		}
		return null;
	}

	@GetMapping("/book/{isbn}")
	Book getBook(@PathVariable("isbn") String isbn){
		return serchBook(isbn);
	}

}
