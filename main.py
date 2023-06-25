import pandas as pd

# converting the text file to csv file
# data = open('/Users/sivasankar/PycharmProjects/pythonProject/givenData.txt').read()
# lines_of_data = data.splitlines()
# tmp = []
# for i in range(len(lines_of_data)):
#     tmp.append(lines_of_data[i].split())
# data_df = pd.DataFrame(tmp)
# data_df.to_csv('/Users/sivasankar/Documents/pythonTest/givenData2.csv')


df = pd.read_csv('/Users/sivasankar/Documents/pythonTest/givenData2.csv', chunksize=1000)
output = pd.DataFrame()
for chunk in df:
    category = ['F','A','Pts']
    details = chunk[category]
    details['count'] = 1
    summary = details.groupby(category).sum().reset_index()
    output = output.append(summary, ignore_index=True)
    print(summary.head())
    #
    final_output = output.groupby(category).sum().reset_index()
    final_output.sort_values('count')
    final_output.head()
    break