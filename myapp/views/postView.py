from datetime import datetime
import json
from django.shortcuts import render
from django.http import JsonResponse
from myapp.models import Post

def addPost(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        title = data.get('title')
        description = data.get('description')
        pic = data.get('pic')
        post = Post(title=title,description=description,pic=pic,nb_likes=0,comments=[],date=datetime.now())
        try:
            post.save()
            return JsonResponse({'message': 'post created successfully'}, status=201)
        except Exception as e:
            print('Error:', e)
            return JsonResponse({'error': 'Failed to save post'}, status=500)

    else:
        return JsonResponse({'error': 'Only POST method is allowed'}, status=405)
    

def deletePost(request,id):
    if request.method == 'DELETE':
        try:
            post = Post.objects.get(_id=id)
            post.delete()
            return JsonResponse({'message': 'Post deleted successfully'})
        except Post.DoesNotExist:
            return JsonResponse({'error': 'Post not found'}, status=404)
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)
    else:
        return JsonResponse({'error': 'Only DELETE method is allowed'}, status=405)


def getAllPosts(request):
    if request.method == 'GET':
        try:
            posts = Post.objects.all()
            post_list = []
            for post in posts:
                post_list.append({
                    '_id': str(post._id),
                    'title': post.title,
                    'description': post.description,
                    'pic': post.pic,
                    'nb_likes': post.nb_likes,
                    'comments': post.comments,
                    'date': post.date.isoformat()
                })
            return JsonResponse({'posts': post_list})
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)
    else:
        return JsonResponse({'error': 'Only GET method is allowed'}, status=405)