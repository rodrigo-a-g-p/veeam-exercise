import os
import shutil
import argparse
import time
import datetime

parser = argparse.ArgumentParser()

parser.add_argument('source_folder_path', type=str, help='Path of the folder to be cloned')
parser.add_argument('destination_folder_path', type=str, help='Path of the cloned folder')
parser.add_argument('log_file_path', type=str, help='Path of the log file')
parser.add_argument('sync_interval', type=int, help='Amount of time in minutes until next cloning process')

args = parser.parse_args()


def clone():
    with open(args.log_file_path, "a") as log_file:
        start_message = f"Cloning process has started at {datetime.datetime.now()}\n"
        log_file.write(start_message)
        print(start_message)

        for item in os.listdir(args.source_folder_path):

            if not os.path.exists(args.destination_folder_path):
                os.makedirs(args.destination_folder_path)
                created_message = f"{args.destination_folder_path} has been created\n"
                log_file.write(created_message)
                print(created_message)

            item_source_absolute_filepath = f"{args.source_folder_path}/{item}"
            item_destination_absolute_filepath = f"{args.destination_folder_path}/{item}"

            if os.path.isfile(item_source_absolute_filepath):
                shutil.copyfile(item_source_absolute_filepath, item_destination_absolute_filepath)

            if os.path.isdir(item_source_absolute_filepath):
                shutil.copytree(item_source_absolute_filepath, item_destination_absolute_filepath, dirs_exist_ok=True)

            cloned_message = f"{item_source_absolute_filepath} has been cloned to {args.destination_folder_path}\n"
            log_file.write(cloned_message)
            print(cloned_message)

        end_message = f"Cloning process has ended at {datetime.datetime.now()}\n\n"
        log_file.write(end_message)
        print(end_message)
        log_file.close()


def main():
    while True:
        clone()
        time.sleep(args.sync_interval * 60)


if __name__ == "__main__":
    main()

