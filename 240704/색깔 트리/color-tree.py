import sys
from collections import Counter

def is_can_put(tree, pid):
    # my_depth = tree[pid]["depth"] + 1
    # print("my_depth", my_depth, "pid  max", tree[pid]["max_depth"])

    if tree[pid]["max_depth"] == 1:
        return False
    else:
        return True

def append(tree, mid, pid, color, max_depth):
    node_info = {"mid":mid, "pid":pid, "color":color, "max_depth":max_depth, "children":[]}

    if pid == -1:
        tree[mid] = {"mid":mid, "pid":pid, "color":color, "depth":1, "max_depth":max_depth, "children":[]}
    else:
        # 부모의 최대 깊이를 초과하면 넣을 수 없다.
        # 내 depth는 부모의 depth+1이다. 그리고 이게 부모의 max_depth를 초과하며 불가
        if is_can_put(tree, pid):
            tree[mid] = {"mid":mid, "pid":pid, "color":color, "depth":tree[pid]["depth"]+1, "max_depth":max_depth, "children":[]} 
            tree[pid]["children"].append(mid)
        # else:
            # print("넣을 수없음")

    # for i in tree:
    #     print(i, tree[i])
    # print("---")


def change_color(tree, mid, color):
    # print("200")
    # mid를 루트로 하는 자식들과 본인의 색을 바꿔요
    tree[mid]["color"] = color
    for mid_num in tree[mid]["children"]:
        tree[mid_num]["color"] = color
    
    # for i in tree:
    #     print(i)
    # print("---")


def print_color(tree, res, mid):
    # print("300")
    res.append(tree[mid]["color"])

def find_all_child(tree, root, child_arr):
    if root:
        child_arr.append(root)
        for child in tree[root]["children"]:
            find_all_child(tree, child, child_arr)

def calc_res(tree):
    # for i in tree:
    #     print(i, tree[i])
    # print("--")
    result = 0
    # 모든 노드의 가치를 계산해서 각각의 제곱의 합을 출력한다.
    # 가치 = 해당 노드를 루트로 하는 서브 트리 내 서로 다른 색깔의 수
    # 냅다 계산해볼까?
    for node_mid_num in tree:
        child_arr = []
        find_all_child(tree, node_mid_num,child_arr)
        colors = set()
        # print("gotten child", child_arr)
        for sub_node_mid_num in child_arr:
            colors.add(tree[sub_node_mid_num]["color"])
        result += len(Counter(colors))**2
        
    return result


def main():
    q = int(sys.stdin.readline().strip())
    res = []
    tree = {}
    for _ in range(q):
        order = list(map(int, sys.stdin.readline().strip().split()))
        if order[0] == 100:
            append(tree=tree, mid=order[1], pid=order[2], color=order[3], max_depth=order[4])
        elif order[0] == 200:
            change_color(tree=tree, mid=order[1], color=order[2])
        elif order[0] == 300:
            print_color(tree=tree, res=res, mid=order[1])
        elif order[0] == 400:
            res.append(calc_res(tree))

    for r in res:
        print(r)

if __name__ == "__main__":
    main()