package com.kite.mm.member.controller;

import javax.servlet.http.HttpSession;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Controller;
import org.springframework.ui.Model;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RequestMethod;

import com.kite.mm.member.domain.MemberRequest;
import com.kite.mm.member.service.MemberLoginService;

//MemberLoginController: 로그인 데이터를 보내는 컨트롤러 클래스
@Controller
@RequestMapping("/member/login")
public class MemberLoginController {
	
	@Autowired
	MemberLoginService service;

	//loginForm 메서드: 로그인 폼을 보여주는 메서드
	//get방식으로 들어왔을 때 처리
	@RequestMapping(method = RequestMethod.GET)
	public String loginForm() {
	
		return "member/loginForm";
	}
	
	//login 메서드: 작성한 로그인 폼을 DB에 저장하도록 서비스 클래스에게 전달하는 메서드
	//커맨드형식 
	@RequestMapping(method = RequestMethod.POST)
	public String login(MemberRequest request, Model model, HttpSession httpsession ){
		
		//System.out.println(request);
		//System.out.println("요청 idx: " + request.getIdx() );
		
		MemberRequest result = service.login(request);
		boolean loginChk = false;
		//System.out.println("결과: " + result );
		//System.out.println("결과 idx: " + request.getIdx());
		
		if(result != null) {
			httpsession.setAttribute("loginInfo", request);
			loginChk = true;
			model.addAttribute("loginInfo", request);
		}
		
		model.addAttribute("loginChk", loginChk);
		
		return "member/login";
	}
	
}//MemberLoginController 컨트롤러 클래스 끝
