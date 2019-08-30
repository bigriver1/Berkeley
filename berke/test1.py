import json
introduce = ""
json1 = json.loads('{"assignedInstructors":[{"assignmentNumber":1,"instructor":{"identifiers":[{"type":"campus-uid","id":"10036","disclose":true}],"names":[{"type":{"code":"PRF","description":"Preferred"},"familyName":"Taylor","givenName":"Ula","formattedName":"Ula Y Taylor","disclose":true,"uiControl":{"code":"U","description":"Edit - No Delete"},"fromDate":"1902-02-01"},{"type":{"code":"PRI","description":"Primary"},"familyName":"Taylor","givenName":"Ula","formattedName":"Ula Yvette Taylor","disclose":true,"uiControl":{"code":"D","description":"Display Only"},"fromDate":"2019-08-01"}]},"role":{"code":"PI","description":"1-TIC","formalDescription":"Teaching and In Charge"},"printInScheduleOfClasses":true,"gradeRosterAccess":{"code":"A","description":"Approve","formalDescription":"Approve"}},{"assignmentNumber":2,"instructor":{"identifiers":[{"type":"campus-uid","id":"966762","disclose":true}],"names":[{"type":{"code":"PRF","description":"Preferred"},"familyName":"Pegs","givenName":"Mariko","formattedName":"Mariko M Pegs","disclose":false,"uiControl":{"code":"U","description":"Edit - No Delete"},"fromDate":"1902-02-01"},{"type":{"code":"PRI","description":"Primary"},"familyName":"Pegs","givenName":"Mariko","formattedName":"Mariko M Pegs","disclose":false,"uiControl":{"code":"D","description":"Display Only"},"fromDate":"2019-05-28"}]},"role":{"code":"TNIC","description":"2-TNIC","formalDescription":"Teaching but Not In Charge"},"printInScheduleOfClasses":true,"gradeRosterAccess":{"code":"G","description":"Grade","formalDescription":"Grade"}}]}')
item = {'info': 'https://classes.berkeley.edu/content/2019-fall-yiddish-103-001-lec-001', 'course_title': '103', 'week': 'TuTh', 'location': 'Mulford 106', 'course_number': '001', 'units': 3, 'location_url': 'http://www.berkeley.edu/map/?mulford', 'time': '11:00:00-12:29:00', 'name': 'Readings in Yiddish', 'instructor': 'Chloe Li Piazza,Yael  Chaver,Chloe L Piazza', 'dept': 'German', 'type': 'Lecture', 'introduce': 'Study of selected Yiddish texts including prose, poetry, and drama, from various periods and geographic areas, in the context of time and place. Review of relevant grammatical topics. Increased attention to the Hebrew/Aramaic component. Selections may vary from semester to semester. '}
xx = []
# print(acr1)
# print(acr2)
# print(acr3)
# # for i in
# # print (s.keys())
# a = json1['assignedInstructors']
# for b in a:
# #
#     # for c in b['instructor']:
#     # print(b['assignmentNumber'])
#     for c in b['instructor']['names']:
#         # x = set(c['formattedName'])
#         # print(x)
#         names = c['formattedName']
#         xx.append(names)
#         aa = set(xx)
#         # aa = ",".join(aa)
# print(aa)
# instructor = []
# for b in a:
#     # print(b["instructor"]["names"])
#     for c in b["instructor"]["names"]:
#         instructor1 = c["formattedName"]
#         instructor.append(instructor1)
#         instructor2 = set(instructor)
#         instructor2 = ",".join(instructor2)
# #         # names = ",".join(names)
# print(instructor2)

# d={'name':'cheng','age':20,'sex':'female'}
# #创建空列表
# a=[]
# #将字典中键和值循环取出添加到列表中
# for i in d.keys():
# 	a.append(i)
# 	a.append(d[i])
# print(a)

# instroutor = ["Patricia A. Kubala", "Rosemary  Joyce", "Patricia A Kubala"]
#
# print(item['instructor'])
# num = len(instroutor)
# if num == 1:
#     s1 = instroutor[0]
#     print(s1)
# elif num == 2:
#     s1 = instroutor[0]
#     s2 = instroutor[1]
#     acr1 = [i[0] for i in s1.split(" ")]
#     acr2 = [i[0] for i in s2.split("  ")]
#     if acr1 == acr2:
#         print(s1)
#     else:
#         print(s1, s2)
#
#     print(s1, s2)
# elif num == 3:
#     s1 = instroutor[0]
#     s2 = instroutor[1]
#     s3 = instroutor[2]
#     acr1 = [i[0] for i in s1.split(" ")]
#     acr2 = [i[0] for i in s2.split("  ")]
#     acr3 = [i[0] for i in s3.split(" ")]
#     if acr1 == acr2 == acr3:
#         print(s1)
#     elif acr1 == acr2 != acr3:
#         print(s1, s3)
#     elif acr1 != acr2 == acr3:
#         print(s1, s2)
#     elif acr1 != acr2 != acr3:
#         print(s1, s2, s3)
#     else:
#         print(s2, s3)
#     # print(s1, s2, s3)
# else:
#     s1 = instroutor[0]
#     s2 = instroutor[1]
#     s3 = instroutor[2]
#     s4 = instroutor[3]
#     acr1 = [i[0] for i in s1.split(" ")]
#     acr2 = [i[0] for i in s2.split("  ")]
#     acr3 = [i[0] for i in s3.split(" ")]
#     acr4 = [i[0] for i in s4.split(" ")]
#     if acr1 == acr2 == acr3 ==acr4:
#         print(s1)
#     elif acr1 == acr2 == acr3 != acr4:
#         print(s1, s4)
#     elif acr1 == acr2 != acr3 == acr4:
#         print(s1, s3)
#     elif acr1 != acr2 == acr3 == acr4:
#         print(s1, s2)
#     elif acr1 != acr2 != acr3 == acr4:
#         print(s1, s2, s3)
#     elif acr1 == acr2 != acr3 != acr4:
#         print(s1, s3, s4)
#     elif acr1 != acr2 == acr3 != acr4:
#         print(s1, s2, s4)
#     elif acr1 != acr2 != acr3 != acr4:
#         print(s1, s2, s3, s4)
#     else:
#         pass

    # print(s1, s2, s3, s4)
# instructor = instructor.split(",")
# print(instructor)
# s = "Chloe Li Piazza,Yael  Chaver,Chloe L Piazza"
# s1 = "Chloe Li Piazza"
# s2 = "Chloe L Piazza"
# s3 = "Chloe w. Piazza"
# acr = [i[0] for i in i.split(" ")]

# acr1 = [i[0] for i in s1.split(" ")]
# acr2 = [i[0] for i in s2.split(" ")]
# acr3 = [i[0] for i in s3.split(" ")]
# print(acr)
# if acr1 == acr2 and acr1 == acr3 and acr2 == acr3:
#     print(s1)
# elif acr1 == acr2 and acr1 == acr3 and acr3 != acr2:
#     print(s1, s2, s3)

