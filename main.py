# write program to send mass email using a template

## read the template from file, the fields <fieldname> are to filled by the recipient's information
with open("email_template.txt", "r",encoding="utf-8") as file:
    template = file.read()


## read the excel file that contains information of each recipient
import pandas as pd
df = pd.read_excel("recipients.xlsx")

## iterate over the rows of the dataframe and create a message for each recipient

for index, row in df.iterrows():
    message = template.replace("<项目>", row["项目"])
    message = message.replace("<学制>", row["学制"])
    message = message.replace("<email>", row["email"])

    ## send the message to the recipient



    ## print the message to the console
    print(message)

    ## save the message to a file



