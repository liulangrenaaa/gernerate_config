config_file = open(".config")
config_file_processed = open(".config_processed", "w")

try:
    lines = config_file.readlines()
    for line in lines:
        line = line.lstrip()
        if not len(line) or line.startswith('#'):
            # print(line)
            continue
        if line.endswith("=y\n"):
            config_file_processed.writelines("\"" + line[:-3] + "\",\n")
            continue
        print(line)
finally:
    config_file.close()


config_file = open(".config")
try:
    lines = config_file.readlines()
    for line in lines:
        line = line.lstrip()
        if not len(line) or line.startswith('#'):
            # print(line)
            continue
        elif line.endswith("=y\n"):
            # config_file_processed.writelines("\"" + line[:-3] + "\",\n")
            continue
        line = line.rstrip()
        config_file_processed.writelines("\"" + line + "\",\n")
finally:
    config_file.close()
    config_file_processed.close()
