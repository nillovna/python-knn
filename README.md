Task:
1. Create the best possible docker image for the application
To checkout your result try to launch container with a published port:
`docker run -d -p local_port:container_port yours_image`
Then checkout application respond:
`curl -Lv 'localhost:local_port/knn?neighbours=7&impute_columns=8&impute_columns=9' -X POST --form file="@/Path/to/file/demog.csv"`
The dataset will returns
2. [Integrate docker image with datagrok](https://datagrok.ai/help/develop/how-to/docker_containers)
