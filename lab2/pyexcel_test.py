import pyexcel

#2 Prepare data
list_of_dicts = [
    {
        "name":"1",
        "number":"one",
    },
    {
        "name":"2",
        "number":"two",
    },
    {
        "name":"3",
        "number":"three",
    },
    {
        "name":"4",
        "number":"four"
    }
]
# List comprehension = convert list a into list b ???


#3 Save file using save_as()
pyexcel.save_as(records=list_of_dicts,dest_file_name="crap.xls")