import re
import operator
import sys
import csv

ERROR_TYPE_COUNT = 0

def process_logfile(logfile):
    error_msgs = {}
    user_stats = {}
    error_code = {}
    pattern1 = r"ticky: ERROR ([\w ]*) "
    pattern2 = r"ticky: INFO ([\w ]*) "
    
    with open(logfile, 'r') as f:
        for line in f:
            if "ticky" not in line:
                continue
            if re.search(pattern1, line) is not None:
                result = re.findall(pattern1, line)
                error = result[0]
                if error not in error_msgs.keys():
                    error_msgs[error] = 1
                    # generate and save a unique code for each error
                    error_code[error] = generate_error_code()
                else:
                    error_msgs[error] += 1
                result = re.findall(r"\([\w\.]*\)", line)
                user_name = result[0][1:-1]
                if user_name not in user_stats.keys():
                    L = [0] * 2
                    L.append('-')
                    user_stats[user_name] = L
                    L[1] = 1
                    L[2] = error_code[error]
                else:
                    (user_stats[user_name])[1] += 1
                    (user_stats[user_name])[2] = error_code[error] if (user_stats[user_name])[2]=='-' else (user_stats[user_name])[2] + ',' + error_code[error]
                    
            elif re.search(pattern2, line) is not None:
                result = re.findall(r"\([\w\.]*\)", line)
                user_name = result[0][1:-1]
                if user_name not in user_stats.keys():
                    L = [0] * 2
                    L.append('-')
                    user_stats[user_name] = L
                    L[0] = 1
                else:
                    (user_stats[user_name])[0] += 1
           
        f.close()
    return error_msgs, user_stats, error_code

def write_to_csv(error_msgs, user_stats, error_code):
    with open('error_message.csv', 'w') as f:
        writer = csv.writer(f)
        col_names = [("Error", "Count", "Error Code")]
        # add error code to items list
        items = [item+(error_code[item[0]],) for item in error_msgs.items()]
        writer.writerows((col_names + sorted(items, key = operator.itemgetter(1), reverse=True)))
        f.close()
    print("Table succesfully written to {}".format(f.name))
        
    with open('user_statistics.csv', 'w') as f:
        list_of_user_stats2 = []
        list_of_user_stats = sorted(user_stats.items(), key = operator.itemgetter(0))
        writer = csv.writer(f)
        col_names = [("Username", "INFO", "ERROR", 'Error code')]
        for elem in list_of_user_stats:
            tu = elem[0], elem[1][0], elem[1][1], elem[1][2]
            list_of_user_stats2.append(tu)
        writer.writerows((col_names + list_of_user_stats2))
        f.close()
    print("Table succesfully written to {}".format(f.name))

def generate_error_code():
    global ERROR_TYPE_COUNT
    ERROR_TYPE_COUNT += 1
    error_code = 'ERR' + str(ERROR_TYPE_COUNT)
    return error_code

if __name__ == '__main__':
    """Verifies the arguments and then calls the processing function"""
    if len(sys.argv) != 2:
        print("ERROR: Exactly 1 argument expected, got {}!".format(len(sys.argv)-1))
        print("Exiting program...")
        sys.exit(1)
    logfile = sys.argv[1]
    error_msgs, user_stats, error_code = process_logfile(logfile)
    write_to_csv(error_msgs, user_stats, error_code)
    
            