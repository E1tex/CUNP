import argparse
import json
import sys
import os


boolean_args = ["alltemplates", "onetemplate"]


def read_config():
    with open('config.json', 'r') as file:
        data = json.load(file)
        return data

def check_int_values(dictionary):
    for key, value in dictionary.items():
        try:
            int_value = int(value)
        except ValueError:
            print(f"Ошибка: Невозможно сконвертировать значение '{value}' в целое число для ключа '{key}'")
            sys.exit(1)  # Завершаем выполнение программы с кодом ошибки

def list_from_file(args, profile_content, config):
    profile_list = profile_content.split('\n')
    for user in profile_list:
        if user == '':
            continue
        user_profile = {'fname': '', 'lname': '', 'birthyear': ''}
        profile_values = user.split(':')
        checker = 0
        for key,value in args.items():
            try:
                if not (key == "inputfile" or key == "outputfile" or key == "singletemplate" or key in boolean_args):
                    intvalue = int(value)
                    user_profile[key] = profile_values[intvalue]
                else:
                    user_profile[key] = value
            except TypeError:
                pass
            except IndexError:
                sys.exit('You need to specify fname/lname/birthyear with values from 0 to 2')

        return_result(user_profile, config)

def list_from_args(args, config):
    user_profile = {}
    name = args.fname
    while name == None or len(name) == 0 or name == " " or name == "  " or name == "   ":
        print("\r\n[-] You must enter a name at least!")
        sys.exit("Exiting.")
    user_profile["fname"] = str(name)
    user_profile["lname"] = args.lname
    user_profile["birthyear"] = args.birthyear

    return_result(user_profile, config)

def read_file(file_path):
    if os.path.isabs(file_path):
        full_path = file_path
    else:
        current_directory = os.getcwd()
        full_path = os.path.join(current_directory, file_path)

    if os.path.exists(full_path):
        with open(full_path, 'r') as r:
            data = r.read()
        return data
    else:
        sys.exit(f"Can't find file {full_path}")

def print_cow():
    print("___________ ")
    print("                            ")
    print(" \033[07m  cunp.py! \033[27m                # \033[07mC\033[27mommon")
    print("      \                     # \033[07mU\033[27mser")
    print("       \   \033[1;31m,__,\033[1;m             # \033[07mN\033[27mame")
    print(
        "        \  \033[1;31m(\033[1;moo\033[1;31m)____\033[1;m         # \033[07mP\033[27mrofiler"
    )
    print("           \033[1;31m(__)    )\ \033[1;m  ")
    print(
        "           \033[1;31m   ||--|| \033[1;m\033[05m*\033[25m\033[1;m"
    )
    print(28 * " " + "[ E1tex | https://github.com/E1tex/]\r\n")

def return_result(profile, config):
    if profile.get('singletemplate'):
        try:
            templates = [profile['singletemplate']]
            profile['singletemplate'].format(f_name=profile['fname'], l_name=profile['lname'], num=profile['birthyear'])
        except ValueError and IndexError:
            sys.exit("Specify the right format for the template! You can find template example in config file.")
    else:
        templates = config["templates"]
    if profile.get('outputfile') is None:
        for template in templates:
            formatted_string = template.format(f_name=profile['fname'], l_name=profile['lname'], num=profile['birthyear'])
            print(formatted_string)
    else:
        with open(profile['outputfile'], 'a') as file:
            for template in templates:
                formatted_string = template.format(f_name=profile['fname'], l_name=profile['lname'], num=profile['birthyear'])
                file.write(formatted_string + "\n")


def main():
    config = read_config()
    parser = get_parser()
    args = parser.parse_args()
    args_dict = vars(args)
    print_cow()

    if args.inputfile:
        data = read_file(args.inputfile)
        list_from_file(args_dict, data, config)
    else:
        list_from_args(args,config)

def get_parser():

    parser = argparse.ArgumentParser(description="Common UserName Profiler")
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument(
        "-aT",
        "--alltemplates",
        action="store_true",
        help="All Templates Usage Mode",
    )
    group.add_argument(
        "-sT",
        "--singletemplate",
        help="With Single Template Specified Mode/ To use single template, specify this argument with the template to use({f_name}_{num}_{l_name})"
    )
    parser.add_argument(
        "-fn",
        "--fname",
        help="Target's first name",
    )
    parser.add_argument(
        "-ln",
        "--lname",
        help="Target's last name"
    )
    parser.add_argument(
        "-by",
        "--birthyear",
        help="Target's birth year"
    )
    parser.add_argument(
        "-i",
        "--inputfile",
        help="The file with target's information specified"
    )
    parser.add_argument(
        "-o",
        "--outputfile",
        help="The file where generated usernames will be written"
    )
    parser.add_argument(
        "-t",
        "--template",
        help="The template example('{f_name}_{num}_{l_name}')"
    )

    return parser

if __name__ == "__main__":
    main()
