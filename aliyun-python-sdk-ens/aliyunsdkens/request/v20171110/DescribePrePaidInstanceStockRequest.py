# Licensed to the Apache Software Foundation (ASF) under one
# or more contributor license agreements.  See the NOTICE file
# distributed with this work for additional information
# regarding copyright ownership.  The ASF licenses this file
# to you under the Apache License, Version 2.0 (the
# "License"); you may not use this file except in compliance
# with the License.  You may obtain a copy of the License at
#
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
#
# Unless required by applicable law or agreed to in writing,
# software distributed under the License is distributed on an
# "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
# KIND, either express or implied.  See the License for the
# specific language governing permissions and limitations
# under the License.

from aliyunsdkcore.request import RpcRequest

class DescribePrePaidInstanceStockRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'Ens', '2017-11-10', 'DescribePrePaidInstanceStock','ens')
		self.set_method('POST')

	def get_InstanceSpec(self):
		return self.get_query_params().get('InstanceSpec')

	def set_InstanceSpec(self,InstanceSpec):
		self.add_query_param('InstanceSpec',InstanceSpec)

	def get_EnsRegionId(self):
		return self.get_query_params().get('EnsRegionId')

	def set_EnsRegionId(self,EnsRegionId):
		self.add_query_param('EnsRegionId',EnsRegionId)

	def get_SystemDiskSize(self):
		return self.get_query_params().get('SystemDiskSize')

	def set_SystemDiskSize(self,SystemDiskSize):
		self.add_query_param('SystemDiskSize',SystemDiskSize)

	def get_Version(self):
		return self.get_query_params().get('Version')

	def set_Version(self,Version):
		self.add_query_param('Version',Version)

	def get_DataDiskSize(self):
		return self.get_query_params().get('DataDiskSize')

	def set_DataDiskSize(self,DataDiskSize):
		self.add_query_param('DataDiskSize',DataDiskSize)