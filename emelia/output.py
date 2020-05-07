import time
import sys
import getopt
# import inspect
# from import filter

from prediction import generate_predictions
from train import train_and_validate



# TODO: Implement click library
def main():
    # starting timer
    start_time = time.time()
    print('\n')
    print('========================= Program Start ==========================')
    print('\n')

    argumentList = sys.argv[1:]
    options = 'hfct'
    long_options = ['Help', 'File', 'Classify', 'Train']
    try:
        # Parsing argument
        arguments, values = getopt.getopt(argumentList, options, long_options)
        # checking each argument
        for currentArgument, currentValue in arguments:

            if currentArgument in ("-h", "--Help"):
                print("HELP:")
                print("Please choose the operation needed to be performed by "
                      "the system.\nCommands should be followed by the "
                      "files to be used (if needed).")
                print("Commands to be passed:")

                print("python <file name> --Classify "
                      "<CSV Input Alarm File Name> <CSV Alarm File Name>"
                      "<CSV Ticket File Name> <CSV Prediction File Name>")
                print("python <file name> --Train <CSV Alarm File Name> "
                      "<CSV Ticket File Name>")

            elif currentArgument in ("-f", "--File"):
                print("Displaying File Name:", sys.argv[2])

            elif currentArgument in ("-c", "--Classify"):
                print(("Command: (% s)") % (currentValue))
                generate_predictions(sys.argv[2], sys.argv[3],
                                     sys.argv[4], sys.argv[5])

            elif currentArgument in ("-t", "--Train"):
                print(("Command: (% s)") % (currentValue))
                print("PROCESSING DATA...\n")
                print("TRAINING WILL BEGIN AFTER DATA PROCESSING IS COMPLETE")
                # DataProcessor(sys.argv[2], sys.argv[3])
                '''
                attrs = (getattr(data_processor, name)
                         for name in dir(data_processor))
                methods = filter(inspect.ismethod, attrs)
                for method in methods:
                    try:
                        method()
                    except TypeError:
                        # Can't handle methods with required arguments.
                        pass
                '''
                print("DATA PROCESSING IS COMPLETE.\n")
                print("LEARNING MODEL WILL BEGIN TRAINING")
                train_and_validate(sys.argv[2], sys.argv[3])

    except getopt.error as err:
        # output error, and return with an error code
        print(str(err))


    '''
    if command == 'train':
        train_and_validate()

    elif command == 'classify':
        generate_predictions(file)

    else:
        train_and_validate()
        generate_predictions()
    '''
    # End timer & total runtime
    end_time = time.time()
    runtime = round(end_time - start_time, 2)

    # print("\n" * 2)
    # print("############################# METRICS ############################")
    print("Runtime: " + str(runtime) + "s")


if __name__ == "__main__":
    main()
