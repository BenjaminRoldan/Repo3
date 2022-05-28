from django.urls import path
from Blog import views

urlpatterns = [
    path('', views.render_posts, name='blog'),
    path('post/<int:post_id>', views.post_detail, name='post_detail'),
    path('post/crear', views.add_post.as_view(), name='PostCreate'),
    path('post/delete/<pk>', views.delete_post.as_view(), name='PostDelete'),
    path('post/editar/<pk>', views.update_post.as_view(), name='PostUpdate'),
]