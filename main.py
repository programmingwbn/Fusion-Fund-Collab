from summary import getContent, summarize, getBart, getHeaders
from excel import *


websites = [
    {
        "OpenAI" : [ 
            "https://en.wikipedia.org/wiki/OpenAI"

        ],
        "SAIL" : [
            "https://web.stanford.edu/~learnest/sail/"

        ],
        "BAIR" : [
            "https://bair.berkeley.edu/blog/"

        ],
        "Vector" : [
            "https://vectorinstitute.ai/vector-institute-2022-23-annual-report-accelerating-ai-in-ontario/"

        ],
        "CMU" : [
            "https://en.wikipedia.org/wiki/Robotics_Institute"

        ],
        "FAIR" : [
            "https://en.wikipedia.org/wiki/Meta_AI"

        ],
        "GoogleAI" : [
            "https://en.wikipedia.org/wiki/Google_AI"

        ],
        "AI2" : [
            "https://en.wikipedia.org/wiki/Allen_Institute_for_AI"

        ],
        "DeepMind" : [
            "https://en.wikipedia.org/wiki/Google_DeepMind"

        ]
                        
    }
            
]

def collectData():
    keys = list(websites[0].keys())

    for i in range(len(websites[0])):
        summary = []
        for k in range(len(websites[0][keys[i]])):
            summarize(keys[i], websites[0][keys[i]][k])
        print(summary) 
        toExcel(summary, keys[i])
    

# collectData()

# content = getContent("https://en.wikipedia.org/wiki/OpenAI")

# summarize("OpenAI", "https://en.wikipedia.org/wiki/OpenAI")
# print(weeklySummary)
# toExcel()
