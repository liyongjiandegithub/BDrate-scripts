from bjontegaard_metric import *
import os

tags = ["HD5min", "HD10min", "HD30min", "FullHD5min", "FullHD10min", "FullHD30min"]

prefixes = ["ExtendedTurboX264Target_", "TurboX264Reference_", "TurboX264Target_"]

testCases = ["DC_THREE_PASS", "DC_TWO_PASS", "GOT_THREE_PASS", "GOT_TWO_PASS", "JGAG_THREE_PASS", "JGAG_TWO_PASS"]


def runTest(prefixRefData, prefixTestData):
    bdsnr_psnr_avg = []
    bdsnr_vmaf_avg = []
    bdrate_psnr_avg = []
    bdrate_vmaf_avg = []
    for testCase in prefixRefData.keys():
        for tag in prefixRefData[testCase].keys():
            bdsnr_psnr = BD_PSNR([float(prefixRefData[testCase][tag][0][1]), float(prefixRefData[testCase][tag][1][1]), float(prefixRefData[testCase][tag][2][1]), float(prefixRefData[testCase][tag][3][1])],
                                 [float(prefixRefData[testCase][tag][0][2]), float(prefixRefData[testCase][tag][1][2]), float(prefixRefData[testCase][tag][2][2]), float(prefixRefData[testCase][tag][3][2])],
                                 [float(prefixTestData[testCase][tag][0][1]), float(prefixTestData[testCase][tag][1][1]), float(prefixTestData[testCase][tag][2][1]), float(prefixTestData[testCase][tag][3][1])],
                                 [float(prefixTestData[testCase][tag][0][2]), float(prefixTestData[testCase][tag][1][2]), float(prefixTestData[testCase][tag][2][2]), float(prefixTestData[testCase][tag][3][2])])
            bdsnr_psnr_avg.append(bdsnr_psnr)
            bdsnr_vmaf = BD_PSNR([float(prefixRefData[testCase][tag][0][1]), float(prefixRefData[testCase][tag][1][1]), float(prefixRefData[testCase][tag][2][1]), float(prefixRefData[testCase][tag][3][1])],
                                 [float(prefixRefData[testCase][tag][0][3]), float(prefixRefData[testCase][tag][1][3]), float(prefixRefData[testCase][tag][2][3]), float(prefixRefData[testCase][tag][3][3])],
                                 [float(prefixTestData[testCase][tag][0][1]), float(prefixTestData[testCase][tag][1][1]), float(prefixTestData[testCase][tag][2][1]), float(prefixTestData[testCase][tag][3][1])],
                                 [float(prefixTestData[testCase][tag][0][3]), float(prefixTestData[testCase][tag][1][3]), float(prefixTestData[testCase][tag][2][3]), float(prefixTestData[testCase][tag][3][3])])
            bdsnr_vmaf_avg.append(bdsnr_vmaf)
            bdrate_psnr = BD_RATE([float(prefixRefData[testCase][tag][0][1]), float(prefixRefData[testCase][tag][1][1]), float(prefixRefData[testCase][tag][2][1]), float(prefixRefData[testCase][tag][3][1])],
                                 [float(prefixRefData[testCase][tag][0][2]), float(prefixRefData[testCase][tag][1][2]), float(prefixRefData[testCase][tag][2][2]), float(prefixRefData[testCase][tag][3][2])],
                                 [float(prefixTestData[testCase][tag][0][1]), float(prefixTestData[testCase][tag][1][1]), float(prefixTestData[testCase][tag][2][1]), float(prefixTestData[testCase][tag][3][1])],
                                 [float(prefixTestData[testCase][tag][0][2]), float(prefixTestData[testCase][tag][1][2]), float(prefixTestData[testCase][tag][2][2]), float(prefixTestData[testCase][tag][3][2])])
            bdrate_psnr_avg.append(bdrate_psnr)
            bdrate_vmaf = BD_RATE([float(prefixRefData[testCase][tag][0][1]), float(prefixRefData[testCase][tag][1][1]), float(prefixRefData[testCase][tag][2][1]), float(prefixRefData[testCase][tag][3][1])],
                                 [float(prefixRefData[testCase][tag][0][3]), float(prefixRefData[testCase][tag][1][3]), float(prefixRefData[testCase][tag][2][3]), float(prefixRefData[testCase][tag][3][3])],
                                 [float(prefixTestData[testCase][tag][0][1]), float(prefixTestData[testCase][tag][1][1]), float(prefixTestData[testCase][tag][2][1]), float(prefixTestData[testCase][tag][3][1])],
                                 [float(prefixTestData[testCase][tag][0][3]), float(prefixTestData[testCase][tag][1][3]), float(prefixTestData[testCase][tag][2][3]), float(prefixTestData[testCase][tag][3][3])])
            bdrate_vmaf_avg.append(bdrate_vmaf)
            print(testCase + "_" + tag + " BDsnr PSNR: "  + str(bdsnr_psnr) + " BDsnr VMAF: " + str(bdsnr_vmaf) + " BDRate PSNR: " + str(bdrate_psnr) + " BDRate VMAF: " + str(bdrate_vmaf))
    print("\nAverages: " + " BDsnr PSNR: " + str(sum(bdsnr_psnr_avg)/len(bdsnr_psnr_avg)) +" BDsnr VMAF: " + str(sum(bdsnr_vmaf_avg)/len(bdsnr_vmaf_avg)) + " BDRate PSNR: " + str(sum(bdrate_psnr_avg)/len(bdrate_psnr_avg)) + " BDRate VMAF: " + str(sum(bdrate_vmaf_avg)/len(bdrate_vmaf_avg)))
    print("Min Val.: " + " BDsnr PSNR: " + str(min(bdsnr_psnr_avg)) +" BDsnr VMAF: " + str(min(bdsnr_vmaf_avg)) + " BDRate PSNR: " + str(min(bdrate_psnr_avg)) + " BDRate VMAF: " + str(min(bdrate_vmaf_avg)))
    print("Max Val.: " + " BDsnr PSNR: " + str(max(bdsnr_psnr_avg)) +" BDsnr VMAF: " + str(max(bdsnr_vmaf_avg)) + " BDRate PSNR: " + str(max(bdrate_psnr_avg)) + " VMAF: " + str(max(bdrate_vmaf_avg)))


def parse_line(tokens):
    name = tokens[0]
    bitrate = tokens[3]
    psnr = tokens[-3]
    vmaf = tokens[-2]
    return (name, bitrate, psnr, vmaf)


def parse_data(data):
    line = data.readline()
    parsedData = {}
    while line:
        #print(line.split(','))
        tokens = line.split(',')
        for tag in tags:
            if (tokens[0].find(tag) != -1):
                parseLine = (tokens[0], tokens[3], tokens[-3], tokens[-2])
                print(parseLine)
                if tag not in parsedData:
                    parsedData[tag] = []
                parsedData[tag].append(parseLine)
        line = data.readline()
    return parsedData



def runBdrateOnFolder(folder):
    testData = {}
    for prefix in prefixes:
        testData[prefix] = {}
        print("For " + prefix)
        for testCase in testCases:
            data = open(os.path.join(folder, prefix+testCase, "data.csv"), "r")
            testData[prefix][testCase] = parse_data(data)
            # print("For " + prefix+testCase)
            # print(testData[prefix][testCase])

    print("\n\n\n Scenario TurboX264Reference_ vs ExtendedTurboX264Target_ \n\n\n")
    runTest(testData["TurboX264Reference_"], testData["ExtendedTurboX264Target_"])
    print("\n\n\n Scenario TurboX264Reference_ vs TurboX264Target_ \n\n\n")
    runTest(testData["TurboX264Reference_"], testData["TurboX264Target_"])


if __name__ == '__main__':
    runBdrateOnFolder("/home/ullas/Work/firstpass_opti/outputs/")