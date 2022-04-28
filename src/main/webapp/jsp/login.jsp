<%@ page language="java" contentType="text/html; charset=ISO-8859-1"
    pageEncoding="ISO-8859-1"%>
<!DOCTYPE html>
<html>
<head>
<meta charset="ISO-8859-1">
<title>Insert title here</title>
</head>
<body>

<%

//fetching data from login form
String email = request.getParameter("email");
String password = request.getParameter("password");
String userRole = request.getParameter("desig");

//printing parameters value to screen
out.println("email: "+email+"<br/>");
out.println("password:"+password+"<br/>");
out.println("User role: "+userRole);

%>
</body>
</html>