# Turn to recorded angle.
Created by Daria Jerjomina May 04, 2017

In some cases, because of the friction, momentum and related factors Cozmo can end up at the position  not expected from the previous body motion key frames. This can be problematic if for example at the end of animation he needs to face the same direction as he faced in the beginning.

In order to use turn to recorded angle please use x:recorded_angle_ctr positioned next to moac ctr, and highlighted in the image below

![](images/01_recorded_angle_ctr.png)

x:recorded_angle_ctr you is one of the extra ctrs, so in order to see it, please make sure that Extra Controls attribute of x:mech_all_ctrl is on.

![](images/02_extraCtrs.png)

Place a key for x:recorded_angle_ctr, at the frame where Cozmo is faced the way you want him to face at the end of the clip. For example if you want Cozmo to face the way he is facing in the beginning that key should be placed at the first frame of the clip.

That is all you need, no other keyframes are required.

Please place only one recorded_angle_ctr key per clip, if you place more than that, only the first one will be counted.

![](images/03_oneKey.png)

In most cases this is all you need to do in order to correct your movement animation.

However, if your last turn looks not quite as expected, you can use the attributes on the recorded_angle_ctr in order to adjust it.

![](images/04_attrs.png)

*Accel, Decel* - Acceleration and Deceleration in degrees per second. Means how fast Cozmo should get to the speed of the turn and out of it. By default it is set to 1000, which means it can go from 0 deg/s to 1000 deg/sec in 1 sec. Kevin Yoon’s tests showed that this value gave the most accurate result. You can play around with this attribute however to see if different values would give a more pleasing outcome. Bigger value won’t look much different, but a smaller one will.

*Overwrite Last* - By default is set to be off. Which means that after all the movement is completed cozmo will turn to be facing the direction it was recorded at.

However, if your last movement is turn in place and an additional turn makes it look choppy, you can turn this attribute off. What that will do is replace your last turn with the turn to recorded angle and will use your last turns speed and duration. This result might look somewhat robotic, which is why it is off by default.

*Duration Ms* - If Overwrite Last is off - duration of the last turn in milliseconds. Correction turn can take different amount of time to complete. If this attribute is set too low correction turn might not have enough time to complete. If it is set too high, even once the turn is completed the next animation will not start unless the duration time gets completed.

In the same animation duration for the last correction turn can be different, so it should be animator's decision on what is more important in the case of this animation - cozmo sometimes not completing the turn, or there sometimes being a lag time between the current and the next animation.

If Overwrite Last is on, duration is being taken the same as it was on the last turn, and in this case Duration Ms attribute serves as an extra buffer time. So in case your last turn doesn’t get completed, you can increase it.

Note: if Duration Ms is set to 0, that’s being handled as a human error, and treated as 500ms

Below is an example with a peekaboo animation, the first one without the correction turn and the second one with one.

[peekaboo noAdjustment](images/peekaboo_noAdjustment.mov)

[peekaboo adjusted](images/peekaboo_adjusted.mov)
