from django.urls import path

from . import views


urlpatterns = [
    path("", views.index, name="index"),
    path('home/', views.home, name='home'),
    path('profile/<str:username>', views.profile, name='profile'),
    path('registration/', views.registration, name='registration'),
    path('login/', views.user_login, name='login'),
    path('sample_profile/', views.sample_profile, name='sample_profile'),
    path('leaderboard/', views.leaderboard, name='leaderboard'),
    path('make_post/', views.make_post, name='make_post'),
    path('village/<str:username>', views.village, name='village'),
    path('village_shop/', views.village_shop, name='village_shop'),
    path('logout/', views.logout_view, name='logout'),
    path('map/', views.map, name='map'),
    path('privacy_policy/', views.privacy_policy, name='privacy_policy'),
    path('terms_conditions/', views.terms_conditions, name='terms_conditions'),
    path('remove_item/', views.remove_item, name='remove_item'),
    path('gamekeeper/', views.gamekeeper, name='gamekeeper'),
    path('products/', views.product_list, name='product_list'),
    path('product/<int:id>/', views.product_detail, name='product_detail'),
    path('payment/', views.payment_view, name='payment'),
    path('payment_success/', views.payment_success, name='payment_success'),
    path('payment_error/', views.payment_error, name='payment_error'),
    path('lauren/', views.lauren, name='lauren'),
    

]
