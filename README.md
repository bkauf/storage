From https://cloud.google.com/kubernetes-engine/docs/how-to/persistent-volumes/gce-pd-csi-driver
###Enabling the Compute Engine persistent disk CSI Driver on an existing cluster
export CLUSTER_NAME="cluster-1"
gcloud container clusters update $CLUSTER_NAME \
   --update-addons=GcePersistentDiskCsiDriver=ENABLED# storage
