# 1. How to use Dockerfile

#### 1.1. You have to install docker by yourself.
#### 1.2. You should be in your venv where you have NESCAFEBOT_TOKEN, to do that:
(if you're using Windows, replace 'bin' with 'Scripts' elsewhere)
> \$ python -m venv venv_bot  
> \$ nano venv_bot/bin/activate

At the end of the file place (instead of _token_ place actual token):
> \> export NESCAFEBOT_TOKEN="_token_"

(If you've done previous steps, you don't need to redo them later)  
then activate it:
> \$ source venv_bot/bin/activate

#### 1.3. Run docker container:
First, start docker:
> \$ sudo systemctl start docker

(At this stage you should be in directory with the Dockerfile [use 'cd'])   
Build an image:
> \$ docker build --tag nescafebot --build-arg NESCAFEBOT_TOKEN=$NESCAFEBOT_TOKEN -f Dockerfile.py .

Run the image in interactive mode within a container:
> \$ docker run -it nescafebot

Check that your token has been passed:
> \$ echo $NESCAFEBOT_TOKEN

Start the bot:
> \$ python bot/start_bot.py

To exit the container:
> \> exit