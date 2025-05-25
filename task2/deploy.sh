kubectl apply -f ../task1/kuber/configmap.yaml
kubectl apply -f ../task1/kuber/deployment.yaml
kubectl apply -f ../task1/kuber/service.yaml
kubectl apply -f ../task1/kuber/daemonset.yaml
kubectl apply -f ../task1/kuber/cronjob.yaml
kubectl apply -f ./kuber/gateway.yaml
kubectl apply -f ./kuber/virtualservice.yaml
kubectl apply -f ./kuber/destinationrule.yaml
