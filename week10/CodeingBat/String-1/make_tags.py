def make_tag(tag,words):
    return '<'+tag+'>'+words+"</"+tag+'>'
tag=input()
words=input()
print(make_tag(tag,words))
