import multiprocessing
import requests
import concurrent.futures

def downloadFile(url, name):
    response = requests.get(url)
    open(f"file {name}.jpg", 'wb').write(response.content)
    print(f"Finfish Downlaod {name} ")

url = "https://picsum.photos/200/300"
# pros = []

# if __name__ == '__main__':
#     for i in range(5):
#         # downloadFile(url,i)
#         p = multiprocessing.Process(target=downloadFile, args=[url, i])
#         p.start()
#         pros.append(p)

#     for p in pros:
#         p.join()

if __name__ == "__main__":
    with concurrent.futures.ProcessPoolExecutor() as executor:
        l1 = [url for _ in range(5)]
        l2 = [i for i in range(5)]
        results = executor.map(downloadFile, l1, l2)
        for r in results:
            print(r)
