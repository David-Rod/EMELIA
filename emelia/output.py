import time
import sys
import getopt

from prediction import generate_predictions
from train import train_and_validate


def main():
    # starting timer
    start_time = time.time()
    print('\n')
    print('========================= Program Start ==========================')
    print('\n')

    argumentList = sys.argv[1:]
    options = 'hfctb'
    long_options = ['Help', 'File', 'Classify', 'Train', 'Both']
    try:
        # Parsing argument
        arguments, values = getopt.getopt(argumentList, options, long_options)
        # checking each argument
        for currentArgument, currentValue in arguments:

            if currentArgument in ("-h", "--Help"):
                print("HELP:")
                print("Please choose the operation needed to be performed by "
                      "the system.\nCommands should be followed by the "
                      "files to be used.")
                print("\n")
                print("Commands to be passed:")
                print("\n")
                print("TO CLASSIFY ONLY:")
                print("python <file name> --Classify "
                      "<CSV Alarm File Name> <CSV Ticket File Name> "
                      "<CSV Test Alarm File Name> <CSV Prediction File Name>")
                print("\n")
                print("TO TRAIN ONLY:")
                print("python <file name> --Train <CSV Alarm File Name> "
                      "<CSV Ticket File Name>")
                print("\n")
                print("TO CLASSIFY AND TRAIN:")
                print("python <file name> --Both "
                      "<CSV Alarm File Name> <CSV Ticket File Name> "
                      "<CSV Test Alarm File Name> <CSV Prediction File Name>")

            elif currentArgument in ("-c", "--Classify"):
                print("STARTING CLASSIFICATION")
                generate_predictions(sys.argv[2], sys.argv[3],
                                     sys.argv[4], sys.argv[5])

            elif currentArgument in ("-t", "--Train"):
                print("LEARNING MODEL WILL BEGIN TRAINING")
                train_and_validate(sys.argv[2], sys.argv[3])

            elif currentArgument in ("-b", "--Both"):
                print("LEARNING MODEL WILL BEGIN TRAINING")
                train_and_validate(sys.argv[2], sys.argv[3])
                print("STARTING CLASSIFICATION")
                generate_predictions(sys.argv[2], sys.argv[3],
                                     sys.argv[4], sys.argv[5])

            else:
                raise ValueError("The input provided is not a valid option."
                                 "Please select one of the options listed "
                                 "in the HELP command.\nType python output.py "
                                 "-h to see which commands are available.")

    except getopt.error as err:
        # output error, and return with an error code
        print(str(err))

    # End timer & total runtime
    end_time = time.time()
    runtime = round(end_time - start_time, 2)

    print("Runtime: " + str(runtime) + "s")


if __name__ == "__main__":
    main()
