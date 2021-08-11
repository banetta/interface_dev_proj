from django.shortcuts import render, get_object_or_404
from .models import ShopBasket, Notice, Question, Product, Review, MyPage
from django.core.paginator import Paginator
# Create your views here.


def index(request):

    item_list = ShopBasket.objects.filter(s_ordered=True).order_by('-s_amount')[:10]
    new_list = Product.objects.order_by('-p_id')[:6]
    context = {
        "item": item_list,
        "new": new_list
    }
    return render(request, 'shop/index.html', context)


def get_notice_list(request):

    page = request.GET.get('page', '1')

    notice_list = Notice.objects.order_by('-n_date')

    paginator = Paginator(notice_list, 20)
    page_obj = paginator.get_page(page)

    context = {
        'notice_list': page_obj
    }

    return render(request, 'shop/notice_list.html', context)


def notice_detail(request, notice_id):
    notice = get_object_or_404(Notice, pk=notice_id)
    context = {
        'notice': notice
    }
    return render(request, 'shop/notice_detail.html', context)


def get_question_list(request):

    page = request.GET.get('page', '1')

    question_list = Question.objects.order_by('-q_date')

    paginator = Paginator(question_list, 20)
    page_obj = paginator.get_page(page)

    context = {
        'question_list': page_obj
    }

    return render(request, 'shop/question_list.html', context)


def question_detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    context = {
        'question': question
    }
    return render(request, 'shop/question_detail.html', context)


def get_review_list(request):
    page = request.GET.get('page', '1')
    review_list = Review.objects.order_by('-r_date')

    paginator = Paginator(review_list, 20)
    page_obj = paginator.get_page(page)

    context = {
        'review_list': page_obj
    }

    return render(request, 'shop/review_list.html', context)


def review_detail(request, review_id):
    review = get_object_or_404(Review, pk=review_id)
    context = {
        'review': review
    }
    return render(request, 'shop/review_detail.html', context)


def get_product_list(request):

    page = request.GET.get('page', '1')

    product_list = Product.objects.order_by('-p_id')

    paginator = Paginator(product_list, 18)
    page_obj = paginator.get_page(page)

    context = {
        'product_list': page_obj
    }
    return render(request, 'shop/product_list.html', context)


def product_detail(request, product_id):
    if request.method == 'POST':
        user_id = request.user



    product = get_object_or_404(Product, pk=product_id)
    context = {
        'product': product
    }
    return render(request, 'shop/product_detail.html', context)


def get_shopbasket_list(request):

    if request.method == 'POST':
        get_list = request.POST.getlist('basket_check[]')
        print(get_list)
        for buy in get_list:
            buy_list = ShopBasket.objects.filter(id=buy)

        context = {
            'buy_list': buy_list
        }
        return render(request, 'shop/payment_process.html', context)
    else:
        user_id = request.user.id

        if user_id:
            basket_list = ShopBasket.objects.filter(user_id=user_id)

            context = {
                'basket_list': basket_list
            }
            return render(request, 'shop/shopbasket_list.html', context)
        else:
            return render(request, 'shop/shopbasket_list.html')


def payment_result(request):
    if request.method == 'POST':
        get_list = request.POST.getlist('result_data[]')
        print(get_list)
        for get in get_list:
            ShopBasket.objects.filter(id=get).update(s_ordered=True)
            payment_list = ShopBasket.objects.filter(id=get)

        print(payment_list)
        context = {
            'payment_list': payment_list
        }
        return render(request, 'shop/payment_result.html', context)

    else:
        pass


def get_mypage(request):
    user_id = request.user.id

    if user_id:
        mypage_data = MyPage.objects.filter(user_id=user_id)

        context = {
            'data': mypage_data
        }
        return render(request, 'shop/mypage.html', context)
