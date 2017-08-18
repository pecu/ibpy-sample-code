from ib.opt import ibConnection, Connection, message
from ib.ext.Contract import Contract
from ib.ext.Order import Order
import time

def print_message_from_ib(msg):
	print(msg)
def my_BidAsk(msg):
	if msg.field == 1:
		global Gbid
		Gbid = msg.price
		print("bid:", Gbid)	
	if msg.field == 2:
		global Gask
		Gask = msg.price	
		print("ask:", Gask)
def main():
	#connect
	# conn = Connection.create(port=7497,clientId=4)
	conn = ibConnection()
	conn.registerAll(print_message_from_ib)
	conn.unregister(print_message_from_ib,message.tickSize,message.tickPrice,
		message.tickString,message.tickOptionComputation)
	conn.register(my_BidAsk,message.tickPrice)
	
	conn.connect()
	print("test:", Gbid)

	##get contract
	newContract = Contract()
	newContract.m_symbol = 'EUR'#買入物
	newContract.m_secType = 'CASH'#股票,外匯
	newContract.m_exchange = 'IDEALPRO'#交易所
	newContract.m_currency = 'USD'#交易貨幣
	tickID = 3
	conn.reqMktData(tickID,newContract, '',False)
	# print(message.tickPrice.price)

	#test = 1.17363
	#if( Gbid > test ):
		#orderID = 104
		#mktOrder = Order()
		#mktOrder.m_totalQuantity = 100
		#mktOrder.m_orderType = 'LMT'
		#mktOrder.m_action = 'BUY'
		#mktOrder.m_lmtPrice = Gbid + 0.001
		#conn.placeOrder(orderID,newContract,mktOrder)
	
	time.sleep(1)
	conn.disconnect()

# if __name__ == "__main__":
main()