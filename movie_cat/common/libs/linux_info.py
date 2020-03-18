import paramiko
import re
class GetLinuxMessage:
#登录远程Linux系统
    def session(self, host, port, username, password):
        try:
            ssh = paramiko.SSHClient()
            ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
            ssh.connect(host, int(port), username, password)
            #print('login %s is successful' % host)
            return ssh
        except Exception as e:
            print(e)
#获取Linux主机名
    def get_hostname(self, host, port=22, username="root", password="Szlocal!!!"):
            cmd_hostname = "cat /etc/hostname"
            client = self.session(host, port, username, password)
            stdin, stdout, stderr = client.exec_command(cmd_hostname)
            hostname = stdout.read()
            return hostname

# 获取Linux系统总memory信息
    def get_total_memory(self, host, port=22, username="root", password="Szlocal!!!"):
        client = self.session(host, port, username, password)
        stdin, stdout, stderr = client.exec_command("cat /proc/meminfo")
        meminfo = stdout.readlines()
        # with open('/proc/meminfo') as meminfo:
        for i in meminfo:
            if i.startswith('MemTotal'):
                memory = int(i.split()[1].strip())
            else:
                pass
        return memory
# 获取Linux系统空闲memory信息
    def get_free_memory(self, host, port=22, username="root", password="Szlocal!!!"):
        client = self.session(host, port, username, password)
        stdin, stdout, stderr = client.exec_command("cat /proc/meminfo")
        meminfo = stdout.readlines()
        # with open('/proc/meminfo') as meminfo:
        for i in meminfo:
            if i.startswith('MemFree'):
                memory = int(i.split()[1].strip())
                memory = '%.f' % (memory / 1024.0)
            else:
                pass
        return memory
# 获取Linux系统可用memory信息
    def get_ava_memory(self, host, port=22, username="root", password="Szlocal!!!"):
        client = self.session(host, port, username, password)
        stdin, stdout, stderr = client.exec_command("cat /proc/meminfo")
        meminfo = stdout.readlines()
        # with open('/proc/meminfo') as meminfo:
        for i in meminfo:
            if i.startswith('MemAvailable'):
                memory = int(i.split()[1].strip())
                memory = '%.f' % (memory / 1024.0)
            else:
                pass
        return int(memory)
# 获取Linux系统缓存memory信息
    def get_cach_and_buff_memory(self, host, port=22, username="root", password="Szlocal!!!"):
        client = self.session(host, port, username, password)
        stdin, stdout, stderr = client.exec_command("cat /proc/meminfo")
        meminfo = stdout.readlines()
        # with open('/proc/meminfo') as meminfo:
        for i in meminfo:
            if i.startswith('Buffers'):
                Buffers_memory = int(i.split()[1].strip())
                Buffers_memory = '%.f' % (Buffers_memory / 1024.0)
            else:
                pass
        for i in meminfo:
            if i.startswith('Cached'):
                Cached_memory = int(i.split()[1].strip())
                Cached_memory = '%.f' % (Cached_memory / 1024.0)
            else:
                pass
        return int(Buffers_memory)+int(Cached_memory)
# 获取Linux系统网络IP信息
    def get_network_info(self, host, port=22, username="root", password="Szlocal!!!"):
        client = self.session(host, port, username, password)
        stdin, stdout, stderr = client.exec_command("ifconfig")
        data = stdout.read().decode('utf-8')
        ret = re.compile('((?:1[0-9][0-9]\.)|(?:25[0-5]\.)|(?:2[0-4][0-9]\.)|(?:[1-9][0-9]\.)|(?:[0-9]\.)){3}((1[0-9][0-9])|(2[0-4][0-9])|(25[0-5])|([1-9][0-9])|([0-9]))')
        match = ret.search(data).group()
        return  match
#获取Linux系统CPU信息
    def get_cpu_info(self, host, port=22, username="root", password="Szlocal!!!"):
        cpunum = 0
        processor = 0
        client = self.session(host, port, username, password)
        stdin, stdout, stderr = client.exec_command("cat /proc/cpuinfo")
        cpuinfo = stdout.readlines()
        #with stdout.read() as cpuinfo:
        for i in cpuinfo:
            if i.startswith('physical id'):
                cpunum = i.split(":")[1]
            if i.startswith('processor'):
                processor = processor + 1
            if i.startswith('model name'):
                cpumode = i.split(":")[1]
        return int(cpunum)+1, processor,cpumode


#获取Linux系统版本信息
    def get_os_version(self, host, port=22, username="root", password="Szlocal!!!"):
        client = self.session(host, port, username, password)
        stdin, stdout, stderr = client.exec_command("cat /etc/redhat-release")
        data = stdout.read()
        return data

#获取Linux系统网卡MAC信息
    def get_network_MAC(self, host, port=22, username="root", password="Szlocal!!!"):
        client = self.session(host, port, username, password)
        #注意网卡名称ens160
        stdin, stdout, stderr = client.exec_command("ifconfig ens160 |egrep 'ether' |awk '{print $2}'")
        data = stdout.read()
        print(data)
        return data