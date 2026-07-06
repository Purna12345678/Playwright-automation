from graph.workflow import graph

state = {

    "url":
    input("Website URL : "),

    "brd_path":
    input("BRD PDF : "),

    "brd_text":"",

    "website":{},

    "requirements":{},

    "mapping":{},

    "generated_tests":[],

    "execution_results":[],

    "failures":[],

    "report_path":""
}

result = graph.invoke(state)

print(result)