from decimal import Decimal
from utils.base_utils import read_json_file, high_precision_sum


def queryincomeAnalysisStatistics(file_path):
    json_data = read_json_file(file_path)

    if not json_data:
        print(f"数据读取失败")

    totalEarnings = (
        Decimal(str(json_data.get('data', {}).get('totalEarnings'))))

    dailyArbitrageGainsCurve = (
        high_precision_sum(json_data.get('data', {}).get('dailyArbitrageGainsCurve')))

    print(f"总收益率: {totalEarnings}")
    print(f"总日收益率: {dailyArbitrageGainsCurve}")
    print(f"一致校验: {totalEarnings == dailyArbitrageGainsCurve}")


def queryincomeAnalysis(file_path):
    json_data = read_json_file(file_path)

    if not json_data:
        print(f"详细页数据读取失败")

    dayAheadDeclaredElectricityCurveSumList = (
        high_precision_sum(json_data.get('data', {}).get('dayAheadDeclaredElectricityCurve')))
    print(f"日前申报电量总和（累加）: {round(dayAheadDeclaredElectricityCurveSumList / 10000, 3)}")

    realTimeEnergyCurveSumList = (
        high_precision_sum(json_data.get('data', {}).get('realTimeEnergyCurve')))
    print(f"实时电量总和（累加）: {round(realTimeEnergyCurveSumList / 10000, 3)}")

    print("-" * 20)

    realTimeOutPower = Decimal(0)
    realTimeOutPowerProfit = Decimal(0)
    realTimeInPower = Decimal(0)
    realTimeInPowerProfit = Decimal(0)
    for i in range(len(json_data.get('data', {}).get('realTimeDayAheadDeviationCurve'))):
        realTimeDayAheadDeviationCurve = (
            Decimal(str(json_data.get('data', {}).get('realTimeDayAheadDeviationCurve')[i])))

        realTimeDayAheadDeviationPriceCurve = (
            Decimal(str(json_data.get('data', {}).get('realTimeDayAheadDeviationPriceCurve')[i])))

        if realTimeDayAheadDeviationCurve > 0:
            realTimeOutPower += realTimeDayAheadDeviationCurve
            realTimeOutPowerProfit += -realTimeDayAheadDeviationPriceCurve * realTimeDayAheadDeviationCurve

        if realTimeDayAheadDeviationCurve < 0:
            realTimeInPower += -realTimeDayAheadDeviationCurve
            realTimeInPowerProfit += -realTimeDayAheadDeviationPriceCurve * realTimeDayAheadDeviationCurve

    print(f"实时超用电量{round(realTimeOutPower / 10000, 3)}")
    print(f"实时超用增利{round(realTimeOutPowerProfit / 1000, 3)}")
    print(f"实时少用电量{round(realTimeInPower / 10000, 3)}")
    print(f"实时少用增利{round(realTimeInPowerProfit / 1000, 3)}")


if __name__ == '__main__':
    # 概览页-本月总收益
    queryincomeAnalysisStatistics("queryincomeAnalysisStatistics.json")

    print("-" * 30)
    # 详细页
    queryincomeAnalysis("queryincomeAnalysis.json")
