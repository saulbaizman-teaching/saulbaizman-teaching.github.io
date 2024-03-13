#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
This program creates a webpage with a list of courses I've taught.
"""

css_stylesheet = 'styles.css'

course_names = {
    'cdgd-304': {
        'name': 'Web Design 1',
        'number': 'cdgd 304'
    },
    'cdgd-322': {
        'name': 'Information Architecture 2',
        'number': 'cdgd 322'
    },
    'cdgd-230': {
        'name': 'Typography 2',
        'number': 'cdgd 230'
    },
    'cdgd-342': {
        'name': 'Information Architecture 1',
        'number': 'cdgd 342'
    },
    'cdgd-206': {
        'name': 'Sophomore Graphic Design Studio',
        'number': 'cdgd 206'
    },
    'cmp-2035': {
        'name': 'Introduction to Web Design',
        'number': 'cmp 2035'
    },
    'idesn-2115': {
        'name': 'Introduction to Web Design',
        'number': 'idesn 2115'
    },
    'idesn-3535': {
        'name': 'Advanced Web Projects',
        'number': 'idesn 3535'
    },
    'cmp-2035i': {
        'name': 'Introduction to Web Design (intensive)',
        'number': 'cmp 2035'
    },
    'cmp-3011': {
        'name': 'Intermediate Web Design',
        'number': 'cmp 3011'
    },
    'dsgn-352': {
        'name': 'Designing with Data',
        'number': 'dsgn 352'
    },
    'dsgn-660': {
        'name': 'Design Symposium',
        'number': 'dsgn 660'
    },
    'art-3402': {
        'name': 'Interactive Design',
        'number': 'art 3402'
    },
}

semesters = {
    'fa14': {
        "season": "fall",
        "year": "2014"
    },
    'sp15': {
        "season": "spring",
        "year": "2015"
    },
    'fa15': {
        "season": "fall",
        "year": "2015"
    },
    'sp16': {
        "season": "spring",
        "year": "2016"
    },
    'su16': {
        "season": "summer",
        "year": "2016"
    },
    'fa16': {
        "season": "fall",
        "year": "2016"
    },
    'sp17': {
        "season": "spring",
        "year": "2017"
    },
    'fa17': {
        "season": "fall",
        "year": "2017"
    },
    'sp18': {
        "season": "spring",
        "year": "2018"
    },
    'fa18': {
        "season": "fall",
        "year": "2018"
    },
    'sp19': {
        "season": "spring",
        "year": "2019"
    },
    'fa19': {
        "season": "fall",
        "year": "2019"
    },
    'sp20': {
        "season": "spring",
        "year": "2020"
    },
    'fa20': {
        "season": "fall",
        "year": "2020"
    },
    'sp21': {
        "season": "spring",
        "year": "2021"
    },
    'fa21': {
        "season": "fall",
        "year": "2021"
    },
    'sp22': {
        "season": "spring",
        "year": "2022"
    },
    'fa22': {
        "season": "fall",
        "year": "2022"
    },
    'fa23': {
        "season": "fall",
        "year": "2023"
    },
}

# add new courses to the top of the list
courses = (
    {
        "course_name": course_names.get('cdgd-304').get('name'),
        "course_number": course_names.get('cdgd-304').get('number'),
        "course_url": "https://cdgd-304-01-fa23.courses.baizman.com",
        "course_section": "1",
        "semester": semesters.get('fa23')
    },
    {
        "course_name": course_names.get('cdgd-304').get('name'),
        "course_number": course_names.get('cdgd-304').get('number'),
        "course_url": "https://cdgd-304-01-fa22.courses.baizman.com",
        "course_section": "1",
        "semester": semesters.get('fa22')
    },
    {
        "course_name": course_names.get('art-3402').get('name'),
        "course_number": course_names.get('art-3402').get('number'),
        "course_url": "https://eclearn.emmanuel.edu/courses/3412590",
        "course_section": "1",
        "semester": semesters.get('sp22')
    },
    {
        "course_name": course_names.get('cdgd-230').get('name'),
        "course_number": course_names.get('cdgd-230').get('number'),
        "course_url": "https://classroom.google.com/c/NDQ0ODgyNzA2ODM0",
        "course_section": "1",
        "semester": semesters.get('sp22')
    },
    {
        "course_name": course_names.get('cdgd-304').get('name'),
        "course_number": course_names.get('cdgd-304').get('number'),
        "course_url": "https://cdgd-304-01-fa21.courses.baizman.com",
        "course_section": "1",
        "semester": semesters.get('fa21')
    },
    {
        "course_name": course_names.get('dsgn-660').get('name'),
        "course_number": course_names.get('dsgn-660').get('number'),
        "course_url": "https://discord.com/channels/796462787517612033/",
        "course_section": "1",
        "semester": semesters.get('sp21')
    },
    {
        "course_name": course_names.get('cdgd-304').get('name'),
        "course_number": course_names.get('cdgd-304').get('number'),
        "course_url": "https://cdgd-304-01-fa20.courses.baizman.com",
        "course_section": "1",
        "semester": semesters.get('fa20')
    },
    {
        "course_name": course_names.get('cdgd-304').get('name'),
        "course_number": course_names.get('cdgd-304').get('number'),
        "course_url": "https://cdgd-304-01-sp20.courses.baizman.com",
        "course_section": "1",
        "semester": semesters.get('sp20')
    },
    {
        "course_name": course_names.get('cdgd-304').get('name'),
        "course_number": course_names.get('cdgd-304').get('number'),
        "course_url": "https://cdgd-304-01-fa19.courses.baizman.com",
        "course_section": "1",
        "semester": semesters.get('fa19')
    },
    {
        "course_name": course_names.get('cdgd-322').get('name'),
        "course_number": course_names.get('cdgd-322').get('number'),
        "course_url": "https://cdgd-322-02-sp19.courses.baizman.com/",
        "course_section": "2",
        "semester": semesters.get('sp19')
    },
    {
        "course_name": course_names.get('cdgd-230').get('name'),
        "course_number": course_names.get('cdgd-230').get('number'),
        "course_url": "https://cdgd-230-02-sp19.courses.baizman.com/",
        "course_section": "2",
        "semester": semesters.get('sp19')
    },
    {
        "course_name": course_names.get('cdgd-304').get('name'),
        "course_number": course_names.get('cdgd-304').get('number'),
        "course_url": "https://cdgd-304-01-sp19.courses.baizman.com/",
        "course_section": "1",
        "semester": semesters.get('sp19')
    },
    {
        "course_name": course_names.get('cdgd-342').get('name'),
        "course_number": course_names.get('cdgd-342').get('number'),
        "course_url": "https://cdgd-342-02-fa18.courses.baizman.com/",
        "course_section": "2",
        "semester": semesters.get('fa18')
    },
    {
        "course_name": course_names.get('cdgd-206').get('name'),
        "course_number": course_names.get('cdgd-206').get('number'),
        "course_url": "https://cdgd-206-01-fa18.courses.baizman.com/",
        "course_section": "1",
        "semester": semesters.get('fa18')
    },
    {
        "course_name": course_names.get('cdgd-206').get('name'),
        "course_number": course_names.get('cdgd-206').get('number'),
        "course_url": "https://cdgd-206-02-fa18.courses.baizman.com/",
        "course_section": "2",
        "semester": semesters.get('fa18')
    },
    {
        "course_name": course_names.get('cdgd-206').get('name'),
        "course_number": course_names.get('cdgd-206').get('number'),
        "course_url": "https://cdgd-206-03-fa18.courses.baizman.com/",
        "course_section": "3",
        "semester": semesters.get('fa18')
    },
    {
        "course_name": course_names.get('cdgd-304').get('name'),
        "course_number": course_names.get('cdgd-304').get('number'),
        "course_url": "https://cdgd-304-01-fa18.courses.baizman.com/",
        "course_section": "1",
        "semester": semesters.get('fa18')
    },
    {
        "course_name": course_names.get('cdgd-322').get('name'),
        "course_number": course_names.get('cdgd-322').get('number'),
        "course_url": "https://cdgd-322-02-sp18.courses.baizman.com/",
        "course_section": "2",
        "semester": semesters.get('sp18')
    },
    {
        "course_name": course_names.get('cdgd-230').get('name'),
        "course_number": course_names.get('cdgd-230').get('number'),
        "course_url": "https://cdgd-230-01-sp18.courses.baizman.com/",
        "course_section": "2",
        "semester": semesters.get('sp18')
    },
    {
        "course_name": course_names.get('cdgd-342').get('name'),
        "course_number": course_names.get('cdgd-342').get('number'),
        "course_url": "https://saulbaizman-massart.github.io/cdgd-342-02-fa17/",
        "course_section": "2",
        "semester": semesters.get('fa17')
    },
    {
        "course_name": course_names.get('cdgd-304').get('name'),
        "course_number": course_names.get('cdgd-304').get('number'),
        "course_url": "https://saulbaizman-massart.github.io/cdgd-304-01-fa17/",
        "course_section": "1",
        "semester": semesters.get('fa17')
    },
    {
        "course_name": course_names.get('cdgd-206').get('name'),
        "course_number": course_names.get('cdgd-206').get('number'),
        "course_url": "https://saulbaizman-massart.github.io/cdgd-206-fa17/",
        "course_section": "",
        "semester": semesters.get('fa17')
    },
    {
        "course_name": course_names.get('cdgd-322').get('name'),
        "course_number": course_names.get('cdgd-322').get('number'),
        "course_url": "https://saulbaizman-massart.github.io/cdgd-322-02-sp17/",
        "course_section": "",
        "semester": semesters.get('sp17')
    },
    {
        "course_name": course_names.get('cmp-2035').get('name'),
        "course_number": course_names.get('cmp-2035').get('number'),
        "course_url": "https://saulbaizman-smfa.github.io/cmp-2035-sp17/",
        "course_section": "",
        "semester": semesters.get('sp17')
    },
    {
        "course_name": course_names.get('cdgd-342').get('name'),
        "course_number": course_names.get('cdgd-342').get('number'),
        "course_url": "https://cdgd-342-fa16.slack.com/",
        "course_section": "",
        "semester": semesters.get('fa16')
    },
    {
        "course_name": course_names.get('idesn-2115').get('name'),
        "course_number": course_names.get('idesn-2115').get('number'),
        "course_url": "https://idesn-2115-fa16.slack.com/",
        "course_section": "",
        "semester": semesters.get('fa16')
    },
    {
        "course_name": course_names.get('idesn-3535').get('name'),
        "course_number": course_names.get('idesn-3535').get('number'),
        "course_url": "https://idesn-3535-fa16.slack.com/",
        "course_section": "",
        "semester": semesters.get('fa16')
    },
    {
        "course_name": course_names.get('cmp-2035i').get('name'),
        "course_number": course_names.get('cmp-2035i').get('number'),
        "course_url": "https://cmp-2035-su16.slack.com/",
        "course_section": "",
        "semester": semesters.get('su16')
    },
    {
        "course_name": course_names.get('cmp-2035').get('name'),
        "course_number": course_names.get('cmp-2035').get('number'),
        "course_url": "https://cmp-2035-s16.slack.com/",
        "course_section": "",
        "semester": semesters.get('sp16')
    },
    {
        "course_name": course_names.get('cmp-3011').get('name'),
        "course_number": course_names.get('cmp-3011').get('number'),
        "course_url": "https://cmp-3011-s16.slack.com/",
        "course_section": "",
        "semester": semesters.get('sp16')
    },
    {
        "course_name": course_names.get('cmp-2035').get('name'),
        "course_number": course_names.get('cmp-2035').get('number'),
        "course_url": "https://cmp-2035-f15.slack.com/",
        "course_section": "",
        "semester": semesters.get('fa15')
    },
    {
        "course_name": course_names.get('dsgn-352').get('name'),
        "course_number": course_names.get('dsgn-352').get('number'),
        "course_url": "https://dsgn-352-f15.slack.com/",
        "course_section": "",
        "semester": semesters.get('fa15')
    },
    {
        "course_name": course_names.get('cmp-3011').get('name'),
        "course_number": course_names.get('cmp-3011').get('number'),
        "course_url": "https://cmp-3011-c1-sp15.slack.com/",
        "course_section": "",
        "semester": semesters.get('sp15')
    },
    {
        "course_name": course_names.get('cmp-2035').get('name'),
        "course_number": course_names.get('cmp-2035').get('number'),
        "course_url": "https://cmp-2035-c1-fa14.slack.com/",
        "course_section": "",
        "semester": semesters.get('fa14')
    },
)

output_filename = "index.html"

page_title = 'course websites'


def format_link(url, target):
    """Format a link."""
    return f'<a href="{url}" target="_blank" rel="noopener">{target}</a>'


def main():
    """ Output webpage to a file. """

    header = f'''
    <!DOCTYPE html>
    <html lang="en" dir="ltr">
    <head>
    <title>{page_title}</title>
    <meta name="viewport" content="width=device-width">
    <link href="https://fonts.googleapis.com/css?family=Oswald:300,500" rel="stylesheet" type="text/css">
    <link href="{css_stylesheet}" rel="stylesheet" type="text/css">
    </head>
    <body>
    <h1>{page_title}</h1>
    '''

    footer = '''
    </body>
    </html>
    '''

    content = []

    previous_semester = ''
    is_first_ul = True
    for course in courses:
        current_semester = f'{course["semester"]["season"]} {course["semester"]["year"]}'
        if current_semester != previous_semester:
            if not is_first_ul:
                content.append('</ul>')  # only print this if not on the first ul
            if is_first_ul:
                is_first_ul = False  # toggle the variable
            content.append(f'<h3>{current_semester}</h3>')
            content.append('<ul>')
        if course['course_section'] != '':
            course_number_and_section = f'{course['course_number'].upper()}-0{course['course_section']}'
        else:
            course_number_and_section = course['course_number'].upper()
        content.append('<li>' + format_link(course['course_url'],
                                            f'{course['course_name']} <span class="course_number">{course_number_and_section}</span>') + '</li>')

        previous_semester = current_semester

    content.append('</ul>')

    # write to the file
    index = open(output_filename, "w")
    index.write(header)
    index.write("\n".join(content))
    index.write(footer)
    index.close()


if __name__ == "__main__":
    main()
