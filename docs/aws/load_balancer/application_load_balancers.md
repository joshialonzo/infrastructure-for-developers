# Application Load Balancers

* Application load balancers operate at the application layer (layer 7) of the OSI model and handle HTTP/HTTPS traffic.
* They support various targets including:
    * EC2 instances
    * IP addresses (useful for hybrid on-premises and cloud setups)
    * Containers
    * Lambda functions for serverless applications
* You can configure them as:
    * internet-facing (public IP)
    * internal (private network only)
* They offer flexible routing options based on:
    * HTTP headers,
    * host headers,
    * URL paths,
    * HTTP methods,
    * query strings,
    * source IP addresses,

enabling precise traffic distribution.