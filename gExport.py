
def _init():#初始化
    global _global_dict
    _global_dict = {}

def set_val(key,value):
    _global_dict[key] = value
    if(value==None):
       del _global_dict[key]

def get_val(key,defValue=None):
    try:
        return _global_dict[key]
    except KeyError:
        return defValue