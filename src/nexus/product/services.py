from django.db import connection

def dictfethall(cursor):
    columns = [col[0] for col in cursor.description]
    return [
        dict(zip(columns, row))
        for row in cursor.fetchall()
    ]

def dictfetchone(cursor):
    row = cursor.fetchone()
    if row is None:
        return False
    columns = [col[0] for col in cursor.description]
    return dict(zip(columns, row))



def get_latest_products(count):
    with connection.cursor() as cursor:
        cursor.execute(f"""
            select pp.*, cc.name as category_name, gc.name as city_name, pp2.image as product_image,
            uu.firstname || ' ' || uu.last_name as fullname
            from product_product pp 
            inner join category_category cc on cc.id = pp.category_id 
            inner join geo_city gc on gc.id = pp.city_id 
            inner join user_user uu on uu.id = pp.user_id 
            inner join product_productimage pp2 on pp2.product_id = pp.id and pp2.is_main is true  
            order by pp.post_date desc
            limit {count}    
        """)
        data = dictfethall(cursor)
        return data


def one_product(**kwargs):
    with connection.cursor() as cursor:
        if kwargs.get("city_id") and kwargs.get("category_id"):
            where = f"""where gc.id = {kwargs.get("city_id")} and cc.id = {kwargs.get("category_id")}"""
            # print(where)
        elif kwargs.get("city_id"):
            where = f"""where gc.id = {kwargs.get("city_id")}"""
            # print(where)
        elif kwargs.get("category_id"):
            where = f"""where cc.id = {kwargs.get("category_id")}"""
            # print(where)
        else:
            where= ''
        cursor.execute(f"""
            select pp.*, cc.name as category_name,gc.name as city_name, pp2.image as product_image,
            uu.firstname || ' ' || uu.last_name as fullname
            from product_product pp 
            inner join category_category cc on cc.id = pp.category_id 
            inner join geo_city gc on gc.id = pp.city_id 
            inner join user_user uu on uu.id = pp.user_id 
            inner join product_productimage pp2 on pp2.product_id = pp.id and pp2.is_main is true
            {where}
        """)
        data = dictfethall(cursor)
        return data


def view_detail(**kwargs):
    with connection.cursor() as cursor:
        cursor.execute(f"""
            select pp.*, cc.name as category_name,gc.name as city_name,
            uu.firstname || ' ' || uu.last_name as fullname, array_agg(pp2.image) AS product_image
            from product_product pp 
            inner join category_category cc on cc.id = pp.category_id 
            inner join geo_city gc on gc.id = pp.city_id 
            inner join user_user uu on uu.id = pp.user_id 
            inner join product_productimage pp2 on pp2.product_id = pp.id 
            where pp.id = {kwargs.get("product_id")}
            group by pp.id , cc.name, gc.name,uu.firstname , uu.last_name
        """)

        return dictfetchone(cursor)




