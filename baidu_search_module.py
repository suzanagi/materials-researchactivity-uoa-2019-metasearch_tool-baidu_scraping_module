import sys
import requests
from bs4 import BeautifulSoup
from result_item import ResultItem

def search(query):
    # Prepare a list for returning the search results
    result = list()
    # Prepare a parameter for the given query
    param = {"ie": "utf-8", "wd": query}
    try:
        # Get the Bing search result page for the query
        rt = requests.get("http://www.baidu.com/s", params=param)
        # print("URL: " + rt.text)
        # Analyse the result page using BeautifulSoup
        soup = BeautifulSoup(rt.text, "html.parser")

    except:
        print("Internet Disconnected. Connect to download text.")
        '''
        import traceback
        traceback.print_exc()
        '''
    # Obtain topics and URL element by the BeautifulSoup function
    results = soup.findAll("div", {"class":"result"})
    lists = list()
    for result_section in results:
        lists.append(result_section.find("h3", {"class":"t"}))
    for item in lists:
        item_text = item.find("a").text
        item_href = item.find("a").attrs["href"]
        # Put the results in the list to be returned
        if item_text and item_href:
            result.append(ResultItem(item_text, item_href))
    # Return the result list
    return result

# Main Function
if __name__ == "__main__":
    # Prepare query vairable
    query = sys.argv[1]
    # Append multiple query words with "+"
    for arg in sys.argv[2:]:
        query = query + " " + arg
    # Experiment the search function
    result = search(query)

    # Print the result list to the command line
    for item in result:
        print("[title] "+item.title)
        print("[url] "+item.url)

