from REST_like_socket import SyncedResources
from time import sleep

syncedResources = SyncedResources(
    isResource_host=True,
    port=55555,
)

syncedResources.server.start()

syncedResources.write("num", 0)


syncedResources.server.join()
