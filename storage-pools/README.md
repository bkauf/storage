

```sh
export PROJECT_ID=
export CLUSTER_NAME=
```

Create  a cluster with boot disks in a pool
```sh

export pool1=projects/$PROJECT_ID/zones/us-central1-a/storagePools/gke-pool-1
export pool2=projects/$PROJECT_ID/zones/us-central1-b/storagePools/gke-pool-2
export pool3=projects/$PROJECT_ID/zones/us-central1-c/storagePools/gke-pool-3

``


```sh

gcloud beta container clusters create $CLUSTERNAME \
    --disk-type=hyperdisk-balanced --storage-pools=$pool1,$pool2,$pool3 \
    --node-locations=us-central1-a,us-central1-b,us-central1-c --machine-type=n4-standard-2 \
    --zone=us-central1-a

```