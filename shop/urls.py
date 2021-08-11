from django.urls import path
from shop import views

app_name = 'shop'

urlpatterns = [
    path('', views.index, name='index'),
    path('notice/', views.get_notice_list, name='get_notice_list'),
    path('notice/<int:notice_id>', views.notice_detail, name='notice_detail'),
    path('qna/', views.get_question_list, name='get_question_list'),
    path('qna/<int:question_id>', views.question_detail, name='question_detail'),
    path('review/', views.get_review_list, name='get_review_list'),
    path('review/<int:review_id>', views.review_detail, name='review_detail'),
    path('product/', views.get_product_list, name='get_product_list'),
    path('product/<int:product_id>', views.product_detail, name='product_detail'),
    path('basket/', views.get_shopbasket_list, name='get_shopbasket_list'),
    path('payment/result/', views.payment_result, name='payment_result'),
    path('mypage/', views.get_mypage, name='mypage'),

]