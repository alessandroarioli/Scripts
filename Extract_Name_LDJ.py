import os
import subprocess
import urllib2
import re

def Extractor(file_path_emails, file_out):
        names=""
        with open(file_path_emails) as f:
                for line in f:
                        if ("marketing") in line:
                            f1=open(file_out, 'a')
                            substring = re.search(r'@.*?\.', line).group()
                            names += substring
                            print(names)
                            f1.write(line + '\n')
                            print(line)
                            f1.close()

                        elif ("sales") in line:
                            f1=open(file_out, 'a')
                            substring = re.search(r'@.*?\.', line).group()
                            names += substring
                            print(names)
                            f1.write(line + '\n')
                            print(line)
                            f1.close()

        with open(file_path_emails) as f:
                for lineAgain in f:
                            if ("contact") in lineAgain:
                                    f1=open(file_out, 'a')
                                    substring = re.search(r'@.*?\.', lineAgain).group()
                                    if substring in names:
                                        print(names)
                                    else:
                                        f1.write(lineAgain + '\n')
                                        print(lineAgain)
                                        f1.close()
                            else:
                                    if ("info") in lineAgain:
                                        f1=open(file_out, 'a')
                                        substring = re.search(r'@.*?\.', lineAgain).group()
                                        if substring in names:
                                            print(names)
                                        else:
                                            f1.write(lineAgain + '\n')
                                            print(lineAgain)
                                            f1.close()


def GradeExtractor(file_mails, file_grade, file_out):
    emails = []
    grades = []
    positions_ok = []
    emails_ok = []
    with open(file_mails) as file:
        for line in file:
            emails.append(line)
    with open(file_grade) as Gfile:
        for line in Gfile:
            if (line != "+" and line != "\n"):
                grades.append(line)
    print emails.__len__()
    print grades.__len__()
    for i, grade in enumerate(grades):
        if grade != "\n" and (grade == "A+\n" or grade == "A\n" or grade == "B\n"):
            emails_ok.append(emails[i])
    for email in emails_ok:
        f1 = open(file_out, 'a')
        f1.write(email)
        f1.close()


# Extractor('/users/dev-01/Desktop/Marketing2.txt', '/users/dev-01/Desktop/Marketing_Pulito.txt')
# GradeExtractor('/users/dev-01/Desktop/EmailsMarketing', '/users/dev-01/Desktop/GradoMarketing', '/users/dev-01/Desktop/Marketing2.txt')