from pyorient.types import OrientRecord
from .connect_db import *

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
			query_string += k+'=\''+params[k]+'\''
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

	@classmethod
	def orient_base_class(cls):
		# Need to determine if the class is of type vertex or edge
		class_type = ''
		if cls.__name__ == 'V' or cls.__name__ == 'E':
			class_type = 'vertex' if cls.__name__ == 'V' else 'edge'
			return class_type

		for base_class in cls.__bases__:
			print base_class.__name__
			if base_class.__name__ == 'V':
				class_type = 'vertex'
				break
			elif base_class.__name__ == 'E':
				class_type = 'edge'
				break
		return class_type

	@classmethod
	def create(cls,params={}):
		print 'in create' 
		result = []
		if params:
			query = 'Create '+cls.orient_base_class()+' '+cls.__name__+' set '+cls.key_value_string(params,',')
			print query
			result = cls.execute(query)
		return result

	def __init__(self,params={}):
		print 'in NetworkLabObject __init__'
		self.db = self.__connect_to_db__()
		self.attributes = params

	def save(self):
		self.__class__.create(self.attributes)
	
	def obj_key_values():
		return key_value_string(self.__dict__)


class V(OrientModel):
	def __init__(self):
		super(V,self).__init__()
		print "V is initiated"

class E(OrientModel):
	def __init__(self):
		super(E,self).__init__()
		print "E is initiated"