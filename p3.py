def fetch_global_data(self):
    url = "https://corona.lmao.ninja/v3/covid-19/all"
    response = requests.get(url)
    data = response.json()

    self.data_text.delete(1.0, tk.END)
    self.data_text.insert(tk.END, "Global Data:\n")
    self.data_text.insert(tk.END, f"Cases: {data['cases']}\n")
    self.data_text.insert(tk.END, f"Deaths: {data['deaths']}\n")
    self.data_text.insert(tk.END, f"Recovered: {data['recovered']}\n")
    self.data_text.insert(tk.END, f"Active Cases: {data['active']}\n")
    self.data_text.insert(tk.END, f"Vaccinations: {data['vaccinations']}\n")
    self.data_text.insert(tk.END, f"People Vaccinated: {data['people_vaccinated']}\n")
    self.data_text.insert(tk.END, f"People Fully Vaccinated: {data['people_fully_vaccinated']}\n")