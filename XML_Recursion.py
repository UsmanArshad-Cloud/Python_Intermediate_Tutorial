import xml.dom.minidom as minidom

domtree = minidom.parse('family.xml')
group = domtree.documentElement
parents = group.getElementsByTagName('parent')


def PrintAllPossibleChilds(parent):
    print(parent.getElementsByTagName('name')[0].childNodes[0].data)
    print(f"Parent Name is:{parent.getElementsByTagName('name')[0].childNodes[0].data}")
    immediate_childs=parent.childNodes.length
    print(f"Parent Name is:{parent.getElementsByTagName('name')[0].childNodes[0].data} and have immediate childrens {immediate_childs}")
    print(immediate_childs)
    childes = parent.getElementsByTagName('child')
    if len(childes) > 0:
        print(f"{parent.getElementsByTagName('name')[0].childNodes[0].data}'s children are:")
        print(f"{parent.getElementsByTagName('name')[0].childNodes[0].data}'s no of children are {len(childes)}")
        for child in childes:
            PrintAllPossibleChilds(child)
    else:
        print(f"{parent.getElementsByTagName('name')[0].childNodes[0].data} has no childrens")
        return

for parent in parents:
    PrintAllPossibleChilds(parent)
    print("__________")
