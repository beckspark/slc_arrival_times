import pandas as pd
from datetime import datetime


def get_date():
    global d
    d = input("Enter \'y\' to use today\'s date. Otherwise, enter the date in mm/dd/YYYY format: ")
    if d == "y":
        d = datetime.now()
    else:
        d = datetime.strptime(d, "%m/%d/%Y")
    d = d.strftime("%Y-%m-%d")


def query_db(url):
    global df
    df = pd.read_html(url)
    df = df[0]
    print(df)


def data_slc():
    df["Scheduled Time"] = pd.to_datetime(df["Scheduled Time"], format="%I:%M %p")
    df["Time Slot"] = df["Scheduled Time"].dt.round('15min').dt.strftime("%H:%M")
    df1 = pd.DataFrame(df["Time Slot"].value_counts().reset_index())
    df1.columns = ["Time Slot","Count"]
    df1.to_csv("slc_flights.csv",index=False)


if __name__=="__main__":
    print("This script pulls flights from the SLC Airport website and lets you know what 15 minute slots have the most arriving flights.")
    get_date()
    slc_d = "https://www.slcairport.com/airlines-flights/arrivals-departures/?type=simple&search_flight=&query_leg=A&sortby=departure&sortdir=asc&page=0&results_per_page=600&carrier=&flightNo=&query_city=&query_airline=&query_gate=&query_date1="+d+"+02%3A00%3A00&query_date2="+d+"+23%3A00%3A00"
    query_db(slc_d)
    data_slc()



