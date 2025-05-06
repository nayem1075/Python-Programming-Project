
studentId = {

    "101" : "Nayem Uddin",
    "102" : "Faisal",
    "103" : "Fahim",
    "104" : "Rakib",
}
print(studentId["101"])
#print(studentId["105"]...error
print(studentId.get("104"))
print(studentId.get("107"))
print(studentId.get("106","Not a valid key"))
print(studentId.get("103","Not a valid key"))