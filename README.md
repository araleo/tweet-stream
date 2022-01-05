# Tweet-Streaming

This is a reusable and replicable service to stream tweets directed at target users. Tweets are streamed using Python's tweepy and stored in a MongoDB instance.

## Usage

To run the containers and start streaming:

```
docker-compose up -d --build
```

This app requires a .env file with the following variables:
```
MONGO_USER=<username>
MONGO_PASS=<password>
MONGO_IP=<ip or service name>
MONGO_DB=<twitter>
SCREEN_NAMES=<twitters handler list>
TWITTER_PUBLIC_KEY=<key>
TWITTER_SECRET_KEY=<key>
TWITTER_PUBLIC_TOKEN=<token>
TWITTER_SECRET_TOKEN=<token>

```

## Tracking users

The SCREEN_NAMES variable in the .env file is supposed to be a comma separated string of twitter handlers that will be tracked by user mentions, ie:

`@spam,@eggs,@bacon`

will stream all tweets in which users @spam or @eggs or @bacon are mentioned (@).

## Data

By default data is being stored in the MongoDB container in a named volume. If you want to persist data in a different way you can change the mongo db settings in the .env file to point to another Mongo database instance, either local, remote or at the cloud.

If you need to change the port, add it after a colon in the `MONGO_IP` variable in the .env file. Ie `0.0.0.0:27018` would try to connect to a Mongo Instance running in port 27018 of the host computer.