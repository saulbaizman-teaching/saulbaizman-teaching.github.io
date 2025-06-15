#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
This program creates a webpage with a list of courses I've taught.
"""

import csv

# page title
page_title = 'course websites'

# stylesheet filename
css_stylesheet = 'styles.css'

# courses filename
courses_tsv = 'courses.tsv'

# course names filename
course_names_tsv = 'course_names.tsv'


def format_link(url, target):
    """Format a link."""
    return f'<a href="{url}" target="_blank" rel="noopener">{target}</a>'


def get_header(title, stylesheet):
    """Return header."""
    return f'''
    <!DOCTYPE html>
    <html lang="en" dir="ltr">
    <head>
    <title>{title}</title>
    <meta name="viewport" content="width=device-width">
    <link href="https://fonts.googleapis.com/css?family=Oswald:300,500" rel="stylesheet" type="text/css">
    <link href="{stylesheet}" rel="stylesheet" type="text/css">
    </head>
    <body>
    <h1>{title}</h1>
    '''


def get_footer():
    """Return footer."""
    return '''
    </body>
    </html>
    '''


def get_course_names(tsv):
    """Return list of course names."""
    course_names_dict = {}
    with open(tsv, newline='') as tsv_file:
        course_names = csv.reader(tsv_file, delimiter="\t", quotechar='"')
        # skip header
        next(course_names)
        for row in course_names:
            course_number = row[0]
            course_name = row[1]
            course_number_clean = course_number.replace('-', ' ')
            # manual fix for one intensive.
            course_number_clean = course_number_clean.replace('2035i', '2035')
            course_names_dict[course_number] = {
                'name': course_name,
                'number': course_number_clean
            }
    return course_names_dict


def get_courses(tsv):
    """Return list of courses."""
    courses_list = []
    with open(tsv, newline='') as tsv_file:
        courses = csv.reader(tsv_file, delimiter="\t", quotechar='"')
        # skip header
        next(courses)
        for row in courses:
            number = row[0]
            url = row[1]
            section = row[2]
            season = row[3]
            year = row[4]
            courses_list.append({
                'number': number,
                'url': url,
                'section': section,
                'season': season,
                'year': year,
            })
    return courses_list


def main():
    """Output the content as a webpage."""

    body = []
    previous_semester = ''
    is_first_ul = True

    course_names = get_course_names(course_names_tsv)

    for course in get_courses(courses_tsv):
        current_semester = f'{course.get('season')} {course.get('year')}'
        course_name = course_names.get(course.get('number')).get('name')
        # do not use course.get('number'). it has a dash and an issue with a course exception.
        course_number = course_names.get(course.get('number')).get('number').upper()

        if current_semester != previous_semester:
            if not is_first_ul:
                body.append('</ul>')  # only print this if not on the first ul
            if is_first_ul:
                is_first_ul = False  # toggle the variable
            body.append(f'<h3>{current_semester}</h3>')
            body.append('<ul>')
        course_number_and_section = course_number
        if course.get('section') != '':
            # prepend a "0" to the section number via f-string format
            course_number_and_section += f'-{course.get('section'):0>2}'
        body.append('<li>' + format_link(
            url=course.get('url'),
            target=f'{course_name} <span class="course_number">{course_number_and_section}</span>'
        ) + '</li>')

        previous_semester = current_semester

    body.append('</ul>')

    # output the data
    print(get_header(title=page_title, stylesheet=css_stylesheet))
    print("\n".join(body))
    print(get_footer())


if __name__ == "__main__":
    main()
