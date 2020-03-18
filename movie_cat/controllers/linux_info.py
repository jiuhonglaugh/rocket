from subprocess import Popen,PIPE
import re
import os,sys
import paramiko
from movie_cat.common.libs.linux_info import GetLinuxMessage
from flask import Blueprint

linux_info = Blueprint('linux_info',__name__)

#if __name__ == '__main__':
@linux_info.route('/getLinuxInfo')
def get_linux_info():
    from movie_cat.config.local_setting import hosts
    hosts = hosts.split(',')
    print(hosts)
    hosts_dict = {}
    for host in hosts:
        print('主机IP为%s的系统信息：'%host)
        result = GetLinuxMessage()
        #hostIP = '172.10.4.100'
        hostIP = host
        host_name = result.get_hostname(hostIP)
        total_memory = result.get_total_memory(hostIP)
        result.get_free_memory(hostIP)
        #print('主机缓存：'+str(result.get_cach_and_buff_memory(hostIP)))
        cache_and_buff = result.get_cach_and_buff_memory(hostIP)
        #print('主机可用内存：'+ str(result.get_ava_memory(hostIP)))
        ava_memory = result.get_ava_memory(hostIP)
        #print('主机名：'+ str(host_name))
        #print('主机总内存：'+ str(total_memory))
        #print('主机IP：'+ result.get_network_info(hostIP))
        host_IP = result.get_network_info(hostIP)
        #print('主机cpu物理核数：'+ str(result.get_cpu_info(hostIP)[0]))
        cpu_physical_num = str(result.get_cpu_info(hostIP)[0])
        #print('主机cpu逻辑核数：' + str(result.get_cpu_info(hostIP)[1]))
        cpu_processor_num = str(result.get_cpu_info(hostIP)[1])
        #print('主机cpu型号_cpu_kind：' + result.get_cpu_info(hostIP)[2])
        cpu_kind = result.get_cpu_info(hostIP)[2]
        #print(result.get_os_version(hostIP))
        os_version = result.get_os_version(hostIP)
        os_network_MAC = result.get_network_MAC(hostIP)
        os_network_MAC = str(os_network_MAC, encoding='utf-8')[0:-1]
        print('os_network_MAC:=========>'+os_network_MAC)
        host_list = {}
        host_name = str(host_name,encoding='utf-8')[0:-1]
        host_list['host_name'] = host_name
        host_list['host_IP'] = host_IP
        host_list['cpu_physical_num'] = cpu_physical_num
        host_list['cpu_processor_num'] = cpu_processor_num
        cpu_kind = cpu_kind[0:-1]
        host_list['cpu_kind'] = cpu_kind
        host_list['total_memory'] = total_memory
        host_list['ava_memory'] = ava_memory
        host_list['cache_and_buff'] = cache_and_buff
        os_version = str(os_version,encoding='utf-8')[0:-1]
        host_list['os_version'] = os_version

        print('===========================================================')
        # print(type(host_name))
        # print(type(host_IP))
        # print(type(cpu_physical_num))
        # print(type(cpu_processor_num))
        # print('cpu_kind'+str(type(cpu_kind)))
        # print(type(total_memory))
        # print(type(ava_memory))
        # print(type(cache_and_buff))
        # print(type(os_version))
        # print(host_list)
        import json
        host_info_json = json.dumps(host_list)
        print(host_info_json)
        hosts_dict[os_network_MAC] = host_list
    host_json = json.dumps(hosts_dict,ensure_ascii='utf-8',indent=4)
    print(host_json)
    return host_json







