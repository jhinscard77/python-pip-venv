import clase_27_mod as mod
import read_csv
import charts


def run():
    data = read_csv.read_csv('world_population.csv')
    # Esto funciona como filtro
    data = list(
        filter(lambda item: item['Continent'] == 'South America', data))

    countries = list(map(lambda x: x['Country/Territory'], data))
    percentages = list(map(lambda x: x['World Population Percentage'], data))
    # charts.generate_bar_chart(countries, percentages)
    charts.generate_pie_chart(countries, percentages)

    # Este codigo comentado hace la grafica de la poblacion de un pais que se esoja
    country = input('Type country => ')

    result = mod.population_by_country(data, country)

    if len(result) > 0:
        country = result[0]
        labels, values = mod.get_population(country)
        charts.generate_bar_chart(country['Country/Territory'], labels, values)


#  Este archivo es invocado como modulo en el archivo example.py
#  Para que pueda ser ejecutado directamente desde main.py debemos colocar el entry point
#  Este entry point permite ejecutar el archivo como modulo y como script sin tener conflictos


if __name__ == '__main__':
    run()
