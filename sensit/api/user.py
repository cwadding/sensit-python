# <no value>
#
class User():

	def __init__(self, client):
		self.client = client

	# <no value>
	# '/api/user' GET
	#
	def profile(self, options = {}):
		body = options['query'] if 'query' in options else {}

		response = self.client.get('/api/user', body, options)

		return response

