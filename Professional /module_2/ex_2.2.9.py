
file_path = 'files/files.txt'
#file_report = 'files/file_report.txt'

CONVERTER_TO_BYTES: dict[str, list] = {
    'B': [1],
    'KB': [1024],
    'MB': [1024, 1024],
    'GB': [1024, 1024, 1024]
}
CONVERTEE_TO_REPORT = {
    0: 'B',
    1: 'KB',
    2: 'MB',
    3: 'GB'
}

def file_reader(file: str):

    file_info_d = {}


    def get_report_files_size(size_bytes: int) -> str:
        type_b = 0
        for count in range(4):

            if not size_bytes // 1024:
                type_b = count
                break
            size_bytes = int((size_bytes/1024)+ 0.5)

        type_b = CONVERTEE_TO_REPORT[type_b]
        return f'Summary: {size_bytes} {type_b}\n'



    def record_file_info(file_name: str, size: int, extension: str):
        if extension not in file_info_d:
            file_info_d[extension] = {}
        file_info_d[extension][file_name] = size


    def get_file_size_as_bytes(size: int, type_b: str) -> int:
        values = CONVERTER_TO_BYTES[type_b]
        for value in values:
            size=size*value
        return size


    def get_and_record_file_info(file_info: str):
        file_info_list = file_info.split(' ')

        file_size = int(file_info_list[1])
        type_b = file_info_list[2]
        extension = file_info_list[0].split('.')[-1]
        file_name = file_info_list[0]

        size_in_bytes = get_file_size_as_bytes(file_size, type_b)
        record_file_info(file_name, size_in_bytes, extension)

    def create_report():
        sorted_extension = sorted(file_info_d)

        #with open(file_report, 'w') as f:
        for extension in sorted_extension:
            file_names_list = list(file_info_d[extension].keys())

            file_names = sorted(
                file_names_list,
                key=lambda x: x[0::]  # сортировка по всем буквам словам
            )

            file_names_str = '\n'.join(file_names)
            file_size = sum(list(file_info_d[extension].values()))
            report_size = get_report_files_size(file_size)

            print(file_names_str)
            print('----------')
            print(report_size)

                # f.write(file_names_str)
                # f.write('\n----------\n')
                # f.write(report_size)


    with open(file, 'r', encoding='utf-8') as f:
        for line in f:
            get_and_record_file_info(line.strip())

    create_report()


file_reader(file_path)