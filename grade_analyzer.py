def process_scores(students):

  averages = {}
  for name,scores in students.items():
    total = 0
    for score in scores:
      total+= score
    avg = total /len(scores)
    averages[name]= round(avg,2)
  return averages

def classify_grades(averages):
  result = {}

  for name, avg in averages.items():
    if avg >= 90:
      result[name] =(avg,"A")
    elif avg >= 80:
      result[name] =(avg,"B") 
    elif avg >= 70:
      result[name] =(avg,"C")
    elif avg >= 60:
      result[name] =(avg,"D")
    else:
      result[name] =(avg,"F")
  return result

def generate_report(classified, passing_avg=70):
  passed = 0
  total = len(classified)
  print("===== Student Grade Report =====")

  for name , data in classified.items():
    avg = data[0]
    grade = data[1]

    if avg >= passing_avg:
      status = "passed"
      passed += 1
    else:
      status ='failed'
    print(name, "| Avg:", avg, "| Grade:", grade, "| Status:", status)
  print("================================")

  failed = total - passed

  print("Total Students :", total)
  print("Passed         :", passed)
  print("Failed         :", failed)

  return passed

students = {
  'sanjay':[90,89,89],
  'sai':[80,85,88],
  'suman':[70,75,80]
}
averages_1 = process_scores(students)
print(averages_1)
classified_1 = classify_grades(averages_1)
print(classified_1)
report = generate_report(classified_1)
print(report)
