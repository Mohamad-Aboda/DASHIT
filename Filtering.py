import ETL as etl

def filter_date(startDate, endData, data):
    if(startDate == 'All' and endData == 'All'):
        return data
    days = len(data)
    new_data = []
    for i in range(days):
        if startDate <= data[i]['date'].iloc[0] and endData >= data[i]['date'].iloc[0]:
            new_data.append(data[i])
    
    return new_data


def filter_country(country, data):
    if country == 'All':
        return data
    else: 
        new_data = []
    
        for df in data:
            new_data.append(df[df['country'] == country])
        
        return new_data


def filter_city(city, data):
    if city == 'All':
        return data
    else: 
        new_data = []
    
        for df in data:
            new_data.append(df[df['city'] == city])
        
        return new_data


def filter_store(store, data):
    if store == 'All':
        return data
    else: 
        new_data = []
    
        for df in data:
            new_data.append(df[df['store'] == store])
        
        return new_data


def filter_product(product, data):
    if product == 'All':
        return data
    else: 
        new_data = []
    
        for df in data:
            new_data.append(df[df['product'] == product])
        
        return new_data


def filter_Brand(brand, data):
    if brand == 'All':
        return data
    else: 
        new_data = []
    
        for df in data:
            new_data.append(df[df['brand'] == brand])
        
        return new_data    


def applyFilters(location, startDate, endDate, country = 'All', city = 'All', store = 'All',brand = 'All', product = 'All'):
    filteredData = filter_date(startDate, endDate, etl.loadData(location))
    filteredData = filter_country(country, filteredData)
    filteredData = filter_city(city, filteredData)
    filteredData = filter_store(store, filteredData)
    filteredData = filter_Brand(brand, filteredData)
    filteredData = filter_product(product, filteredData)
    return filteredData
