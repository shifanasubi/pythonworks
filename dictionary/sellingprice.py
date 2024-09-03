# selling price calculate

mobile={"name":"motoedge14","brand":"moto","price":22000,"is_available":True,"offer":500}
if "offer" in mobile:
    selling_price=mobile.get("price")-mobile.get("offer")
    print(selling_price)
else:
    selling_price=mobile.get("price")
    print(selling_price)