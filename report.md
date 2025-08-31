# OWASP Django Demo (Introduction to Cyber Security Project Essay)

GitHub Link: https://github.com/ozkanali357/Introduction-to-Cybersecurity-Project-1.git

## Introduction

As the final project of the course Introduction to Cyber Security, five commmon web application vulnerabilities from the OWASP Top Ten (2021) were selected, demonstrated and solved in a demo Django web application. The purpose was to make developers see, observe, understand these flaws, their reasons and their fixes to adopt safe, appropriate web development practices in a real project. This app shows the different steps in a webpage and how users interact with it such as authenticating, accessing, submitting documents. In this report, the setup instructions are present. More importantly, the flaws and the commented-out fixes in the codebase are shown and explained.

## Installation

The below steps are to run the project locally:

1. The repository is cloned.
   ```
   git clone https://github.com/yourusername/django-owasp-demo.git
   cd django-owasp-demo
   ```

2. A virtual environment is created.
   ```
   python3 -m venv venv
   source venv/bin/activate
   ```

3. The dependencies are installed.
   ```
   pip install -r requirements.txt
   ```

4. Migrations are applied.
   ```
   python manage.py migrate
   ```

5. The development server is ran.
   ```
   python manage.py runserver
   ```

6. The application is accessed.
   The user should go to these links in the browser. (http://127.0.0.1:8000). Login with a valid username and password such as "alice" and "password123" or "bob" and "password456" here "http://127.0.0.1:8000/vulnerabilities/broken-authentication/".

7. This is the Django admin URL. (http://127.0.0.1:8000/admin/)

## Vulnerabilities

In this section, the five vulnerabilities selected and illustrated from OWASP 2021 is listed with the ID's assigned to these flaws in the original website (https://owasp.org/Top10/). The links to the demonstrations and fixes of these flaws are also highlighted, which sends the user directly to the code line in the code files where the flaw or fix is applied. Moreover, browser screenshots of the flawed and fixed states of the app are also provided in the repository folder for visual comparison.

### Flaw 1: A01:2021-Broken Access Control
Location: views.py, `insecure_direct_object_reference.html`

Description: https://github.com/ozkanali357/Introduction-to-Cybersecurity-Project-1/blob/main/vulnerabilities/views.py#L8
- When the users put a `doc_id` in the browser search bar such as `/vulnerabilities/insecure-direct-object-reference/?doc_id=1`, the app allows them to access that document. The users should only reach documents which belong to them rather than other users' ones. However, the flaw is that there is no checks done to verify that the document belongs to the user which sent the request. Therefore, any registered, authenticated user can access any document in the app (including other users' documents) by just changing the `doc_id` parameter.

Demonstration: First of all, the user should go to this link (http://127.0.0.1:8000/vulnerabilities/broken-authentication/) and login with a valid username and password such as "alice" and "password123". After logging in, the user can visit a URL which shows the contents of a document with ID 1 (http://127.0.0.1:8000/vulnerabilities/insecure-direct-object-reference/?doc_id=1) after that, the user can change the ID number to 2 to access documents belonging to other users (http://127.0.0.1:8000/vulnerabilities/insecure-direct-object-reference/?doc_id=2). It can be seen who does the documents belong to in the admin pannel.

Fix: An authorization check is added to be sure that when a user requests a document, the app looks if it belongs to the user. After this fix, only the owner of the document can access it.
  
Summary: This vulnerability portrayed that if access control is missing, then it can end up with unauthorized users accessing to sensitive resources. As a fix, becore granting access, resource ownership is checked.

### Flaw 2: A07:2021-Identification and Authentication Failures
Location: views.py, `broken_authentication.html`

Description: https://github.com/ozkanali357/Introduction-to-Cybersecurity-Project-1/blob/main/vulnerabilities/views.py#L29
- Passwords are stored and checked in plaintext, and if there are multiple failed attempts to login, there is no account lockout. Furthermore, there is no secure authentication and password hashing. For this reason, the system is open to attacks and database leaks.

Demonstration: http://127.0.0.1:8000/vulnerabilities/broken-authentication/
- The user should navigate to `/vulnerabilities/broken-authentication/` and try logging in with any username and password from the database like `alice`, `password123`. There is no account lockout or password hashing.

Fix: Django’s built-in authentication system should be used. It securely hashes passwords, supports account lockout and other security features.

Summary: This flaw conveys that weak authentication can result in attackers getting into accounts. Using Django’s secure authentication system, enforce account lockout and password hashing is the optimal solution.

### Flaw 3: A03:2021-Injection
Location: views.py, `cross_site_scripting.html`

Description: https://github.com/ozkanali357/Introduction-to-Cybersecurity-Project-1/blob/main/vulnerabilities/views.py#L56
- Without escaping the user input is rendered. This allows attackers to inject and execute malicious scripts in the browser. For instance, a JavaScript alertteri will be triggered if `<script>alert('XSS')</script>` is entered.

Demonstration: http://127.0.0.1:8000/vulnerabilities/cross-site-scripting/
- The user should go to `/vulnerabilities/cross-site-scripting/`, enter `<script>alert('XSS')</script>` in the input box and submit. The script will work in the browser.

Fix: If the user input is escaped before rendering it in the template the problem can be solved. This can be done by removing the `|safe` filter or escaping input in the view.

Summary: This flaw indicates that unsanitized user inputs can lead to XSS attacks. The solution is to escape user input before rendering it in the browser.

Location: views.py, `sql_injection.html`

(Here is another problem connected with the same vulnerability. Trigger them separately, one by one.)

Description: https://github.com/ozkanali357/Introduction-to-Cybersecurity-Project-1/blob/main/vulnerabilities/views.py#L73
- With unsanitized user input, raw SQL queries are constructed. This allows SQL injection. For example, the query can be manipulated and unintended data can be accessed by entering `1 OR 1=1` as the user ID.

Demonstration: http://127.0.0.1:8000/vulnerabilities/sql-injection/
- When navigated to `/vulnerabilities/sql-injection/`, `1 OR 1=1` is entered as the user ID, and submitted. SQL injection is shown when the query returns all users.

Fix: If it is aimed to safely handle user input, parameterized queries or Django ORM methods should be used.

Summary: This problem critiques that SQL injection attacks can happen because of unsanitized user input. To prevent injection, parameterized queries or ORM methods is the fix.

### Flaw 4: A02:2021-Cryptographic Failures
Location: models.py, `cryptographic_failures.html`

Description: https://github.com/ozkanali357/Introduction-to-Cybersecurity-Project-1/blob/main/vulnerabilities/views.py#L97
- The password is displayed in the application because they are stored in plaintext in the database. Data breach possibilities increade dramaticaly because of this, as sensitive data is exposed. Attackers can see all of the users' passwords if they can access to the database or rendered page.

Demonstration: http://127.0.0.1:8000/vulnerabilities/cryptographic-failures/
- How sensitive data is exposed is shown through the page of `/vulnerabilities/cryptographic-failures/`. It has a table with all usernames and their plaintext passwords.

Fix: Thanks to Django's built-in password hashing functions, `make_password` and `check_password`, password hashing in the backend can be implemented. To never display passwords again, the password column from the template should be deleted as well.

Summary: Serious security risks can arise if senitive data is stored and shown in plaintext. Hashing passwords in the backend and never exposing them in the frontend is the healthy method to use.

### Flaw 5: A05:2021-Security Misconfiguration
Location: settings.py, `security_misconfiguration.html`

Description: https://github.com/ozkanali357/Introduction-to-Cybersecurity-Project-1/blob/main/vulnerabilities/views.py#L104
- Sensitive error information can be exposed if the application runs with `DEBUG=True`. Django will show a detailed error page with stack trace and configuration info when a user visits a non-existent URL.

Demonstration: http://127.0.0.1:8000/vulnerabilities/does-not-exist/
- When visited the page `/vulnerabilities/does-not-exist/` while `DEBUG=True`, Django will display a detailed error page.

Fix: `DEBUG=False` should be set `ALLOWED_HOSTS` should be configured in settings.py. The secret key should be stored securely using environment variables.

Summary: The lesson to take from this flaw is that misconfigured security settings can expose sensitive information. A supported practice is to disable debug mode and properly configure allowed hosts in production.

## References

- OWASP Top Ten 2021: https://owasp.org/Top10/
- Django Security Documentation: https://docs.djangoproject.com/en/4.2/topics/security/
