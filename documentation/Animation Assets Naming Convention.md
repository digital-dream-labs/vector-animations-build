# Animation Assets Naming Convention

General Rules

- All LOWERCASE
- Each word is separated by an underscore
- Variation numbers at the end are double digit (audio events will not have variations in name)
- No special characters (!@#$%^)
- Sprite Sequences use a PNG format and need to be compressed into .tar files before committed.

### Animations = anim_(feature, behavior name)_(action)_(variation)
Example 1: anim_blackjack_getin_01 = animation + part of the blackjack feature + a get in + variation #1

Example 2: anim_chargerdocking_leftturn_01  = animation + feature + get in + variation #1

### Animation Groups = ag_(feature, behavior name)_(action)_(variation)
Example 1: ag_blackjack_getin_01 = animation group + part of the blackjack feature + a get in + variation #1

Example 2: anim_chargerdocking_leftturn_01  = animation group + feature + get in + variation #1


### Sprite Sequences = face_(feature)_(activity name)_(frame#).png

examples:
face_avs_getin_0004.png = sprite sequence + the avs feature + action + 4 digit frame number.

face_holiday_lights_01_0004.png

face_knowledgegraph_fail_0004.png

face_lookatphone_loop_0004.png


### SFX = sfx_(type)_(action)_(event action)

ex: sfx_ui_button_generic_play = sound fx + ui + generic button press + play event

sfx_ui_button_generic_play

sfx_ui_window_open_play

sfx_ui_window_close_play


### VO = vo_(character)_(gameplay, open play, activity)_(game name, activity name)_(action)_(variation)
ex: vo_coz_gp_st_tap_effort_play = vo + cozmo + gameplay + speed tap

ex: vo_coz_shared_laugh_play = vo + cozmo + shared anywhere + laugh

ex: vo_coz_proc_happy_play

vo_coz_gp_st_pounce_effort_play

vo_coz_gp_st_coz_win_play

vo_coz_gp_st_coz_lose_play

vo_coz_shared_laugh_play

vo_coz_proc_happy_play

## Notes
Don't use action descriptions as feature names

### example 1: anim_mutemic_micon_01

This animation turned out confusing. It communicates muting the microphone, and turning the microphone on in the same animation – two conflicting ideas. We ended up replacing "mutemic" with "micstate".

### Example 2: anim_rtpickup_putdown_01

Same idea, 2 conflicting actions.

## Common Terminology

getready
: Content switching. This animation needs to switch the attention of the user from the device to Cozmo.

getin
: An animation that plays when the robot gets into a behavior (like a game or a state).

getout
: An animation that plays when the robot gets out of a behavior (like a game or a state).

idle
: An animation that plays when the robot has to stay put, but look alive. Usually plays as a loop.

wait
: A version of an idle loop. The robot is waiting for the player and has to stay put.

drive_start
: Part of a driving set. This animation plays when the robot begins to drive.

drive_loop
: Part of a driving set. This animation loops while the robot is driving.

drive_end
: Part of a driving set. This animation plays when the robot arrived at it's destination.

onlyaudio
: This animation only plays an audio and doesn't have any animation keyframes.

success
: An animation that plays after the robot did a successful action.  ex: anim_fistbump_success_01

fail
: An animation that plays after the robot failed to do an action. ex: anim_fistbump_fail_01

reaction
:

head_angle_-20
: A head angle animation. Plays an animation that starts and ends at a -20° head angle.

head_angle_20
: A head angle animation. Plays an animation that starts and ends at a 20° head angle.

head_angle_40
: A head angle animation. Plays an animation that starts and ends at a 40° head angle.

wakeup
: An animation that plays when the robot turns on while on the charger.

fix
: Part of the need/repair feature.

Intensity
:

wingame
:

losegame
:
