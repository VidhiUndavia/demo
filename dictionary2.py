book={}
print(book)

book['name']="Python"
book['price']=150
book['author']="abc"
print(book)

book["chapter"]=(1,2,3,4)
book["topics"]=["basic","list","set","tuple","dictionary"]
print(book)
book2=book.copy()
print(book2)
topic=["basic","list","set","tuple","dictionary"]
topic1=dict.fromkeys(topic)
print(topic1)
