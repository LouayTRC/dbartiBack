import bcrypt
from django.http import JsonResponse
import json

from myapp.models import User,Admin
import jwt

def register(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        username = data.get('username') 
        fullname = data.get('fullname') 
        password = data.get('password') 
        mail = data.get('mail')
        pic = data.get('pic')
        if username and fullname and mail and password and pic:
            try:
                if User.objects(username=username).first():
                    return JsonResponse({'error': 'Username already taken'}, status=400)
                if User.objects(mail=mail).first():
                    return JsonResponse({'error': 'Email already registered'}, status=400)
            
                hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())

                user = User(**data)
                user.password=hashed_password.decode('utf-8')
                user.role='USER'
                print('u',user)
                user.save()
                return JsonResponse({'message': 'User registered successfully'}, status=201)
            except Exception as e:
                print('Error:', e)
                return JsonResponse({'error': 'Failed to register'}, status=500)
        else:
            return JsonResponse({'error': 'Missing info: name or password'}, status=400)
    else:
        return JsonResponse({'error': 'Only POST method is allowed'}, status=405)



def login(request):
    secretKey="sdmfnqskmdl,fvlsmdf5s53f1ds6f65@QSDQ"
    if request.method == 'POST':
        data = json.loads(request.body)
        username = data.get('username')  # Assuming the key for the username is 'username'
        password = data.get('password')  # Assuming the key for the password is 'password'
        if username and password:
            try:
                user = User.objects.get(username=username)
                user_res={
                    'id':str(user.id),
                    'username':user.username,
                    'fullname':user.fullname,
                    'password':user.password,
                    'role':user.role,
                    'pic':user.pic,
                }
                
                if bcrypt.checkpw(password.encode('utf-8'), user.password.encode('utf-8')):

                    token = jwt.encode({'username': username}, secretKey , algorithm='HS256')
                   
                    return JsonResponse({'token': token,'user':user_res}, status=200)
                else:
                    return JsonResponse({'error': 'Invalid credentials'}, status=401)
            except User.DoesNotExist:
                return JsonResponse({'error': 'User not found'}, status=404)
            except Exception as e:
                print('Error:', e)
                return JsonResponse({'error': 'Login failed'}, status=500)
        else:
            return JsonResponse({'error': 'Missing username or password'}, status=400)
    else:
        return JsonResponse({'error': 'Only POST method is allowed'}, status=405)


# def createAdmin(request):
#     if request.method == 'POST':
#         data = json.loads(request.body)
#         username = data.get('username') 
#         fullname = data.get('username') 
#         password = data.get('username') 
#         mail = data.get('mail')
#         if username and fullname and mail and password:
#             try:
                
#                 hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())

#                 user = User(**data)
#                 user.password=hashed_password.decode('utf-8')
#                 user.role='ADMIN'
#                 print('u',user)
#                 user.save()

#                 admin=Admin(user)
#                 admin.save()

#                 return JsonResponse({'message': 'admin registered successfully'},admin, status=201)
#             except Exception as e:
#                 print('Error:', e)
#                 return JsonResponse({'error': 'Failed to register'}, status=500)
#         else:
#             return JsonResponse({'error': 'Missing info: name or password'}, status=400)
#     else:
#         return JsonResponse({'error': 'Only POST method is allowed'}, status=405)

def createAdmin(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        username = data.get('username')
        fullname = data.get('fullname')
        password = data.get('password')
        mail = data.get('mail')
        
        if username and fullname and mail and password:
            try:
                # Check if the username or email already exists
                if User.objects(username=username).first():
                    return JsonResponse({'error': 'Username already taken'}, status=400)
                if User.objects(mail=mail).first():
                    return JsonResponse({'error': 'Email already registered'}, status=400)
                
                # Hash the password
                hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())

                # Create the user
                user = User(
                    username=username,
                    mail=mail,
                    password=hashed_password.decode('utf-8'),
                    fullname=fullname,
                    role='ADMIN'
                )
                user.save()
                
                # Create the admin
                admin = Admin(user=user)
                admin.save()
                
                return JsonResponse({'message': 'User registered successfully'}, status=201)
            except Exception as e:
                print('Error:', e)
                return JsonResponse({'error': 'Failed to register'}, status=500)
        else:
            return JsonResponse({'error': 'Missing info: username, fullname, email, or password'}, status=400)
    else:
        return JsonResponse({'error': 'Only POST method is allowed'}, status=405)