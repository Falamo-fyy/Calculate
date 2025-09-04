from decimal import Decimal
from utils.base_utils import read_json_file, high_precision_sum

def DailyLiquidationCheck(file_path):
    # 读取JSON文件
    json_data = read_json_file(file_path)

    if not json_data:
        print("JSON数据读取失败！")

    # 全日总计电量
    totalClearElectricityQuantity = (
        Decimal(str(json_data.get('data', {}).get('totalClearElectricityQuantity'))))
    # 全日总计电量-中长期
    mediumLongTermDeviationElectricityQuantityCurveSumList = (
        high_precision_sum(json_data.get('data', {}).get('mediumLongTermDeviationElectricityQuantityCurve')))
    # 中长期总计电量-日前市场
    dayAheadElectricityQuantityCurveSumList = (
        high_precision_sum(json_data.get('data', {}).get('dayAheadElectricityQuantityCurve')))
    # 中长期总计电量-实时市场
    realTimeDeviationElectricityQuantityCurveSumList = (
        high_precision_sum(json_data.get('data', {}).get('realTimeDeviationElectricityQuantityCurve')))
    # 总和校验
    totalClearElectricityQuantityCheck = (
            dayAheadElectricityQuantityCurveSumList +
            realTimeDeviationElectricityQuantityCurveSumList)

    print("全日总计电量：", totalClearElectricityQuantity)
    print("中长期总计电量：", mediumLongTermDeviationElectricityQuantityCurveSumList)
    print("日前市场总计电量：", dayAheadElectricityQuantityCurveSumList)
    print("实时市场总计电量：", realTimeDeviationElectricityQuantityCurveSumList)
    print("总和校验：", totalClearElectricityQuantityCheck == totalClearElectricityQuantity)
    print("总和校验：", totalClearElectricityQuantityCheck)

    # 分割线
    print("-----------------")

    # 全日总计电费
    totalClearElectricityFee = (
        Decimal(str(json_data.get('data', {}).get('totalClearElectricityFee'))))

    mediumLongTermElectricityFeeCurveSumList = (
        high_precision_sum(json_data.get('data', {}).get('mediumLongTermElectricityFeeCurve')))
    dayAheadElectricityFeeCurveSumList = (
        high_precision_sum(json_data.get('data', {}).get('dayAheadElectricityFeeCurve')))
    realTimeElectricityFeeCurveSumList = (
        high_precision_sum(json_data.get('data', {}).get('realTimeElectricityFeeCurve')))
    totalClearElectricityFeeCheck = (
            mediumLongTermElectricityFeeCurveSumList +
            dayAheadElectricityFeeCurveSumList +
            realTimeElectricityFeeCurveSumList)

    print("全日总计电费：", totalClearElectricityFee)
    print("中长期总计电费：", mediumLongTermElectricityFeeCurveSumList)
    print("日前市场总计电费：", dayAheadElectricityFeeCurveSumList)
    print("实时市场总计电费：", realTimeElectricityFeeCurveSumList)
    print("总和校验：", totalClearElectricityFeeCheck == totalClearElectricityFee)

    # 分割线
    print("-----------------")

    # 全日加权平均价
    totalClearAveragePrice = (
        Decimal(str(json_data.get('data', {}).get('totalClearAveragePrice'))))
    mediumLongTermAveragePrice = (
        Decimal(str(json_data.get('data', {}).get('mediumLongTermAveragePrice'))))
    dayAheadAveragePrice = (
        Decimal(str(json_data.get('data', {}).get('dayAheadAveragePrice'))))
    realTimeAveragePrice = (
        Decimal(str(json_data.get('data', {}).get('realTimeAveragePrice'))))

    totalClearAveragePriceCheck = (
        round(Decimal(str(totalClearElectricityFee / totalClearElectricityQuantity)), 10)
    )
    mediumLongTermAveragePriceCheck = (
        round(Decimal(str(mediumLongTermElectricityFeeCurveSumList / mediumLongTermDeviationElectricityQuantityCurveSumList)),
              10)
    )
    dayAheadAveragePriceCheck = (
        round(Decimal(str(dayAheadElectricityFeeCurveSumList / dayAheadElectricityQuantityCurveSumList)), 10)
    )
    realTimeAveragePriceCheck = (
        round(Decimal(str(realTimeElectricityFeeCurveSumList / realTimeDeviationElectricityQuantityCurveSumList)), 10)
    )

    print("全日加权平均价：", totalClearAveragePrice)
    print("中长期加权平均价：", mediumLongTermAveragePrice)
    print("日前市场加权平均价：", dayAheadAveragePrice)
    print("实时市场加权平均价：", realTimeAveragePrice)
    print("----------------")
    print("全日加权平均价校验：", round(totalClearAveragePriceCheck, 10))
    print("中长期加权平均价校验：", round(mediumLongTermAveragePriceCheck, 10))
    print("日前市场加权平均价校验：", round(dayAheadAveragePriceCheck, 10))
    print("实时市场加权平均价校验：", round(realTimeAveragePriceCheck, 10))
    print("全日加权平均价校验：", totalClearAveragePriceCheck == totalClearAveragePrice)
    print("中长期加权平均价校验：", mediumLongTermAveragePriceCheck == mediumLongTermAveragePrice)
    print("日前市场加权平均价校验：", dayAheadAveragePriceCheck == dayAheadAveragePrice)
    print("实时市场加权平均价校验：", realTimeAveragePriceCheck == realTimeAveragePrice)


if __name__ == "__main__":
    # # 发电
    # DailyLiquidationCheck("FDdataJson.json")

    print("-"*50+"<-发电、售电->"+"-"*50)
    # 售电
    DailyLiquidationCheck("XDdataJson.json")
