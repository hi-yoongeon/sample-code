from tornado.ioloop import IOLoop
from tornado.websocket import WebSocketHandler
from tornado.web import Application

class EachWebSocket(WebSocketHandler) :
	def open(self) : 
		print "WebSocket opened"
		self.write_message("is connected");

	def on_message(self, message) :
		print "arrived message : " + message
		self.write_message( u"You said: " + message)

	def on_close(self) :
		print "WebSocket closed"



application = Application([
	("/websocket", EachWebSocket)
])


if __name__ == "__main__" :
	application.listen(8888)
	IOLoop.instance().start()