from REST_like_socket import SyncedResources
from time import sleep

syncedResources = SyncedResources(
    isResource_host=False,
    synchronize_to="X.X.X.X",
)

for _ in range(30):
    num = syncedResources.read("num")
    syncedResources.write("num", num - 1)
    print(num)
    sleep(0.5)
