from pyorient.types import OrientRecord
from topgenerator.connect_db import *

class OrientModel(OrientRecord):
	
	@classmethod
	def __connect_to_db__(cls):
		print 'in classmethod __connect_to_db__'
		cls.db = connect()
		print 'db connected'
		return cls.db

	@classmethod
	def key_value_string(cls,params={},seperator=','):
		keys = params.keys()
		filtered_keys = []
		for k in keys:
			if ~(k.startswith('_') or k == 'in' or k == 'out'):
				filtered_keys.append(k)
		query_string = ''
		for key in filtered_keys:
			query_string += k+'='+params[k]
			if key != filtered_keys[-1]:
				query_string+=seperator
		print query_string
		return query_string
	
	@classmethod
	def find(cls,params={}):
		query = 'Select from '+cls.__name__
		if params:
			query+=' where '+cls.key_value_string(params,' and ')
		print query
		results = cls.execute(query)
		return results

	@classmethod
	def execute(cls,query=''):
		cls.__connect_to_db__()
		result = []
		try:
			result = cls.db.command(query)
		except Exception, e:
			raise e
		return result

	def __init__(self):
		print 'in NetworkLabObject __init__'
		self.db = self.__connect_to_db__()

	def obj_key_values():
		return key_value_string(self.__dict__)

class V(OrientModel):
	def __init__(self):
		super(V,self).__init__()
		print "V is initiated"

	def save():
		# return self.db.command('Create vertex '+self.__class__.__name__+' set '+obj_key_values())
		print "V saved"

	def create():
		print "V created"
