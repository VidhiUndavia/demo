book={}
print(book)

book['name']="Python"
book['price']=150
book['author']="abc"
print(book)

book["chapter"]=(1,2,3,4)
book["topics"]=["basic","list","set","tuple","dictionary"]
print(book)
print("Toppics = ",book["topics"])

book2=book.copy()
print(book2)
topic=["basic","list","set","tuple","dictionary"]
topic1=dict.fromkeys(topic)
print(topic1)
print(book.items())
print(book.keys())
print(book.values())
print(topic1.values())
print(topic1.keys())
topic1["basic"]="variables"
print(topic1.values())
print(book.popitem())
print(book)
print(book.pop("author"))
print(book)
topic1.clear()
print(topic1)