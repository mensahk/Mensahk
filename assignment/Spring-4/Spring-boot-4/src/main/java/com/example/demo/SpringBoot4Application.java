package com.example.demo;

import java.security.Principal;

import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;
import org.springframework.boot.autoconfigure.security.oauth2.client.EnableOAuth2Sso;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RestController;

@SpringBootApplication
@RestController
@EnableOAuth2Sso
public class SpringBoot4Application {

	@GetMapping("/")
	public String  Welcome2User(Principal principal) {
		return "Hi " + principal.getName()+"Welcome to Mensahk Web page";
	}
	
	public static void main(String[] args) {
		SpringApplication.run(SpringBoot4Application.class, args);
	}

}
