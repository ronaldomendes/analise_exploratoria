import matplotlib.pyplot as plt
import pandas as pd

DATA_FIELDS = ['total_cases', 'total_deaths', 'total_tests', 'people_vaccinated', 'people_fully_vaccinated']

"""
Data rows:
iso_code,continent,location,date,total_cases,new_cases,new_cases_smoothed,total_deaths,new_deaths,new_deaths_smoothed,
total_cases_per_million,new_cases_per_million,new_cases_smoothed_per_million,total_deaths_per_million,
new_deaths_per_million,new_deaths_smoothed_per_million,reproduction_rate,icu_patients,icu_patients_per_million,
hosp_patients,hosp_patients_per_million,weekly_icu_admissions,weekly_icu_admissions_per_million,weekly_hosp_admissions,
weekly_hosp_admissions_per_million,total_tests,new_tests,total_tests_per_thousand,new_tests_per_thousand,
new_tests_smoothed,new_tests_smoothed_per_thousand,positive_rate,tests_per_case,tests_units,total_vaccinations,
people_vaccinated,people_fully_vaccinated,total_boosters,new_vaccinations,new_vaccinations_smoothed,
total_vaccinations_per_hundred,people_vaccinated_per_hundred,people_fully_vaccinated_per_hundred,
total_boosters_per_hundred,new_vaccinations_smoothed_per_million,new_people_vaccinated_smoothed,
new_people_vaccinated_smoothed_per_hundred,stringency_index,population,population_density,
median_age,aged_65_older,aged_70_older,gdp_per_capita,extreme_poverty,cardiovasc_death_rate,diabetes_prevalence,
female_smokers,male_smokers,handwashing_facilities,hospital_beds_per_thousand,life_expectancy,human_development_index,
excess_mortality_cumulative_absolute,excess_mortality_cumulative,excess_mortality,excess_mortality_cumulative_per_million

Sample info:
BRA,South America,Brazil,2021-02-25,10402913.0,68279.0,51872.714,251811.0,1575.0,1151.286,48613.233,319.071,242.403,
1176.723,7.36,5.38,1.11,,,,,,,,,34460303.0,133728.0,161.034,0.625,78653.0,0.368,,,tests performed,8101787.0,6346769.0,
1755018.0,,302787.0,223804.0,3.79,2.97,0.82,,1046.0,100898.0,0.047,,213993441.0,25.04,33.5,8.552,5.06,14103.452,3.4,
177.961,8.11,10.1,17.9,,2.2,75.88,0.765,,,,
"""

pd.options.display.max_rows = 10
data = pd.read_csv('arquivos/owid-covid-data.csv', delimiter=',')
brazil = data[data['location'] == 'Brazil']
cases = brazil[DATA_FIELDS]
print(cases)

# TODO tratar o resultados nulos que existem no CSV

# cases.plot()

cases.plot.area(figsize=(12, 4), subplots=True)
plt.savefig('grafico.png', dpi=300)

# fig, axs = plt.subplots(figsize=(12, 4))
# cases.plot.area(ax=axs)
# fig.savefig('grafico.png', dpi=300)

plt.show()
