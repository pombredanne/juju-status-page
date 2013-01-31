import yaml


raw = """machines:
    0:
        agent-state: running
        dns-name: 0.status.com
        instance-id: i-0
        instance-state: running
    113:
        agent-state: running
        dns-name: 113.status.com
        instance-id: i-113
        instance-state: running
    114:
        agent-state: running
        dns-name: 114.status.com
        instance-id: i-114
        instance-state: running
    127:
        agent-state: running
        dns-name: 127.status.com
        instance-id: i-127
        instance-state: running
    128:
        agent-state: running
        dns-name: 128.status.com
        instance-id: i-128
        instance-state: running
    129:
        agent-state: running
        dns-name: 129.status.com
        instance-id: i-129
        instance-state: running
    142:
        agent-state: running
        dns-name: 142.status.com
        instance-id: i-142
        instance-state: running
    147:
        agent-state: running
        dns-name: 147.status.com
        instance-id: i-147
        instance-state: running
services:
    chicote2:
        charm: local:precise/ruby-6
        relations: {}
        units:
            chicote2/2:
                agent-state: started
                machine: 147
                public-address: 147.status.com
    cpbr6:
        charm: local:precise/python-37
        relations: {}
        units:
            cpbr6/3:
                agent-state: started
                machine: 142
                public-address: 142.status.com
    mysqlapi:
        charm: local:precise/python-37
        relations: {}
        units:
            mysqlapi/1:
                agent-state: started
                machine: 127
                public-address: 127.status.com
            mysqlapi/2:
                agent-state: started
                machine: 128
                public-address: 128.status.com
    tsurudashboard:
        charm: local:precise/ruby-6
        relations: {}
        units:
            tsurudashboard/1:
                agent-state: started
                machine: 113
                public-address: 113.status.com
            tsurudashboard/2:
                agent-state: started
                machine: 114
                public-address: 114.status.com
    zito001:
        charm: local:precise/static-2
        relations: {}
        units:
            zito001/0:
                agent-state: started
                machine: 129
                public-address: 129.status.com"""

output = yaml.load(raw, Loader=yaml.Loader)
