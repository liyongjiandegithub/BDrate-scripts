from bjontegaard_metric import *
import os

tags = ["PASSHD5min", "PASSHD10min", "PASSHD30min", "PASSFullHD5min", "PASSFullHD10min", "PASSFullHD30min"]

prefixes = ["ExtendedTurboX264Target_", "TurboX264Reference_", "TurboX264Target_"]

testCases = ["4794_THREE_PASS", "4794_TWO_PASS", "DC_THREE_PASS", "DC_TWO_PASS", "GOT_THREE_PASS", "GOT_TWO_PASS", "JGAG_THREE_PASS", "JGAG_TWO_PASS"]

{
    "PASSHD5min" : [
        ("JGAG_THREE_PASSFullHD10min_400kbps", 510796, 42.96172181287369, 54.370873),
("JGAG_THREE_PASSFullHD10min_400kbps", 510796, 42.96172181287369, 54.370873),
("JGAG_THREE_PASSFullHD10min_400kbps", 510796, 42.96172181287369, 54.370873),
("JGAG_THREE_PASSFullHD10min_400kbps", 510796, 42.96172181287369, 54.370873)
    ]
}

def parse_data(data):
    line = data.readline()
    bdrt_data = {}
    while line:
        print(line.split(','))
        tokens = line.split(',')
        for tag in tags:
            if (tokens[0].find(tag) != -1):
                bdrt_data[tag]
        line = data.readline()


def open_data_files(folder):
    for prefix in prefixes:
        for testCase in testCases:
            data = open(os.path.join(folder, prefix+testCase, "data.csv"), "r")
            parse_data(data)


if __name__ == '__main__':
    open_data_files("/home/ullas/Work/firstpass_opti/outputs/")