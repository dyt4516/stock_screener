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

NasDaq = {'2020':0.1742,'2019':0.1286,'2018':0.1811}

def mean(lst):
	sum=0
	for each in lst:
		sum+=each
	return sum/len(lst)

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
		for year in ['2020','2019','2018']:
			result = financial_ratios_annually.loc['netProfitMargin'][year]
			ticker_data[company].append(result)

	Text.insert(3.0,fmtTime(time.time())+': Done!'+"\n")
	chosen = []
	for each_company in ticker_list:
		if(win_environment(list(NasDaq.values()),ticker_data[each_company])):
			chosen.append(each_company)
	Text.insert(4.0,fmtTime(time.time())+' Choosen: '+str(chosen)+"\n")
	profit_2021=[]
	for each_company in chosen:
		begin_data_detailed  = fa.stock_data_detailed(each_company, api_key, begin="2020-12-31", end="2021-01-01")
		begin = begin_data_detailed.loc['2020-12-31']['close']
		end_data_detailed  = fa.stock_data_detailed(each_company, api_key, begin="2021-11-01", end="2021-11-02")
		end = end_data_detailed.loc['2021-11-01']['close']
		profit_2021.append((end-begin)/begin)
	Text.insert(5.0, "My portfolio profit is: " + str(round(mean(profit_2021), 3)) + ", compared with NasDaq average of 0.211\n" )

