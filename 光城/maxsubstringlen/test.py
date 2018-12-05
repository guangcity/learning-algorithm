class Goods:
    def __init__(self, weight, value, status):
        self.weight = weight
        self.value = value
        self.status = status   # 0未选中，1已选中

#@param goods 物品的集合
#@param total 背包的空闲重量
def greed(goods, total):
    result = []
    sum_weight = 0
    sum_value = 0
    while True:
        s=strategy(goods,total)
        if s == -1:
            break
        sum_weight += goods[s].weight
        sum_value += goods[s].value
        result.append(goods[s].weight)
        total = total - goods[s].weight
        goods[s].status = 1
        goods.pop(s)
    print("按照取最小重量贪心决策，最终总重量为：" + str(sum_weight))
    print("按照取最小重量贪心决策，最终总价值为：" + str(sum_value))

    return result

#策略
def strategy(goods,total):
    index = -1
    minWeight = goods[0].weight
    for i in range(0, len(goods)):
        currentGood = goods[i]
        if currentGood.status == 0 and currentGood.weight <= total and currentGood.weight <= minWeight:
            index = i
            minWeight = goods[index].weight

    return index


goods = [Goods(35,10,0),Goods(30,40,0),Goods(60,30,0),Goods(50,50,0),Goods(40,35,0),Goods(10,40,0),Goods(25,30,0)]
a = greed(goods,150)
print("装入背包对应的物体重量为：",end='')
print(a)



def strategy2(goods,total):
    index = -1
    maxValue = goods[0].value
    for i in range(0, len(goods)):
        currentGood = goods[i]
        if currentGood.status == 0 and currentGood.weight<=total and currentGood.weight == total:
            if currentGood.value > maxValue:
                index=i
                maxValue = currentGood.value
    return index
def greed2(goods, total):
    result = []
    sum_weight = 0
    sum_value = 0
    s_index = []
    while True:
        s=strategy2(goods,total)
        if s == -1:
            break;
        sum_weight += goods[s].weight
        sum_value += goods[s].value
        result.append(goods[s].value)
        total = total - goods[s].weight
        goods[s].status = 1
        s_index.append(s+1)
    print("装入背包的编号依次是：", end='')
    print(s_index)
    print("按照取最大价值贪心决策，最终总重量为：" + str(sum_weight))
    print("按照取最大价值贪心决策，最终总价值为：" + str(sum_value))
    return result

goods = [Goods(35,10,0),Goods(30,40,0),Goods(60,30,0),Goods(50,50,0),Goods(40,35,0),Goods(10,40,0),Goods(25,30,0)]
a = greed2(goods,150)
print("装入背包对应的物体价值为：",end='')
print(a)


def strategy3(goods,total):

    index = -1
    maxSi = goods[0].value/goods[0].weight
    for i in range(0, len(goods)):
        currentGood = goods[i]
        if currentGood.status == 0 and currentGood.weight<=total:
            if currentGood.value/currentGood.weight > maxSi:
                index = i
                maxSi = currentGood.value / currentGood.weight
            if currentGood.weight == total:
                index=i
    return index

def greed3(goods, total):
    result = []
    sum_weight = 0
    sum_value = 0
    s_index = []
    while True:
        s=strategy3(goods,total)
        if s == -1:
            break;
        sum_weight += goods[s].weight
        sum_value += goods[s].value
        result.append(goods[s].value/goods[s].weight)
        total = total - goods[s].weight
        goods[s].status = 1
        s_index.append(s+1)
    print("装入背包的编号依次是：", end='')
    print(s_index)
    print("按照取最大价值密度贪心决策，最终总重量为：" + str(sum_weight))
    print("按照取最大价值密度贪心决策，最终总价值为：" + str(sum_value))
    return result

goods = [Goods(35,10,0),Goods(30,40,0),Goods(60,30,0),Goods(50,50,0),Goods(40,35,0),Goods(10,40,0),Goods(25,30,0)]
a = greed3(goods,150)
print("装入背包对应的物体密度为：",end='')
print(a)