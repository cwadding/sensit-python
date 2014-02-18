# <no value>
#
class User():

	def __init__(self, client):
		self.client = client

	# <no value>
	# '/user' GET
	#
	def profile(self, options = {}):
		body = options['query'] if 'query' in options else {}

		response = self.client.get('/user', body, options)

		return response

