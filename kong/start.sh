
```bash
kubectl apply -f https://raw.githubusercontent.com/Kong/kubernetes-ingress-controller/main/deploy/single/all-in-one-dbless.yaml


kubectl create ns bookinfo
kubectl -n bookinfo apply -f https://raw.githubusercontent.com/istio/istio/master/samples/bookinfo/platform/kube/bookinfo.yaml


export PROXY_IP=$(kubectl -n kong get svc kong-proxy -o=jsonpath='{.status.loadBalancer.ingress[0].ip}')

```