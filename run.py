import pandas as pd
import os
import sys

from web_scraping.web_scraping import scraper, transformer, writer, reader


URL = "https://id.wikipedia.org/wiki/Daftar_orang_terkaya_di_Indonesia"
DB_NAME = "web_scraping_db"
DB_USER = "username"
DB_PASSWORD = "secret"
DB_HOST = "db"
DB_PORT = "5432"
CONNECTION_STRING = f"postgresql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
TABLE_NAME = "orang_terkaya_indonesia"


def main() -> None:
    dfs = scraper.scrape(URL)
    data_list = []
    years_list = ["2006", "2007", "2008", "2011", "2013", "2017", "2019", "2020"]

    for item in range(3, len(years_list)):
        if item > 2 and item < 6 :
            df = transformer.transform_2011to2017(dfs[item], years_list[item])
            data_list.append(df)
        if item > 5 :
            df = transformer.transform(dfs[item], years_list[item])
            data_list.append(df)
    final_data = pd.concat(data_list).reset_index(drop=True)
    writer.write_to_postgres(df=final_data, db_name=DB_NAME, table_name=TABLE_NAME, connection_string=CONNECTION_STRING)
    result_df = reader.read_from_postgres(db_name=DB_NAME, table_name=TABLE_NAME, connection_string=CONNECTION_STRING)
    
    print("Daftar Orang Terkaya di Indonesia:")
    print(result_df.to_string())


if __name__ == "__main__":
    main()
