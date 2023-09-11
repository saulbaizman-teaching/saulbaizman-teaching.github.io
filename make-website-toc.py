#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''
This program creates a webpage with a list of courses I've taught.
'''

css_stylesheet='styles.css'

# course name, course number, url, semester

# add new course names to the bottom of the list
course_names = (
{
"name":       "Web Design 1", # 0
"number":     "cdgd 304"
},
{
"name":       "Information Architecture 2", # 1
"number":     "cdgd 322"
},
{
"name":       "Typography 2", # 2
"number":     "cdgd 230"
},
{
"name":       "Information Architecture 1", # 3
"number":     "cdgd 342"
},
{
"name":       "Sophomore Graphic Design Studio", # 4
"number":     "cdgd 206"
},
{
"name":       "Introduction to Web Design", # 5
"number":     "cmp 2035"
},
{
"name":       "Introduction to Web Design", # 6
"number":     "idesn 2115"
},
{
"name":       "Advanced Web Projects", # 7
"number":     "idesn 3535"
},
{
"name":       "Introduction to Web Design (intensive)", # 8
"number":     "cmp 2035"
},
{
"name":       "Intermediate Web Design", # 9
"number":     "cmp 3011"
},
{
"name":       "Designing with Data", # 10
"number":     "dsgn 352"
},
{
"name":       "Design Symposium", # 11
"number":     "dsgn 660"
},
{
"name":       "Interactive Design", # 12
"number":     "art 3402"
},
)

# add new semesters to the bottom of the list
semesters = (
{ #0
"season":     "fall",
"year":       "2014"
},
{ #1
"season":     "spring",
"year":       "2015"
},
{ #2
"season":     "fall",
"year":       "2015"
},
{ #3
"season":     "spring",
"year":       "2016"
},
{ #4
"season":     "summer",
"year":       "2016"
},
{ #5
"season":     "fall",
"year":       "2016"
},
{ #6
"season":     "spring",
"year":       "2017"
},
{ #7
"season":     "fall",
"year":       "2017"
},
{ #8
"season":     "spring",
"year":       "2018"
},
{ #9
"season":     "fall",
"year":       "2018"
},
{ #10
"season":     "spring",
"year":       "2019"
},
{ #11
"season":     "fall",
"year":       "2019"
},
{ #12
"season":     "spring",
"year":       "2020"
},
{ #13
"season":     "fall",
"year":       "2020"
},
{ #14
"season":     "spring",
"year":       "2021"
},
{ #15
"season":     "fall",
"year":       "2021"
},
{ #16
"season":     "spring",
"year":       "2022"
},
{ #17
"season":     "fall",
"year":       "2022"
},
{ #18
"season":     "fall",
"year":       "2023"
},
)

# add new courses to the top of the list
courses = (
# fa23
{
"course_name":        course_names[0]["name"],
"course_number":      course_names[0]["number"],
"course_url":         "https://cdgd-304-01-fa23.courses.baizman.com",
"course_section":     "1",
"semester":           semesters[18]
},
# fa22
{
"course_name":        course_names[0]["name"],
"course_number":      course_names[0]["number"],
"course_url":         "https://cdgd-304-01-fa22.courses.baizman.com",
"course_section":     "1",
"semester":           semesters[17]
},
# sp22
{
"course_name":        course_names[12]["name"],
"course_number":      course_names[12]["number"],
"course_url":         "https://eclearn.emmanuel.edu/courses/3412590",
"course_section":     "1",
"semester":           semesters[16]
},
{
"course_name":        course_names[2]["name"],
"course_number":      course_names[2]["number"],
"course_url":         "https://classroom.google.com/c/NDQ0ODgyNzA2ODM0",
"course_section":     "1",
"semester":           semesters[16]
},
# fa21
{
"course_name":        course_names[0]["name"],
"course_number":      course_names[0]["number"],
"course_url":         "https://cdgd-304-01-fa21.courses.baizman.com",
"course_section":     "1",
"semester":           semesters[15]
},
# sp21
{
"course_name":        course_names[11]["name"],
"course_number":      course_names[11]["number"],
"course_url":         "https://discord.com/channels/796462787517612033/",
"course_section":     "1",
"semester":           semesters[14]
},
# fa20
{
"course_name":        course_names[0]["name"],
"course_number":      course_names[0]["number"],
"course_url":         "https://cdgd-304-01-fa20.courses.baizman.com",
"course_section":     "1",
"semester":           semesters[13]
},
# sp20
{
"course_name":      course_names[0]["name"],
"course_number":    course_names[0]["number"],
"course_url":       "https://cdgd-304-01-sp20.courses.baizman.com",
"course_section":   "1",
"semester":         semesters[12]
},
# fa19
{
"course_name":      course_names[0]["name"],
"course_number":    course_names[0]["number"],
"course_url":       "https://cdgd-304-01-fa19.courses.baizman.com",
"course_section":   "1",
"semester":         semesters[11]
},
# sp19
{
"course_name":      course_names[1]["name"],
"course_number":    course_names[1]["number"],
"course_url":       "https://cdgd-322-02-sp19.courses.baizman.com/",
"course_section":   "2",
"semester":         semesters[10]
},
{
"course_name":      course_names[2]["name"],
"course_number":    course_names[2]["number"],
"course_url":       "https://cdgd-230-02-sp19.courses.baizman.com/",
"course_section":   "2",
"semester":         semesters[10]
},
{
"course_name":      course_names[0]["name"],
"course_number":    course_names[0]["number"],
"course_url":       "https://cdgd-304-01-sp19.courses.baizman.com/",
"course_section":   "1",
"semester":         semesters[10]
},
# fa18
{
"course_name":      course_names[3]["name"],
"course_number":    course_names[3]["number"],
"course_url":       "https://cdgd-342-02-fa18.courses.baizman.com/",
"course_section":   "2",
"semester":         semesters[9]
},
{
"course_name":      course_names[4]["name"],
"course_number":    course_names[4]["number"],
"course_url":       "https://cdgd-206-01-fa18.courses.baizman.com/",
"course_section":   "1",
"semester":         semesters[9]
},
{
"course_name":      course_names[4]["name"],
"course_number":    course_names[4]["number"],
"course_url":       "https://cdgd-206-02-fa18.courses.baizman.com/",
"course_section":   "2",
"semester":         semesters[9]
},
{
"course_name":      course_names[4]["name"],
"course_number":    course_names[4]["number"],
"course_url":       "https://cdgd-206-03-fa18.courses.baizman.com/",
"course_section":   "3",
"semester":         semesters[9]
},
{
"course_name":      course_names[0]["name"],
"course_number":    course_names[0]["number"],
"course_url":       "https://cdgd-304-01-fa18.courses.baizman.com/",
"course_section":   "1",
"semester":         semesters[9]
},
# sp18
{
"course_name":      course_names[1]["name"],
"course_number":    course_names[1]["number"],
"course_url":       "https://cdgd-322-02-sp18.courses.baizman.com/",
"course_section":   "2",
"semester":         semesters[8]
},
{
"course_name":      course_names[2]["name"],
"course_number":    course_names[2]["number"],
"course_url":       "https://cdgd-230-01-sp18.courses.baizman.com/",
"course_section":   "2",
"semester":         semesters[8]
},
# fa17
{
"course_name":      course_names[3]["name"],
"course_number":    course_names[3]["number"],
"course_url":       "https://saulbaizman-massart.github.io/cdgd-342-02-fa17/",
"course_section":   "2",
"semester":         semesters[7]
},
{
"course_name":      course_names[0]["name"],
"course_number":    course_names[0]["number"],
"course_url":       "https://saulbaizman-massart.github.io/cdgd-304-01-fa17/",
"course_section":   "1",
"semester":         semesters[7]
},
{
"course_name":      course_names[4]["name"],
"course_number":    course_names[4]["number"],
"course_url":       "https://saulbaizman-massart.github.io/cdgd-206-fa17/",
"course_section":   "",
"semester":         semesters[7]
},
# sp17
{
"course_name":      course_names[1]["name"],
"course_number":    course_names[1]["number"],
"course_url":       "https://saulbaizman-massart.github.io/cdgd-322-02-sp17/",
"course_section":   "",
"semester":         semesters[6]
},
{
"course_name":      course_names[5]["name"],
"course_number":    course_names[5]["number"],
"course_url":       "https://saulbaizman-smfa.github.io/cmp-2035-sp17/",
"course_section":   "",
"semester":         semesters[6]
},
# fa16
{
"course_name":      course_names[3]["name"],
"course_number":    course_names[3]["number"],
"course_url":       "https://cdgd-342-fa16.slack.com/",
"course_section":   "",
"semester":         semesters[5]
},
{
"course_name":      course_names[6]["name"],
"course_number":    course_names[6]["number"],
"course_url":       "https://idesn-2115-fa16.slack.com/",
"course_section":   "",
"semester":         semesters[5]
},
{
"course_name":      course_names[7]["name"],
"course_number":    course_names[7]["number"],
"course_url":       "https://idesn-3535-fa16.slack.com/",
"course_section":   "",
"semester":         semesters[5]
},
# su16
{
"course_name":      course_names[8]["name"],
"course_number":    course_names[8]["number"],
"course_url":       "https://cmp-2035-su16.slack.com/",
"course_section":   "",
"semester":         semesters[4]
},
# sp16
{
"course_name":      course_names[5]["name"],
"course_number":    course_names[5]["number"],
"course_url":       "https://cmp-2035-s16.slack.com/",
"course_section":   "",
"semester":         semesters[3]
},
{
"course_name":      course_names[9]["name"],
"course_number":    course_names[9]["number"],
"course_url":       "https://cmp-3011-s16.slack.com/",
"course_section":   "",
"semester":         semesters[3]
},
# fa15
{
"course_name":      course_names[5]["name"],
"course_number":    course_names[5]["number"],
"course_url":       "https://cmp-2035-f15.slack.com/",
"course_section":   "",
"semester":         semesters[2]
},
{
"course_name":      course_names[10]["name"],
"course_number":    course_names[10]["number"],
"course_url":       "https://dsgn-352-f15.slack.com/",
"course_section":   "",
"semester":         semesters[2]
},
# sp15
{
"course_name":      course_names[9]["name"],
"course_number":    course_names[9]["number"],
"course_url":       "https://cmp-3011-c1-sp15.slack.com/",
"course_section":   "",
"semester":         semesters[1]
},
# fa14
{
"course_name":      course_names[5]["name"],
"course_number":    course_names[5]["number"],
"course_url":       "https://cmp-2035-c1-fa14.slack.com/",
"course_section":   "",
"semester":         semesters[0]
},
)


output_filename = "index.html"


import os

def format_link ( url, target ) :
    """Format a link."""
    return '<a href="%s" target="_blank" rel="noopener">%s</a>' % ( url, target )

page_title = 'course websites'

header='''
<!DOCTYPE html>
<html lang="en" dir="ltr">
<head>
<title>%s</title>
<meta name="viewport" content="width=device-width">
<link href="https://fonts.googleapis.com/css?family=Oswald:300,500" rel="stylesheet" type="text/css">
<link href="%s" rel="stylesheet" type="text/css">
</head>
<body>
<h1>%s</h1>
''' % ( page_title, css_stylesheet, page_title )

footer='''
</body>
</html>
'''

content = []

previous_semester = ''
is_first_ul = True
for course in courses:
    #print (course['course_name'])
    #print (course)
    current_semester = '%s %s' % ( course["semester"]["season"], course["semester"]["year"] )
    #print ("current_semester: %s" % current_semester)
    #print ("previous_semester: %s" % previous_semester)
    if current_semester != previous_semester:
        if not is_first_ul:
            content.append ( '</ul>' ) # only print this if not on the first ul
        if is_first_ul:
            is_first_ul = False # toggle the variable
        content.append ('<h3>%s</h3>' % ( current_semester ) )
        content.append ( '<ul>' )
    if course['course_section'] != '':
        course_number_and_section = '%s-0%s' % ( course['course_number'].upper(), course['course_section'] )
    else:
        course_number_and_section = '%s' % course['course_number'].upper()
    content.append ( '<li>%s</li>' % format_link ( course['course_url'], '%s <span class="course_number">%s</span>' % ( course['course_name'], course_number_and_section ) ) )

    previous_semester = current_semester

content.append ( '</ul>' )

# write to the file
index = open(output_filename, "w")
index.write(header)
index.write("\n".join(content))
index.write(footer)
index.close()
