from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.utils.html import escape
from django.db import connection
from .models import InsecureDirectObjectReference, User

# Flaw 1: A01:2021-Broken Access Control
def insecure_direct_object_reference(request):
    doc_id = request.GET.get('doc_id')
    document_content = None
    try:
        doc_id = int(doc_id)
        # Problem: owner not checked, with ID, any user can access any document
        document = InsecureDirectObjectReference.objects.get(id=doc_id)
        # Fix: user restricted to access only document they own
        # document = InsecureDirectObjectReference.objects.get(id=doc_id, user=request.user)
        if document.document:
            with document.document.open('r') as f:
                document_content = f.read()
    except (TypeError, ValueError, InsecureDirectObjectReference.DoesNotExist, Exception):
        return HttpResponse("Document not found or invalid ID.", status=404)
    return render(
        request,
        'vulnerabilities/insecure_direct_object_reference.html',
        {'document': document, 'document_content': document_content}
    )

# Flaw 2: A07:2021-Identification and Authentication Failures
def broken_authentication(request):
    # Problem: no account lockout, weak password check, no password hashing
    user = None
    error = None
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        try:
            user = User.objects.get(username=username, password=password)  # plaintext password check
        except User.DoesNotExist:
            error = "Invalid credentials"
    return render(request, 'vulnerabilities/broken_authentication.html', {'user': user, 'error': error})

    # Fix: Django authentication system, hashed passwords and lockout
    # from django.contrib.auth import authenticate, login
    # if request.method == 'POST':
    #     username = request.POST.get('username')
    #     password = request.POST.get('password')
    #     user = authenticate(request, username=username, password=password)
    #     if user is not None:
    #         login(request, user)
    #         return HttpResponse("Logged in successfully")
    #     else:
    #         return HttpResponse("Invalid credentials")
    # return render(request, 'vulnerabilities/broken_authentication.html')

# Flaw 3: A03:2021-Injection
def cross_site_scripting(request):
    user_input = ""
    if request.method == 'POST':
        user_input = request.POST.get('user_input', '')
    # Problem: not sanitized user input
    return render(request, 'vulnerabilities/cross_site_scripting.html', {'user_input': user_input})

    # Fix: escape user input in template, backend
    # return render(request, 'vulnerabilities/cross_site_scripting.html', {'user_input': escape(user_input)})

# Flaw 3: A03:2021-Injection
def sql_injection(request):
    user_id = request.GET.get('user_id', '')
    user_data = None
    if user_id:
        try:
# Flawed: weak to SQL injection
            with connection.cursor() as cursor:
                cursor.execute(f"SELECT username FROM vulnerabilities_user WHERE id = {user_id}")
                row = cursor.fetchone()
                if row:
                    user_data = row[0]
                else:
                    user_data = "No user found."
        except Exception as e:
            user_data = f"Error: {e}"
    return render(request, 'vulnerabilities/sql_injection.html', {'user_data': user_data})

# Fix: parameterized queries
#            with connection.cursor() as cursor:
#                cursor.execute("SELECT username FROM vulnerabilities_user WHERE id = %s", [user_id])
#                row = cursor.fetchone()
#                if row:
#                    user_data = row[0]
#                else:
#                    user_data = "No user found."
#        except Exception as e:
#            user_data = f"Error: {e}"
#    return render(request, 'vulnerabilities/sql_injection.html', {'user_data': user_data})

# Flaw 4: A02:2021-Cryptographic Failures
def cryptographic_failures(request):
    # Problem: show all users and passwords
    # Fix: don't display password, use password hashing in models.py and cryptographic_failures.html
    users = User.objects.all()
    return render(request, 'vulnerabilities/cryptographic_failures.html', {'users': users})

# Flaw 5: A05:2021-Security Misconfiguration
def security_misconfiguration(request):
    # Problem: DEBUG=True in settings.py
    return render(request, 'vulnerabilities/security_misconfiguration.html')
    # Fix: Set DEBUG=False and configure ALLOWED_HOSTS in settings.py