# PNG Image Compression

This project is meant to compress large png images to maximize storage capacity.
This program takes advantage of the .PNG compression system, which encodes each pixel
in reference to how different it is to the surrounding pixels. By rounding pixels to some
arbitrary multiple, we can approximate their value so that little color is lost, but 
the PNG compression is much more optimized.

---

## Results

<table>
  <tr>
    <td>
      <img src="world_map.png" alt="World Map" style="display: block; margin: 0 auto; width: 200px;" />
      <br><em>World Map - 6.97MB</em>
    </td>
    <td>
      <img src="world_map_compressed.png" alt="Compressed Map" style="display: block; margin: 0 auto; width: 200px;" />
      <br><em>Compressed Map - 3.13MB</em>
    </td>
  </tr>
</table>
This is a 55.1% compression.

<div style="display: flex; justify-content: space-between; align-items: center;">
  <figure style="flex: 1; text-align: center; margin: 0;">
    <img src="car.png" alt="Car" style="width: 90%" />
    <figcaption>Car - 10.9MB</figcaption>
  </figure>

  <figure style="flex: 1; text-align: center; margin: 0;">
    <img src="car_compressed.png" alt="Compressed Car" style="width: 40%" />
    <figcaption>Compressed Car - 1.75MB</figcaption>
  </figure>
</div>
This is an 83.9% compression.

<div style="display: flex; justify-content: space-between; align-items: center;">
  <figure style="flex: 1; text-align: center; margin: 0;">
    <img src="pizza.png" alt="Pizza" style="width: 90%; max-width: 100%;" />
    <figcaption>Pizza - 58.2MB</figcaption>
  </figure>

  <figure style="flex: 1; text-align: center; margin: 0;">
    <img src="pizza_compressed.png" alt="Compressed Pizza" style="width: 90%; max-width: 100%;" />
    <figcaption>Compressed Pizza - 11.3MB</figcaption>
  </figure>
</div>
This is an 80.6% compression

---

As you can see, some vibrancy and saturation is lost, and images with especially bright colors
might appear washed out. Gradients will lose their smoothness too.





