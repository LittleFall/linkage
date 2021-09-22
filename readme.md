# Linkage

Thanks to [manim](https://github.com/3b1b/manim), the great math print lib. 

Thanks to [为什么连杆可以画出曲线](https://www.bilibili.com/medialist/play/594380494?from=space&business=space&sort_field=pubtime), the great Popular Science video for linkage.

## Run

1. [Install manim](https://github.com/3b1b/manim#installation).

2. Run the linkages by `manimgl <source> <scene>` like:
    ```sh
    manimgl main.py Linkage0
    ```
3. Generate mp4
    ```sh
    manimgl -w main.py PeaucellierLinkage
    ```
4. Generate gif
    ```sh
    ffmpeg -i videos/PeaucellierLinkage.mp4 out.gif
    ```


## TODO

See TODO in codes.

## Agreement

### dot

- color red: the driver, move around a circle.
- color yellow: point that will be driven.
- color blue: fixed point.
- color green: driven point used to draw the locus.
