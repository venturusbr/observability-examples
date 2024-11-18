# Observability Examples

In this repository we will create some examples of observability infrastructure 
with example systems that provide data to it. **These examples are just to test and show how it works!** 
For production some changes must be made on the source code. These changes are related to
provided a more reliable infrastrutucture, like creating scalability to visualization and database endpoints
or securing how scrappers and system parts communicate each other.

The examples are inside the *"./examples"* folder and are divided by programming language. 
In the future, more examples will be added, even with pure infrastructure code will be provided.
All these examples are brought as is by **Venturus**.

# How to deploy the examples

The examples will generally be containerized, but some examples will use an IaC tool like Terraform or Cloudformation to be deployed
on public clouds.
The containerized projects will run on any machine that is running Docker(tested on v20.10) and Docker Compose(tested on v1.25).
The tutorial to run the examples are in their respective folder. In most cases, just following the README.md file is
enough to put them running.

## Running using Docker Compose

1. Go to directory "./examples/python/fastapi"
2. Run: `docker compose run`
3. Check if *prometheus*, *loki*, *graphana* and *fastapi* containers started well.
4. Access Graphana using your browser at: `http://localhost:3000`
   1. First time access user and password are: `admin`
   2. Set your new admin password!
5. Create a Prometheus data source:
   1. On the left side panel in Graphana, go to option **Data sources**
   2. On the top right corner, select  **" + add new data source"**
   3. Select **"Prometheus"**
   4. Configure in the **Conncetion** section the "Prometheus server URL" with `http://prometheus:9090`
   5. Save and test!
6. Import the dashboard:
   1. On the left side panel, go to **Dashboards**
   2. On the top right corner, select  **"New -> New dashboard"**
   3. Select "Import a dashboard"
   4. Upload the "*graphana_dashboard.json*" file
   5. Select the Prometheus data source created early.
   6. Import!
   
## Making counters work

To see the metrics turning into cool graphics we must access the FastAPI application endpoint and then see counters raising in Graphana.

1. Call the "hello" endpoint inserting the following URL in your browser: `http://127.0.0.1:8000/hello`
2. Do it more 5 times
3. Go to Graphana dashboards and see the counter Fastapi Hello raising

# How to contribute

You can contribute in many ways with this project:

To contribute with suggestions, please contact the Venturus team accessing http://www.venturus.org.br .
Or you can try to leave an issue for us.

To contribute with code, just fork our project, do your changes and submit a PR to us. 
We will take a look on changes, and if everything is ok, your code will be merged to our repository.

# Come to work with us

Did you like our work? If you are a person who works with technology, and would love to work with these
kind of things, please come to work with us. Just call our HR through our [https://jobs.kenoby.com/venturus/](site).

If do you represent a company, come to talk with us, we probably have a solution for your problems!

