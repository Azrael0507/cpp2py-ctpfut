# -*- coding: utf-8 -*-
from MyApi import *
import thostmduserapi as MDapi

class CFtdcMdSpi(MDapi.CThostFtdcMdSpi):

    def __init__(self,mdapi):
        MDapi.CThostFtdcMdSpi.__init__(self)
        self.mdapi=mdapi
        
    def OnFrontConnected(self) -> "void":
        print ("OnFrontConnected")
        self.mdapi.ReqLogin()
        
    def OnRspUserLogin(self, pRspUserLogin: 'CThostFtdcRspUserLoginField', pRspInfo: 'CThostFtdcRspInfoField', nRequestID: 'int', bIsLast: 'bool') -> "void":
        print (f"OnRspUserLogin, SessionID={pRspUserLogin.SessionID},ErrorID={pRspInfo.ErrorID},ErrorMsg={pRspInfo.ErrorMsg}")
        self.mdapi.ReqDepthMD()

    def OnRtnDepthMarketData(self, pDepthMarketData: 'CThostFtdcDepthMarketDataField') -> "void":
        print ("OnRtnDepthMarketData")

        DealTooMax(pDepthMarketData)

        mdlist=([pDepthMarketData.TradingDay,\
        pDepthMarketData.InstrumentID,\
        pDepthMarketData.LastPrice,\
        pDepthMarketData.PreSettlementPrice,\
        pDepthMarketData.PreClosePrice,\
        pDepthMarketData.PreOpenInterest,\
        pDepthMarketData.OpenPrice,\
        pDepthMarketData.HighestPrice,\
        pDepthMarketData.LowestPrice,\
        pDepthMarketData.Volume,\
        pDepthMarketData.Turnover,\
        pDepthMarketData.OpenInterest,\
        pDepthMarketData.ClosePrice,\
        pDepthMarketData.SettlementPrice,\
        pDepthMarketData.UpperLimitPrice,\
        pDepthMarketData.LowerLimitPrice,\
        pDepthMarketData.PreDelta,\
        pDepthMarketData.CurrDelta,\
        pDepthMarketData.UpdateTime,\
        pDepthMarketData.UpdateMillisec,\
        pDepthMarketData.BidPrice1,\
        pDepthMarketData.BidVolume1,\
        pDepthMarketData.AskPrice1,\
        pDepthMarketData.AskVolume1,\
        pDepthMarketData.AveragePrice])
        print (mdlist)

    def OnRspSubMarketData(self, pSpecificInstrument: 'CThostFtdcSpecificInstrumentField', pRspInfo: 'CThostFtdcRspInfoField', nRequestID: 'int', bIsLast: 'bool') -> "void":
        print ("OnRspSubMarketData")
        print ("InstrumentID=",pSpecificInstrument.InstrumentID)
        print ("ErrorID=",pRspInfo.ErrorID)
        print ("ErrorMsg=",pRspInfo.ErrorMsg)

#深度行情处理异常值
def DealTooMax(mddata):
    maxprice = 1e+15
    minprice = -1e+15
    if((mddata.SettlementPrice > maxprice) or (mddata.SettlementPrice < minprice)):
        mddata.SettlementPrice=0
    if((mddata.OpenPrice > maxprice) or (mddata.OpenPrice < minprice)):
        mddata.OpenPrice=0
    if((mddata.HighestPrice > maxprice) or (mddata.HighestPrice < minprice)):
        mddata.HighestPrice=0
    if((mddata.LowestPrice > maxprice) or (mddata.LowestPrice < minprice)):
        mddata.LowestPrice=0
    if((mddata.PreDelta > maxprice) or (mddata.PreDelta < minprice)):
        mddata.PreDelta=0
    if((mddata.CurrDelta > maxprice) or (mddata.CurrDelta < minprice)):
        mddata.CurrDelta=0
    if((mddata.BidPrice1 > maxprice) or (mddata.BidPrice1 < minprice)):
        mddata.BidPrice1=0
    if((mddata.AskPrice1 > maxprice) or (mddata.AskPrice1 < minprice)):
        mddata.AskPrice1=0
