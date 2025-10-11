# PNG Image Compression

This project is meant to compress large png images to maximize storage capacity.
This program takes advantage of the .PNG compression system, which encodes each pixel
in reference to how different it is to the surrounding pixels. By rounding pixels to some
arbitrary multiple, we can approximate their value so that little color is lost, but 
the PNG compression is much more optimized.

---

## Results

<p>
  <img alt="world_map" src="world_map.png" width="2560"/>
  <img alt="world_map_compressed" src="world_map_compressed.png" width="2560" title="map" />
</p>



