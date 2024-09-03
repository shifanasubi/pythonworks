placements={"testing":45,"python":39,"bigdata":32,"asp":56,"java":60}
def get_value(key):
    return wc.get(key)
srt=sorted(wc,key=get_value,reverse=True)
print(srt)

