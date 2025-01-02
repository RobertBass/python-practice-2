import utils
import charts
import read_csv

def run():
    data = read_csv.read_csv('./app/data.csv') 
    country = input("Que pais quieres verificar? ")
    res = utils.population_by_country(data, country)
    if len(res) > 0:
        country =  res[0]
        labels, values = utils.getPopulation(country)
        charts.generate_bar_char(labels, values)

    continent = input("Que continente quieres revisar? ")
    filtered = list(filter(lambda x: x['Continent'] == continent, data))
    countries, percentages = utils.getWorldPopulationPercentage(filtered)
    charts.generate_bar_char(countries, percentages)

if __name__ == "__main__":
    run()