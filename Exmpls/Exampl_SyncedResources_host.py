from REST_like_socket import SyncedResources
from time import sleep

syncedResources = SyncedResources(isResource_host=True)

syncedResources.server.start()

syncedResources.write("num", 0)

for _ in range(30):
    num = syncedResources.read("num")
    response = syncedResources.write("num", num + 1)
    print(num)
    sleep(0.5)


syncedResources.server.join()
