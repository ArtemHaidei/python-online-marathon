# test 1
import json
import logging
from os.path import exists
import csv
from jsonschema import validate
from json import JSONEncoder
import pickle
from enum import Enum
from os import path


def get_value(array, key, output_list):
    if isinstance(array, list):
        [get_value(item, key, output_list) for item in array if type(item) == dict]

    elif isinstance(array, dict):
        for key_f, value in array.items():
            if key == key_f and isinstance(value, (str, list)) and value not in output_list:
                output_list += [x for x in value if x not in output_list]\
                    if isinstance(value, list) else [value]
            elif isinstance(value, (dict, list)):
                get_value(value, key, output_list)


def find(file, key):
    result = []
    with open(file) as f:
        get_value(json.load(f), key, result)
    return result


# test 2
logging.basicConfig(filename='app.log', filemode='w', format='%(name)s - %(levelname)s - %(message)s')


def parse_user(output_file, *input_files):
    unique_names, parse_result = [], []
    for file in input_files:
        if not exists(file):
            logging.error(f"File {file} doesn't exist")
            continue
        with open(file, 'r') as f:
            for dictionary in json.load(f):
                if 'name' in dictionary and dictionary["name"] not in unique_names:
                    unique_names += [dictionary["name"]]
                    parse_result += [dictionary]

    with open(output_file, 'w') as file:
        json.dump(parse_result, file, indent=4)


# test 3
class DepartmentName(Exception): pass


class InvalidInstanceError(Exception): pass


def validate_json(data, schema):
    for key, value in schema.items():
        if key not in data or type(data[key]) != value:
            raise InvalidInstanceError(f'Error in {"user" if "department_id" in schema else "department"} schema')


def user_with_department(csv_file, user_json, department_json):
    with open(user_json) as u:
        with open(department_json) as d:
            user, department = json.load(u), json.load(d)
            [validate_json(x, {'id': int, 'name': str, 'department_id': int}) for x in user]
            [validate_json(i, {'id': int, 'name': str}) for i in department]
            result = [['name', 'department']]
            for x in user:
                if not any([x['department_id'] == i['id'] for i in department]):
                    raise DepartmentName(f"Department with id {x['department_id']} doesn't exists")
                result += [[x['name'], i['name']] for i in department if x['department_id'] == i['id']]

    with open(csv_file, 'w') as cv:
        csv_writer = csv.writer(cv, delimiter=',')
        for line in result:
            csv_writer.writerow(line)


# test 4
class Student:
    def __init__(self, full_name: str, avg_rank: float, courses: list):
        self.full_name, self.avg_rank, self.courses = full_name, avg_rank, courses

    def __str__(self):
        return f"{self.full_name} ({self.avg_rank}): {self.courses}"

    @classmethod
    def from_json(cls, json_file):
        with open(json_file) as file:
            return cls(*json.load(file).values())

    @staticmethod
    def serialize_to_json(student, filename):
        Group.serialize_to_json(student, filename)


class Group:
    def __init__(self, title: str, students: list):
        self.title, self.students = title, students

    def __str__(self):
        string = [f'{x["full_name"]} ({x["avg_rank"]}): {x["courses"]}' for x in self.__dict__['students']]
        return f"{self.title}: {string}"

    @staticmethod
    def serialize_to_json(list_of_groups, filename):
        with open(filename, 'w') as file:
            json.dump(list_of_groups, file, default=lambda o: o.__dict__ if isinstance(o, (Group, Student)) else o)

    @classmethod
    def create_group_from_file(cls, students_file):
        with open(students_file, "r") as file:
            group = json.load(file)
        return cls(students_file.split(".")[0], group if type(group) == list else [group])


# test 5
class FileType(Enum):
    JSON = '.json'
    BYTE = '.byte'


class SerializeManager:
    def __init__(self, filename, type_):
        self.filename, self.type_ = filename, type_

    def serialize(self, user_dict):
        method = {'.json': [json.dump, "w"], '.byte': [pickle.dump, 'wb']}[self.type_.value]
        with open(self.filename, method[1]) as file:
            method[0](user_dict, file)

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        pass


def serialize(obj, filename, fileType):
    with SerializeManager(filename, fileType) as manager:
        manager.serialize(obj)
