# How to query Animations for broken Audio Event references.
Created by Andrew Bertolini  Apr 05, 2019

A newly implemented part of our build process will now fail and stop a build if it finds that any animation is referencing an audio event that no longer exists in the Wwise project. If this happens we will have to follow the error messages to figure out what exactly broke and fix it before the build can be run successfully. In an effort to give us tools to preempt this, we can now run a script locally that will run the audio event validation step. This is great because we can verify the integrity of our audio events in animations before ever sending our builds to the build server. See below for how to execute said script:

1. First you will need to navigate to the root of your Victor repo(code not audio). Your path will be different than the one below so be sure to update to wherever you keep your Victor repo.

![](images/Screen%20Shot%202019-04-03%20at%203.06.23%20PM.png)

2. Once you are in your Victor repo run the following command in terminal:


	./project/victor/scripts/fetch-build-deps.sh && export PYTHONPATH=./project/buildScripts && python -c "import validate_anim_data; validate_anim_data.check_audio_events_all_anims('./EXTERNALS')"

3. The script will run and if there are any broken audio events you should see something like this:

![](images/Screen%20Shot%202019-04-03%20at%203.13.28%20PM.png)

In the above example we can see that the animations *anim_rtp_blackjack_request_01.json* and *anim_rtp_blackjack_timeout_01.json* are referencing audio events that unavailable.


If there are zero broken audio references the readout should reflect that and there should be no animations listed in the output of that script. See Below:

![](images/Screen%20Shot%202019-04-03%20at%203.36.34%20PM.png)
