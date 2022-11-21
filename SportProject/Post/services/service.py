from Post.models import Post
from django.db import transaction

class PostQuery():
    @transaction.non_atomic_requests
    def insertPost(img:str, namePost:str, location:str, description:str):
        post = Post(Img = img, Name = namePost, Location = location, Description = description)
        post.save()
        return "Post created."
    
    @transaction.non_atomic_requests
    def changeInfo(namePost:str, **info:str):
        post = Post.objects.get(Name = namePost)
        for key, value in info.items():
            match key:
                case "Name":
                    post.Name = value
                case "Location":
                    post.Location = value
                case "Description":
                    post.Description = value
                case "Img":
                    post.Img = value
                case _:
                    print(f"Field '{key}' not understood, transaction canceled")
            print(f"Field '{key}' can be changed")
        post.save()
                