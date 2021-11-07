import FundamentalAnalysis  as fa 
import time

#https://pypi.org/project/FundamentalAnalysis/

def win_environment(environment, tinker):
	for i in range(len(tinker)):
		if(tinker[i]<environment[i]):
			return False
	return True


def fmtTime(timeStamp):
    timeArray = time.localtime(timeStamp)
    dateTime = time.strftime("%Y-%m-%d %H:%M:%S", timeArray)
    return dateTime


api_key = '1e22a0373e96f71ca2343fa8ec7685fa'
ticker_list = ['TSLA','AAPL','AMZN','GOOG','BABA','TCEHY','FB','PFE','MSFT','JD','NFLX','SBUX','CSCO','INTC','AMD','NVDA']

NasDaq = {'2020':0.1742,'2019':0.1286,'2018':0.1811,'2017':0.1847,'2016':0.1379}



def data_collecting(input_file,Text):
	ticker_list=[]
	file1 = open(input_file, 'r')
	Lines = file1.readlines()
	for each in Lines:
		ticker_list.append(each.strip())
	Text.insert(1.0,fmtTime(time.time())+ ': choosing from: '+str(ticker_list)+"\n")
	Text.insert(2.0,fmtTime(time.time())+ ": collecting data... ..."+"\n")
	
	ticker_data= {}
	for company in ticker_list:
		financial_ratios_annually = fa.financial_ratios(company, api_key, period="annual")
		ticker_data[company] = []
		for year in ['2020','2019','2018','2017','2016']:
			result = financial_ratios_annually.loc['netProfitMargin'][year]
			ticker_data[company].append(result)

	Text.insert(3.0,fmtTime(time.time())+': Done!'+"\n")
	chosen = []
	for each_company in ticker_list:
		if(win_environment(list(NasDaq.values()),ticker_data[each_company])):
			chosen.append(each_company)
	Text.insert(4.0,fmtTime(time.time())+'Choosen: '+str(chosen)+"\n")
	for each_company in chosen:
		break
		financial_ratios_annually = fa.financial_ratios(each_company, api_key, period="annual")
		profit_2021 = financial_ratios_annually.loc['netProfitMargin'][2021]
		Text.insert(5.0,each_company+"'s 2021 profit: "+ profit_2021+" vs "+"11.9% on average"+"\n")