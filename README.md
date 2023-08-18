# Task

1. Create the best possible docker image for the application
2. [Integrate docker image with datagrok](https://datagrok.ai/help/develop/how-to/docker_containers)

## Check yourself

To check your **task-1** result try to launch container with a published port:

```bash
docker run -d -p local_port:container_port your_image
```

Then check the application respond:

```bash
curl -Lv 'localhost:local_port/knn?neighbours=7&impute_columns=8&impute_columns=9' -X POST --form file="@/Path/to/file/demog.csv"
```

Application returns a dataset
