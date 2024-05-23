from datetime import datetime
import json
from django.shortcuts import render
from django.http import JsonResponse
from myapp.models import Comment, Post,User

def addPost(request,id):
    if request.method == 'POST':
        data = json.loads(request.body)
        title = data.get('title')
        description = data.get('description')
        pic = data.get('pic')
        
        try:
            post = Post(title=title,description=description,pic=pic,nbLikes=0,comments=[],date=datetime.now(),user=id)
            post.save()
            post_info={
                    'id': str(post.id),
                    'title': post.title,
                    'description': post.description,
                    'pic': post.pic,
                    'nbLikes': post.nbLikes,
                    'comments': post.comments,
                    'date': post.date.isoformat(),
                    'user': {
                        'id': str(post.user.id),
                        'fullname': post.user.fullname,
                        'username': post.user.username,
                        'mail': post.user.mail
                    }
                }
            return JsonResponse({'message': 'post created successfully','post':post_info}, status=201)
        except Exception as e:
            print('Error:', e)
            return JsonResponse({'error': 'Failed to save post'}, status=500)

    else:
        return JsonResponse({'error': 'Only POST method is allowed'}, status=405)
    

def deletePost(request,id):
    if request.method == 'DELETE':
        try:
            post = Post.objects.get(id=id)
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
                comment_list=[]
                for comment in post.comments:
                    comment_list.append({
                        'id':str(comment.id),
                        'description':comment.description,
                        'user':{
                                'id': str(comment.user.id),
                                'fullname': comment.user.fullname,
                                'username': comment.user.username,
                                'mail': comment.user.mail
                            },
                        'date':comment.date.isoformat()
                    })
                
                # user = User.objects.get(id=post.user.id)
                # if not user:
                #     raise ValueError("User not found")
                post_list.append({
                    'id': str(post.id),
                    'title': post.title,
                    'description': post.description,
                    'pic': post.pic,
                    'nbLikes': post.nbLikes,
                    'comments': comment_list,
                    'date': post.date.isoformat(),
                    'user': {
                        'id': str(post.user.id),
                        'fullname': post.user.fullname,
                        'username': post.user.username,
                        'mail': post.user.mail
                    }
                })
            return JsonResponse(post_list,safe=False)
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)
    else:
        return JsonResponse({'error': 'Only GET method is allowed'}, status=405)
    
def create_comment(request, idP, idU):
    try:
        post = Post.objects.get(id=idP)
        user = User.objects.get(id=idU)
    except (Post.DoesNotExist, User.DoesNotExist):
        return JsonResponse({'error': 'Post or User not found'}, status=404)
    
    data = json.loads(request.body)
    description = data.get('description')
    
    if not description:
        return JsonResponse({'error': 'Description is required'}, status=400)
    
    comment = Comment.objects.create(user=user, description=description, date=datetime.now())
    post.comments.append(comment)
    comment_info={
        'id':str(comment.id),
        'description':comment.description,
        'user':{
                'id': str(comment.user.id),
                'fullname': comment.user.fullname,
                'username': comment.user.username,
                'mail': comment.user.mail
            },
        'date':comment.date.isoformat()
    }
    post.save()
    return JsonResponse({'message': 'Comment created successfully','comment':comment_info},status=201)

def delete_comment(request, idP, idC):
    try:
        post = Post.objects.get(id=idP)
        comment = Comment.objects.get(id=idC)
    except (Post.DoesNotExist, Comment.DoesNotExist):
        return JsonResponse({'error': 'Post or Comment not found'}, status=404)
    
    if comment not in post.comments:
        return JsonResponse({'error': 'Comment does not belong to this post'}, status=400)
    
    comment.delete()
    post.comments.remove(comment)
    post.save()
    
    return JsonResponse({'message': 'Comment deleted successfully'})

