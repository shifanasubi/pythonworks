# lenght

# from json import load
# f=open("C:\\Users\\USER\\Desktop\\PythonJuneWorks\\jsonWorks\\products.json","r",encoding="UTF-8")
# items=load(f)
#items=[{},{},......{}]
# print(len(items))
# products=load(f)
# print(len(products))


# productsnte title print cheyyan
from json import load
f=open("C:\\Users\\USER\\Desktop\\PythonJuneWorks\\jsonWorks\\products.json","r",encoding="UTF-8")
products=load(f)
# print(items.get("title"))
product_title=[p.get("title") for p in products]
# print(product_title)


#jewellery product category

# # jewellery_products=[i.get("title") for i in products if i.get("category")=="jewelery"]
# print(jewellery_products)

# product price>100

# product_price=[i.get("title")for i in products if i.get("price")>100]
# print(product_price)

# products in range of 100 to 150
# product_range=[i.get("title")for i in products if i.get("price")>=100 and i.get("price")<=150]
# print(product_range)

def get_rating_count(dic):
    return dic.get("rating").get("count")
top_selling_product=max(items,key=get_rating_count)
print(top_selling_product)


