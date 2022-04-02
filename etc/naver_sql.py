import pymysql, requests


def PyMySQL_Test(jsonArray):

    con = pymysql.connect(host='localhost', user='root', password='1234', db='naver_search', charset='utf8')
    cur = con.cursor()

    for list in jsonArray:
        title = list.get('title')
        title = title.replace('<b>','')
        title = title.replace('</b>', '')
        sql = "INSERT INTO naver_search.shop_product (p_Id, p_title, p_image, p_lprice, p_brand, p_category1, p_category2, p_category3, p_category4) VALUES ('" + list.get('productId') + "', '" + title + "', '" + list.get('image') + "', '" + list.get('lprice') + "', '" + list.get('brand') + "', '" + list.get('category1') + "', '" + list.get('category2') + "', '" + list.get('category3') + "', '" + list.get('category4') +"')"
        cur.execute(sql)

    con.commit()
    con.close()


def request_db():
    url_items = "https://openapi.naver.com/v1/search/shop.json"

    headers = {
        "X-Naver-Client-Id": 'Z6Nt3iRF7GNH1kFgl365',
        "X-Naver-Client-Secret": 'npD_3zPwMC'
    }
    query_set1 = {'바지', '티셔츠', '치마', '모자', '운동화', '구두', '언더웨어', '홈웨어', '시계', '뷔스티에', '썬글라스', '원피스', '박스핏', '구찌', '톰브라운'}
    query_set2 = {'운동화', '구두', '서머룩', '윈터룩', '가을 컬렉션'}
    query_set3 = {'언더웨어', '홈웨어', '봄 컬랙션', '시계', '쥬얼리'}
    query_set4 = {'뷔스티에', '썬글라스', '원피스', '룩북', '박스핏'}
    query_set5 = {'구찌', '톰브라운', '입생로랑', '샤넬', '빈폴'}

    for query in query_set1:
        params = {
            'query': query,
            'display': '100'
        }
        response = requests.get(url_items, params=params, headers=headers)
        test_json = response.json()
        jsonarray = test_json.get('items')
        PyMySQL_Test(jsonarray)


if __name__ == '__main__':

    request_db()


