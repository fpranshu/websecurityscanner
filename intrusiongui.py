import requests
from bs4 import BeautifulSoup
import tkinter as tk
from tkinter import ttk
from tkinter import scrolledtext

class AllTags:
    def __init__(self, url: str):
        self.base_url = url if url.endswith("/") else url + "/"
        self.all_atags = self.find_all_atags(self.base_url)

    def __str__(self) -> str:
        return f"All links for {self.base_url}"

    def find_all_atags(self, url: str):
        r = requests.get(url)
        if r.status_code == 200:
            soup = BeautifulSoup(r.content, "html.parser")
            return soup.find_all("a")
        else:
            return []  # Return an empty list if the request fails or no anchor tags are found

class LinkResults(AllTags):
    def __init__(self, url: str):
        super().__init__(url)
        self.results = self.build_results_dictionary()

    def check_link_for_http_scheme(self, href: str) -> str:
        if href.startswith(self.base_url):
            return href
        elif href.startswith("/"):
            href = self.base_url + href.lstrip("/")
            return href
        elif href.startswith("./"):
            return self.base_url + href.lstrip("./")
        elif href.startswith("../"):
            return self.base_url + href.lstrip("../")
        else:
            return None

    def build_results_dictionary(self) -> dict:
        results = {}
        try:
            for tag in self.all_atags:
                href = tag.get("href")
                parsed_url = self.check_link_for_http_scheme(href)
                if parsed_url is not None:
                    parsed_url_status_code = requests.get(parsed_url).status_code
                    if parsed_url_status_code in results:
                        results[parsed_url_status_code].append(parsed_url)
                    else:
                        results[parsed_url_status_code] = [parsed_url]
        except:
            pass
        return results

class LinkAnalysis(AllTags):
    def __init__(self, url: str):
        super().__init__(url)
        self.obsolete_attrs = self.obsolete_attributes(self.all_atags)
        self.unsafe_attrs = self.unsafe_attributes(self.all_atags)

    def obsolete_attributes(self, links) -> dict:
        if links is None:
            return {}  # Return an empty dictionary if links is None

        OBSOLETE_ATTRS = ("charset", "coords", "name", "rev", "shape")
        return_dict = {}
        for link in links:
            obs_link_attrs = [
                attribute for attribute in OBSOLETE_ATTRS if link.get(attribute)
            ]
            if obs_link_attrs:
                href = link.get("href", "")
                if href in return_dict:
                    for _attr in obs_link_attrs:
                        return_dict[href].append(_attr)
                else:
                    return_dict[href] = obs_link_attrs
        return return_dict

    def unsafe_attributes(self, links) -> dict:
        if links is None:
            return {}  # Return an empty dictionary if links is None

        return_dict = {}
        for link in links:
            if link.get("target"):
                if link.get("rel") and "noopener" in link.get("rel"):
                    return_dict[link] = False
                else:
                    return_dict[link] = True
        return return_dict

class LinkAnalyzerGUI:
    def __init__(self, master):
        self.master = master
        master.title("Link Analyzer")

        # URL Entry
        self.label = ttk.Label(master, text="Enter the URL:")
        self.label.grid(row=0, column=0, padx=10, pady=10)
        self.url_entry = ttk.Entry(master, width=50)
        self.url_entry.grid(row=0, column=1, padx=10, pady=10)

        # Analyze Button
        self.analyze_button = ttk.Button(master, text="Analyze Links", command=self.analyze_links)
        self.analyze_button.grid(row=0, column=2, padx=10, pady=10)

        # Result Text
        self.result_text = scrolledtext.ScrolledText(master, wrap=tk.WORD, width=80, height=20)
        self.result_text.grid(row=1, column=0, columnspan=3, padx=10, pady=10)

    def analyze_links(self):
        url_to_check = self.url_entry.get()

        # LinkResults
        link_results = LinkResults(url_to_check)
        results = link_results.results

        # LinkAnalysis
        link_analysis = LinkAnalysis(url_to_check)
        unsafe_attrs = link_analysis.unsafe_attrs

        # Display Results
        self.result_text.delete(1.0, tk.END)  # Clear previous results

        if results:
            self.result_text.insert(tk.END, "Link Results:\n")
            for status_code, urls in results.items():
                for url in urls:
                    self.result_text.insert(tk.END, f"HTTP Code {status_code} - {url}\n")

        if unsafe_attrs:
            self.result_text.insert(tk.END, "\nUnsafe Attributes:\n")
            for link, is_unsafe in unsafe_attrs.items():
                self.result_text.insert(tk.END, f"{link} is {'Unsafe' if is_unsafe else 'Safe'}\n")
        else:
            self.result_text.insert(tk.END, "\nAll links are safe.")

if __name__ == "__main__":
    root = tk.Tk()
    app = LinkAnalyzerGUI(root)
    root.mainloop()
