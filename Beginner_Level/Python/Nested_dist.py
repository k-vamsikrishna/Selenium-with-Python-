employee_data = {
    "Vamsi": {"emp_id": 126, "join_date": "08-Sep-2021", "course": "python"},
    "Kowshik": {"emp_id": 178, "join_date": "25-July-2023", "course": "C++"}
}
print(employee_data["Kowshik"])

employee_data["Vamsi"]["phone_num"] = 9908734934
print(employee_data["Vamsi"])

print(employee_data["Vamsi"]["course"])

del employee_data["Vamsi"]["join_date"]
print(employee_data["Vamsi"])
