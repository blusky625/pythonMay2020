import pandas as pd
covid_data= pd.read_csv("https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_daily_reports/05-13-2020.csv")
covid_data['Active'] = covod_data['Confirmed'] -covid_data['Deaths']- covid_data['Recovered']

result = covid_data.groupby('Country/Region')['Confirmed', 'Deaths', 'Recovered', 'Active'].sum().reset_index()


print(result)

# Active

# Confirmed

# Deaths