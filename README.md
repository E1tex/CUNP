# CUNP (Common UserName Profiler)
CUNP (Common UserName Profiler) is a simple tool that allows you to generate lists of usernames based on input data such as first name, last name, and birth year.

## Features
- **Username Generation**: Generate usernames by combining different parts of the user's profile information.
- **Customizable**: Easily customize the format and structure of the generated usernames.
- **Easy to Use**: Simple command-line interface for quick and efficient username generation.

## Installation
You can install CUNP using git clone:
```bash
git clone https://github.com/E1tex/CUNP.git
```
Then you need to install requirements with pip:
```bash
pip install -r requirments.txt
```
## Usage

### All Templates Mode
To generate usernames based on individual target information (first name, last name, and birth year), use the following command:

```bash
python cunp.py -aT --fname <first_name> --lname <last_name> --birthyear <birth_year>
```
Replace <first_name>, <last_name>, and <birth_year> with the actual target information.
For example:
```bash
python cunp.py --fname Ivan --lname Petrov --birthyear 1985
```
### Single Template Mode
To generate usernames using a specific template, use the following command:
```bash
python main.py -sT "{f_name}_{num}_{l_name}" --fname <first_name> --lname <last_name> --birthyear <birth_year>
```

### Custom Sequence Mode
You can specify a custom sequence of fields using the following command format:

```bash
python main.py -i <input_file> -o <output_file> --template "{custom_sequence}"
```
Replace <input_file> with the file containing target information and specify the <output_file> for the generated usernames. Use arguments to denote the order of fields in the custom sequence. For example:

```bash
python main.py -aT -i data.txt -o usernames.txt --fname 1 --lname 0 --birthyear 2 
```
In this example, the script will interpret the first field as the last name, the second field as the first name, and the third field as the birth year.

Input File Format:
```bash
1932:Ivan:Spiridonov
2010:Vitaliy:Pupkin
2001:Sergey:Maltsev
```

## Contributing
Contributions are welcome! If you have any ideas for improvements or new features, feel free to submit an issue or create a pull request.
