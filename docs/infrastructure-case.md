# Router-Level VPN / Network Automation Case

Infrastructure case documenting practical work with router-level traffic routing.

## Goal

Route selected home-network devices through a centrally configured VPN/proxy layer instead of installing and maintaining a separate client on every device.

## Environment

- Xiaomi Mesh System AX3000 (RA82)
- Qualcomm IPQ5018 platform
- Router-level configuration
- SSH-based administration
- Proxy/VPN routing

## Engineering concepts demonstrated

- Understanding device and firmware constraints before deployment
- Router administration and SSH workflows
- Centralized network routing
- Persistent configuration / restart recovery
- Selective direct-routing exceptions for services that should bypass the proxy
- Connectivity and performance verification
- Rollback planning

## Architecture

```text
Phones / TV / VR / Cameras
           ↓
       Home Router
        ↙      ↘
 DIRECT rules   VPN / Proxy Route
        ↘      ↙
        Internet
```

## Portfolio note

This is presented as infrastructure and networking experience. Credentials, server addresses, private routing configuration and device-specific secrets are not included.
