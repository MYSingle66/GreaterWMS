import yaml
from ruamel import yaml


def read_yaml(yaml_path):
    with open(yaml_path,mode="r",encoding="utf-8") as f:
        result=yaml.load(stream=f,Loader=yaml.FullLoader)
        return result

def read_yaml2(fileDir):
    with open(fileDir,'r',encoding='utf8') as file:
        return yaml.safe_load(file.read())


def write_yaml(yaml_path,data):
    with open(yaml_path,encoding="utf-8",mode="w") as f:
        yaml.dump(data,stream=f,allow_unicode=True)

def add_yaml(yaml_path,data):
    with open(yaml_path, 'a', encoding="UTF8") as f:
        yaml.dump(data, stream=f,allow_unicode=True,Dumper=yaml.RoundTripDumper)



if __name__ == '__main__':
    print(read_yaml2('E:\Django文件\poDemo\data\logindata.yaml'))
    # print(write_yaml())