This application covers Four major API for the assignment.
GetHtml
GetAllProductDetails
GetProductDetails
GetPriceTrend

The application is also Dockerized. To create a Docker container
docker build --tag ciq .

To run the container
docker run -d -p 5000:5000 ciq

Things could be implemented but I couldn't due to time restrain and some Family Emergency
1. A Database to store all this Info. My preference would be MySQL.
2. A final API `GetProductDetailsHistory` this is a interesting API i could apply binary search with some conditions. I can discuss more if on call.
3. Some more error and exception handling and some comments as well. I tried to follow camel casing and suitable naming conventions for more readable code.