from .models import Tag


# def search(tags):
#     questions = Question.objects.order_by("title")
#     for question in questions:
#         for tag in questions.__getattribute__(tags):
#
#     for tag in tags:


def addTag(name, parent):
    if parent is None:
        Tag.objects.create(name, None)
        return
    parent_tag = None
    for tag in Tag.objects:
        if tag.name == parent:
            parent_tag = Tag.objects.get(parent)
            break
    if parent_tag is None:
        addTag(parent, None)
        addTag(name, parent)
    else:
        Tag.objects.create(name, parent_tag)