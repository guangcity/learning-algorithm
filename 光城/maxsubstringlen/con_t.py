# 0-1背包问题的实现
class Goods:
    def __init__(self, weight, value, status):
        # 物品的重量
        self.weight = weight
        # 物品的价值
        self.value = value
        # 0表示未放入包,1表示已经放入包
        self.status = status

class Greedy(object):

    def greed(self,goods,total,parameter=None):
        result = []
        sum_weight = 0
        sum_value = 0
        s_index = []
        while True:
            s = self.strategy(goods, total,parameter)
            if s == -1:
                break
            sum_weight += goods[s].weight
            sum_value += goods[s].value
            if parameter == 'weight':
                result.append(goods[s].weight)
            elif parameter == 'value':
                result.append(goods[s].value)
            elif parameter == 'si':
                # 保留两位有效数字
                res = round(goods[s].value / goods[s].weight,2)
                result.append(res)
            total = total - goods[s].weight
            goods[s].status = 1
            s_index.append(s+1)
        return result,sum_weight,sum_value


    def strategy(self,goods,total,parameter=None):
        index = -1

        minWeight = goods[0].weight
        maxValue = goods[0].value
        maxSi = maxValue / minWeight


        for i in range(0, len(goods)):
            currentGood = goods[i]
            if parameter == 'weight':
                if currentGood.status == 0 and currentGood.weight <= total and currentGood.weight <= minWeight:
                    index = i
                    minWeight = goods[index].weight

            elif parameter == 'value':
                if currentGood.status == 0 and currentGood.weight <= total and currentGood.value > maxValue:
                    index = i
                    maxValue = currentGood.value
            elif parameter == 'si':
                if currentGood.status == 0 and currentGood.weight <= total and currentGood.value / currentGood.weight > maxSi:
                    index = i
                    maxSi = currentGood.value / currentGood.weight
                if currentGood.value / currentGood.weight <= maxSi and currentGood.weight==total:
                    index = i
        return index


if __name__ == '__main__':

    parameter_list = ['weight','value','si']
    for parameter in parameter_list:
        goods = [Goods(35, 10, 0), Goods(30, 40, 0), Goods(60, 30, 0), Goods(50, 50, 0),
                 Goods(40, 35, 0), Goods(10, 40, 0), Goods(25, 30, 0)]
        g = Greedy()
        result, sum_weight, sum_value = g.greed(goods, 150, parameter=parameter)
        if parameter == 'weight':
            print("--------------按照取最小重量贪心策略--------------")
            print("最终总重量为：" + str(sum_weight))
            print("最终总价值为：" + str(sum_value))
            print("重量选取依此选择为：", end='')
            print(result)
        elif parameter == 'value':
            print("--------------按照取最大价值贪心策略--------------")
            print("最终总重量为：" + str(sum_weight))
            print("最终总价值为：" + str(sum_value))
            print("价值选取依此选择为：", end='')
            print(result)
        elif parameter == 'si':
            print("--------------按照取最大价值密度贪心策略--------------")
            print("最终总重量为：" + str(sum_weight))
            print("最终总价值为：" + str(sum_value))
            print("密度选取依此选择为：", end='')
            print(result)