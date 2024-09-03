mobiles=[{"id":100,"title":"s23 ultra","brand":"samsung","price":125000,"network":"5g"},
        {"id":101,"title":"s23","brand":"samsung","price":54000,"network":"4g"},
        {"id":102,"title":"edge14pro","brand":"moto","price":25000,"network":"5g"},
        {"id":103,"title":"edgeneo","brand":"moto","price":22000,"network":"4g"},
        {"id":104,"title":"redminote10pro","brand":"mi","price":25000,"network":"5g"},
        {"id":105,"title":"redmi13","brand":"mi","price":12000,"network":"4g"},

]
# print all mobile names
# all_mobile_names=[mob.get("title") for mob in mobiles ]
# print(all_mobile_names)

# print all brands
# all_brand_names=[mob.get("brand")for mob in mobiles]
# print(set(all_brand_names))

# print samsung mobile names
# samsung_mobile_names=[mob.get("title")for mob in mobiles if mob.get("brands")=="samsung"]
# print(set(samsung_mobile_names))


# print all mobiles available in range of 23k to 40k
# available_range=[mob.get("title") for mob in mobiles if mob.get("price") in range(23000,40001)]
# print(available_range)

def get_price(mob):
     return mob.get("price")
# costly_mobile=max(mobiles,key=get_price)
# print(costly_mobile)
# cheep_mobile=min(mobiles,key=get_price)
# print(cheep_mobile)

# sorted_mobiles=sorted(mobiles,key=get_price,reverse=True)
# print(sorted_mobiles)

total_cost=sum([mob.get("price")for mob in mobiles])
print(total_cost)
