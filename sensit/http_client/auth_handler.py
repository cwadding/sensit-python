# AuthHandler takes care of devising the auth type and using it
class AuthHandler():

	HTTP_HEADER = 1

	def __init__(self, auth):
		self.auth = auth

	# Calculating the Authentication Type
	def get_auth_type(self):

		if 'http_header' in self.auth:
			return self.HTTP_HEADER

		return -1

	def set(self, request):
		if len(self.auth.keys()) == 0:
			return request

		auth = self.get_auth_type()
		flag = False

		if auth == self.HTTP_HEADER:
			request = self.http_header(request)
			flag = True

		if not flag:
			raise StandardError("Unable to calculate authorization method. Please check")

		return request

	# Authorization with HTTP header
	def http_header(self, request):
		request['headers']['Authorization'] = 'Bearer ' + self.auth['http_header']
		return request

