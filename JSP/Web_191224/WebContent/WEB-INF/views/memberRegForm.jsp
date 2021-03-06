<%@ page language="java" contentType="text/html; charset=UTF-8"
	pageEncoding="UTF-8"%>
<%@ page trimDirectiveWhitespaces="true"%>
<!DOCTYPE html>
<html>
<head>
<title>회원가입</title>
<script src="https://code.jquery.com/jquery-1.12.4.js"
	integrity="sha256-Qw82+bXyGq6MydymqBxNPYTaUXXq7c8v3CwiYwLLNXU="
	crossorigin="anonymous"></script>
<link rel="stylesheet" href="191203_01.css">

<style>
* {
	margin: 0;
	padding: 0;
}
select.byear {
	width: 200px;
	height: 30px;
	font-size: 1.3em;
}


#nav {
	overflow: hidden;
	list-style: none;
	margin: 10px 0;
	border-top: 1px solid #999;
	border-bottom: 1px solid #999;
}

#nav>li {
	float: left;
	padding: 3px 30px;
}
</style>

</head>
<body>
<%@ include file="/WEB-INF/views/frame/header.jsp"%>
	<!-- 2em: 배수 표현, 기본 사이즈 16px -> 32px -->
	<h1 class="title">회원가입</h1>
	<hr>
	<form action="reg" method="post"> <!-- 상대 경로: /op/member/regForm -> /op/member/reg -->
		<table class="inputBox">
			<tr>
				<td>아이디(이메일)</td>
				<td><input type="text" name="uid"></td>
			</tr>

			<tr>
				<td>비밀번호</td>
				<td><input type="password" name="pw"></td>
			</tr>

			<tr>
				<td>이름</td>
				<td><input type="text" name="uname"></td>
			</tr>

			<tr>
				<td>성별</td>
				<td>남성<input type="radio" name="gender" value="m"> 여성<input
					type="radio" name=gender value="w">
				</td>
			</tr>

			<tr>
				<td>태어난 년도</td>
				<td><select id="byear" class="byear" name="byear">
						<!--  <option value="2000">2000</option>
                    <option>1999</option>
                    <option>1998</option>
                    <option>1997</option>
                    <option>1996</option>
                    <option>1995</option>-->
				</select></td>
			</tr>

			<tr>
				<td>프로필 사진</td>
				<td><input type="file" name="pflie"></td>
			</tr>

			<tr>
				<td></td>
				<td><input type="submit" value="회원가입"></td>
			</tr>
		</table>
	</form>

	<script>
		$(document).ready(function() {

			var selectOption = '';
			for (var i = 2019; i >= 1950; i--) {

				selectOption += '<option value='+i+'>' + i + '</option>\n';
				$('#byear').html(selectOption);
			}
		});
	</script>




</body>
</html>