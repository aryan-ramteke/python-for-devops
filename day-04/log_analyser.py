import json 

def read_logs(file) :
    dict = {}
    info = 0
    warning = 0
    error = 0 
    with open(file,'r') as file :
        for line in file.readlines() : 
            # print(line)
            if line.find('INFO') > 0 :
                info = info + 1
                continue
            elif line.find('WARNING') > 0 :
                warning = warning + 1
                continue
            elif line.find('ERROR') > 0 :
                error = error + 1
    dict['INFO'] = info
    dict['WARNING'] = warning
    dict['ERROR'] = error 
    print(dict)
    return dict

def write_logs(dict, file) :
    with open(file,'w') as file :
        json.dump(dict,file)
try :
    dict = read_logs('app.log')
    write_logs(dict,'log_summary.json')
except FileNotFoundError as f :
    print('FileNotFoundError: ',f)
except Exception as e:
    print('Execption occured: ',e)