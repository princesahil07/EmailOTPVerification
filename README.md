# EmailOTPVerification

Creating an email OTP (One-Time Password) verification web application in Django involves setting up a system where users receive a unique code 
via email to authenticate their identity. This process enhances security by ensuring that the email address provided is valid and belongs to the user. 
The implementation typically involves creating a user model and forms to handle registration and login. When a user registers or attempts to log in, 
the application generates a unique OTP and sends it to the user's email address using Django's built-in email functionality. The user must then enter this 
OTP into the application to complete the verification process. This OTP is usually time-limited and securely stored in the database, ensuring it cannot be 
reused or easily intercepted. Integrating Django's security features, such as token generation and hashing, ensures the robustness of the verification process, 
providing a secure and user-friendly method for email verification in web applications.

* User Login panel

![image](https://github.com/princesahil07/EmailOTPVerification/assets/97822056/a5207cec-a2de-4795-9cfe-a87923c65f6a)

* User register Panel

![image](https://github.com/princesahil07/EmailOTPVerification/assets/97822056/01362f18-0ad9-4a6a-941f-8604f39a0b72)

* OTP verification 

![image](https://github.com/princesahil07/EmailOTPVerification/assets/97822056/6e448d68-ea05-4a83-9f79-795d011d7e2f)
