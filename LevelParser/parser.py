import csv
import json

def readQuestionFromCSV():
    all_level = []
    with open('mlq.csv', newline='') as csvfile:
        mlq_levels = csv.reader(csvfile, delimiter=' ', quotechar='|')
        next(mlq_levels)
        for level in mlq_levels:
            parsed = level[0].split(',')
            level_id = parsed[0]
            level_type = parsed[1]
            correct_target = parsed[2]
            correct_target_iri = parsed[3]
            incorrect_targets = parsed[4]
            incorrect_targets_iri = parsed[5]

            incorrect_target_array = incorrect_targets.split("|")
            incorrect_iri_array = incorrect_targets_iri.split("|")
            incorrect  = []

            if(len(incorrect_target_array) == len(incorrect_iri_array)):
                for i in range(len(incorrect_target_array)):
                    incorrect_json = {
                        "literal": incorrect_target_array[i],
                        "iri": incorrect_iri_array[i]
                    }
                    incorrect.append(incorrect_json)
            else:
                print("Length of incorrect target and iri are not the same.")
            

            level_json = {
                "levelID" : level_id , 
                "levelType" : level_type , 
                "correctTarget": correct_target,
                "correctStandardContent" : correct_target_iri,
                "incorrect" : incorrect  
            }
            all_level.append(level_json)
    return json.dumps(all_level )

def main():
    f = open("levels.json", "w+")
    levels = readQuestionFromCSV()
    f.write(levels)


main()
