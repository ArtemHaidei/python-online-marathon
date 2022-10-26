import json
from enum import Enum
import re
import uuid


class NonUniqueException(Exception):
    data = None

    def __str__(self):
        return f"User with name {NonUniqueException.data} already exists"


class PasswordValidationException(Exception):
    ...


class ForbiddenException(Exception):
    ...


class Role(Enum):
    Mentor = 'Role.Mentor'
    Trainee = 'Role.Trainee'


class Subject:
    def __init__(self, title, id=None):
        self.title, self.id = title, id


class Score:
    B, D = 'B', 'D'

    def __init__(self, user_id, subject_id, score):
        self.user_id, self.subject_id, self.score = user_id, subject_id, score


class User:
    def __init__(self, username, id, role, passwords):
        self.username, self.id, self.role, self.password, = username, id, role, passwords
        self.subjects_scores = []

    @staticmethod
    def create_user(username, password, role):
        if len([x for x in [r'[a-z]', r'[A-Z]', r'[0-9]', r'[!$./_]'] if re.search(x, password)]) != 4:
            raise PasswordValidationException
        return User(username, uuid.NAMESPACE_URL, role.value, password)

    def add_score_for_subject(self, discipline: Subject, score: Score):
        self.subjects_scores += [{discipline.title: score if isinstance(score, str) else score.score}]

    def __str__(self):
        return f'{self.username} with role {self.role}: {self.subjects_scores}'


def get_subjects_from_json(subjects_json):
    with open(subjects_json, 'r') as f:
        return [Subject(item['title'], item["id"]) for item in json.load(f)]


def get_grades_from_json(grades_json):
    with open(grades_json, 'r') as f:
        return [Score(item['user_id'], item["subject_id"], item['score']) for item in json.load(f)]


def get_users_with_grades(users_json, subjects_json, grades_json):
    disciplines = get_subjects_from_json(subjects_json)
    grades = get_grades_from_json(grades_json)
    subjects_grades = [(discipline, grade) for grade in grades
                       for discipline in disciplines if grade.subject_id == discipline.id]

    with open(users_json, 'r') as u:
        list_users = [User(*user_.values()) for user_ in json.load(u)]

    for user_ in list_users:
        for item in subjects_grades:
            if item[1].user_id == user_.id:
                user_.add_score_for_subject(item[0], item[1])
    return list_users


def add_user(user_, users_):
    name_id = (user_.username, user_.id)
    for x in users_:
        if x.username in name_id and x.id in name_id:
            NonUniqueException.data = user_.username
            raise NonUniqueException
    users_.append(user_)


def add_subject(discipline, disciplines):
    for x in disciplines:
        if discipline == x:
            raise NonUniqueException(f"User with name {x} already exists")
    disciplines.append(discipline)


def get_grades_for_user(username: str, user_: User, users_: list):
    if user_.role == 0:
        raise ForbiddenException
    return [grade for user_ in users_ for grade in user_.subjects_scores if user_.username == username]


def users_to_json(users_, json_file):
    json_users = [{'username': x.username, 'id': x.id if type(x.id).__name__ != 'UUID' else 0,
                   'role': x.role, 'password': x.password} for x in users_]
    with open(json_file, 'w') as file:
        json.dump(json_users, file)


def subjects_to_json(disciplines, json_file):
    json_subjects = [{'title': x.title, 'id': x.id} for x in disciplines]
    with open(json_file, 'w') as file:
        json.dump(json_subjects, file)


def grades_to_json(users_, disciplines, json_file):
    json_users = []
    for user_ in users_:
        subjects_scores = {i: x[i] for x in user_.subjects_scores for i in x}
        for sub in disciplines:
            if sub.title in subjects_scores:
                json_users.append({'user_id': user_.id if type(user_.id).__name__ != 'UUID' else 0,
                                   'subject_id': sub.id, 'score': subjects_scores[sub.title]})
    with open(json_file, 'w') as file:
        json.dump(json_users, file)


def check_if_user_present(username, password, users_):
    for x in users_:
        if x.username == username and x.password == password:
            return True
    return False


def file_contains(path, key, value):
    with open(path) as file:
        for item in json.load(file):
            if key in item and item[key] == value:
                return False
    return True
